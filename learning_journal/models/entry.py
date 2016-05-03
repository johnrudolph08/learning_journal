import datetime
from learning_journal.models.meta import Base, DBSession

from sqlalchemy import(
    Column,
    Integer,
    Unicode,
    UnicodeText,
    DateTime,
    )

class Entry(Base):

    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255), unique= True, nullable = False)
    body = Column(UnicodeText)
    created = Column(DateTime, default=datetime.datetime.utcnow)
    edited = Column(DateTime, default=datetime.datetime.utcnow)

    @classmethod
    def all(cls):
        """Return a query of users sorted by name."""
        Entry = cls
        q = DBSession.query(Entry).order_by(Entry.created)
        return q

    @classmethod
    def by_id(cls, id_val):
        """Return a query of users sorted by name."""
        Entry = cls
        q = DBSession.query(Entry).get(id_val)
        return q

