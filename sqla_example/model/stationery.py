from sqlalchemy.orm import Mapped, mapped_column
from sqla_example.model.base import Base


class Notebook(Base):
    """A paper notebook."""
    __tablename__ = "stationery_notebook"
    id: Mapped[int] = mapped_column(primary_key=True)
