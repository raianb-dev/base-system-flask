from .connection.mysql import connection_mysql
from sqlalchemy import Integer, String, Boolean, Column
db, api = connection_mysql()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(60))
    age = Column(Integer)
    
    def selectUser(self):
        return {
            "account":{
                "id": self.id,
                "fullname": self.fullname,
                "age": self.age
            }
        }
    





    
#db.create_all()