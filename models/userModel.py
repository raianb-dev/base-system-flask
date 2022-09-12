from .connection.mysql import connection_mysql
from sqlalchemy import Integer, String, Boolean, Column
import uuid
db, api = connection_mysql()

class User(db.Model):
    __tablename__ = 'users'
    id = Column(String(60), primary_key=True, default=uuid.uuid4 )
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
    





#db.drop_all()  
#db.create_all()