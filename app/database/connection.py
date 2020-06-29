import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import sessionmaker

class DBConnectionManager:
    '''This class handles connection to the database.'''
    Base = declarative_base()
    conn_url = os.environ.get('DB_CONN_URL')
    engine = create_engine(conn_url)
    Session = sessionmaker(bind=engine)


    @staticmethod
    def get_db():
        '''Returns a session.
        
        :return: The session
        :rtype: Session
        '''
        return Session()
