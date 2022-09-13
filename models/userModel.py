from .connection.mysql import connection_mysql
from sqlalchemy import Integer, String, Boolean, Column, ForeignKey
import uuid
db, api = connection_mysql()

class Account(db.Model):
    
    id = Column(String(60), primary_key=True, default=uuid.uuid4 )
    fullname = Column(String(60))
    age = Column(Integer)
    uf = Column(String(2))
    username = Column(String(50))
    password = Column(String(1000))
    online = Column(Boolean, default=False)
    urlPic_Porfile = Column(String(60))
    urlPic_Banner = Column(String(60))
    bio = Column(String(255))
    friends_count = Column(Integer)
    
    def selectUser(self):
        return {
                "id": self.id,
                "fullname": self.fullname,
                "online": self.online,

            }
        
    def userGetby(self):
            
        return {
                "id": self.id,
                "fullname": self.fullname,
                "age": self.age,
                "uf": self.uf,
                "pwd": self.password,
                "username": self.username,
                "urlPic_profile": self.urlPic_Porfile,
                "urlPic_banner": self.urlPic_Banner,
                "online": self.online,
                "friends_count": self.friends_count,
                "bio": self.friends_count,
                "online": self.online
            }
        

    
    
    




#db.drop_all()  
#db.create_all()