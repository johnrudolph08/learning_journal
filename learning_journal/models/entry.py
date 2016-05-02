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
    def all(class_):
        """Return a query of users sorted by name."""
        Entry = class_
        q = DBSession.query(Entry).all()
        return q

    @classmethod
    def by_id(class_, id):
        """Return a query of users sorted by name."""
        Entry = class_
        q = DBSession.query(Entry).get(id)
        return q

