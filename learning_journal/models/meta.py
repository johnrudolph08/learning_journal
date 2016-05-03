from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


#changed structure of model to conform to: 
#http://docs.pylonsproject.org/projects/pyramid-blogr/en/latest/basic_models.html

#deleted out MyModel