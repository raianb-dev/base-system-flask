from .connection.mysql import connection_mysql
from sqlalchemy import Integer, String, Boolean, Column
db, api = connection_mysql()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(60))
    age = Column(Integer)
    
    
#db.create_all()