from sqlalchemy import orm

from .model import computers, person, stationery

orm.configure_mappers()
