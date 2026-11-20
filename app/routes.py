import datetime
import csv
import os

from flask import render_template, redirect, url_for, flash, request
from sqlalchemy.exc import IntegrityError
from sqlalchemy import func, select
from werkzeug.utils import secure_filename

from app import app
from app import db
from app.models import *
from app.forms import *


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/csv-upload', methods=['GET', 'POST'])
def csv_upload():
    form = UploadForm()

    if form.validate_on_submit():
        file = form.file.data
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        with open(os.path.join(app.config["UPLOAD_FOLDER"], filename), "r") as f:
            reader = csv.reader(f, delimiter=",")
            for i in range(5):
                next(reader, None)
            for row in reader:
                if not row:
                    continue
                try:
                    date_str = row[0]
                    date_obj = datetime.strptime(date_str, "%d %b %Y")

                    if row[3]:
                        paid_out = float(row[3][1:])
                    else:
                        paid_out = 0

                    if row[4]:
                        paid_in = float(row[4][1:])
                    else:
                        paid_in = 0

                    new_transaction = Transaction(
                        date = date_obj,
                        type = row[1],
                        description = row[2],
                        paid_in = paid_in,
                        paid_out = paid_out,
                        balance = float(row[5][1:])
                    )

                    db.session.add(new_transaction)
                except:
                    continue

                try:
                    db.session.commit()
                except IntegrityError:
                    db.session.rollback()
                    print("Identical record already exists!")

        return redirect(url_for("index"))

    return render_template("csv_upload.html", form=form)


@app.route('/view-transactions', methods=['GET', 'POST'])
def view_transactions():
    return render_template('view_transactions.html')


@app.route('/analysis', methods=['GET', 'POST'])
def analysis():
    return render_template('analysis.html')