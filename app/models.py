import sqlalchemy.orm as so
import sqlalchemy as sa

from sqlalchemy.orm import Mapped, mapped_column
from app import db
from datetime import datetime

class Transaction(db.Model):
    id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
    date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False)
    type: Mapped[str] = mapped_column(db.String, nullable=False)
    description: Mapped[str] = mapped_column(db.String, nullable=False)
    paid_in: Mapped[float] = mapped_column(db.Float)
    paid_out: Mapped[float] = mapped_column(db.Float)
    balance: Mapped[float] = mapped_column(db.Float, nullable=False)

    __table_args__ = (
        sa.UniqueConstraint(date, type, description, paid_in, paid_out, balance),
    )

    def __repr__(self):
        return f"{self.date} | {self.type} | {self.description} | {self.paid_in} | {self.paid_out} | {self.balance}\n"