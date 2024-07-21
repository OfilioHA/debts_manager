from sqlalchemy.ext.declarative import declared_attr
from extensions.alchemy import db
from datetime import datetime


class TimeStampMixin (object):

    @declared_attr
    def created_at(self):
        return db.Column(db.String, default=datetime.now().strftime("%Y-%m-%d %H:%M"), nullable=False)

    @declared_attr
    def modified_at(self):
        return db.Column(db.String, nullable=True)
