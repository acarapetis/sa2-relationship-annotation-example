from __future__ import annotations # Removing this fixes the error

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqla_example.model.base import Base
import sqla_example.model.computers

class Person(Base):
    __tablename__ = "person"
    id: Mapped[int] = mapped_column(primary_key=True)
    laptop_id: Mapped[int] = mapped_column(ForeignKey(sqla_example.model.computers.Notebook.id))
    laptop: Mapped["sqla_example.model.computers.Notebook"] = relationship()
