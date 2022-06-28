from application import db
from application.models import Users,Posts

db.drop_all()
db.create_all()

rootUser = Users(userName="Root",firstName="root",lastName="root")
db.session.add(rootUser)
db.session.commit()

rootUser = Users(userName="Admin",firstName="admin",lastName="admin")
db.session.add(rootUser)
db.session.commit()

rootPost= Posts(message="root" ,userID=1)
db.session.add(rootPost)
db.session.commit()

rootPost= Posts(message="admin" ,userID=2)
db.session.add(rootPost)
db.session.commit()