from app import app,db
from app.models import User,followers,Posts
from flask_login import current_user

# F = followers()
#
# print(F.is_following(1))
p = Posts()
t = 1
print(db.session.query(followers,Posts).join(followers,Posts.anther_id==followers.followed_id).filter(followers.follower_id==t))