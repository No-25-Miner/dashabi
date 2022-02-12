from app import app,db
from app.models import User

u = User(username='susan', email='susan@example.com')
u.set_password('cat')
db.session.add(u)
db.session.commit()
