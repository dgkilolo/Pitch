from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    
    # reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f'User {self.username}'

    # def save_review(self):
    #     db.session.add(self)
    #     db.session.commit()

    # @classmethod
    # def get_reviews(cls,id):
    #     reviews = Review.query.filter_by(movie_id=id).all()
    #     return reviews

class Pitch(db.Model):
  
  __tablename__ ='pitches'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(700))
  posted = db.Column(db.DateTime, default=datetime.utcnow)  
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  category = db.Column(db.String(255))
  

  def save_pitch(self):

    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_pitches(cls,category):
    pitches = Pitch.query.filter_by(category=category).all()
    return pitches  

  @classmethod
  def get_pitch(cls,id):
    pitch=Pitch.query.filter_by(id=id).first()
    return pitch


# class Review(db.Model):

#     __tablename__ = 'reviews'

#     id = db.Column(db.Integer,primary_key = True)
#     movie_id = db.Column(db.Integer)
#     movie_title = db.Column(db.String)
#     image_path = db.Column(db.String)
#     movie_review = db.Column(db.String)
#     posted = db.Column(db.DateTime,default=datetime.utcnow)
#     user_id = db.Column(db.Integer,db.ForeignKey("users.id"))

#     all_reviews = []

#     def __init__(self,movie_id,title,imageurl,review):
#         self.movie_id = movie_id
#         self.title = title
#         self.imageurl = imageurl
#         self.review = review


#     def save_review(self):
#         Review.all_reviews.append(self)


#     @classmethod
#     def clear_reviews(cls):
#         Review.all_reviews.clear()

#     @classmethod
#     def get_reviews(cls,id):

#         response = []

#         for review in cls.all_reviews:
#             if review.movie_id == id:
#                 response.append(review)

#         return response


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'
