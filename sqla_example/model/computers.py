from sqlalchemy.orm import Mapped, mapped_column
from sqla_example.model.base import Base


class Notebook(Base):
    """A laptop."""
    __tablename__ = "computer_notebook"
    id: Mapped[int] = mapped_column(primary_key=True)
