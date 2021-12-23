from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker, declarative_base

from lab4.part2.database.database_config import user, password, host, dialect, database


class Singleton(type):
    """
        A metaclass that is used to implement singleton pattern

    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DBManager(metaclass=Singleton):
    """
        A class that represents a convenient way to get a database session

    """

    base = declarative_base()

    def __init__(self):
        self.engine = create_engine(f'{dialect}://{user}:{password}@{host}/{database}')
        self.sessionmaker = sessionmaker(self.engine)
        self.base.metadata.create_all(self.engine)

    @property
    def engine(self):
        return self.__engine

    @engine.setter
    def engine(self, value):
        if not isinstance(value, Engine):
            raise TypeError('engine must be of type Engine')
        self.__engine = value

    @property
    def sessionmaker(self):
        return self.__session

    @sessionmaker.setter
    def sessionmaker(self, value):
        if not isinstance(value, sessionmaker):
            raise TypeError('sessionmaker must be of type sessionmaker')
        self.__session = value

