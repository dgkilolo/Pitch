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
    
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))

    pitches=db.relationship('Pitch',backref='user',lazy="dynamic")
    comment=db.relationship('Comment',backref='user',lazy='dynamic')

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

    

class Pitch(db.Model):
  
  __tablename__ ='pitches'

  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(255))
  description = db.Column(db.String(700))
  posted = db.Column(db.DateTime, default=datetime.utcnow)  
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  category = db.Column(db.String(255))
  # comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
  

  def save_pitch(self):

    db.session.add(self)
    db.session.commit()

  def get_comment(self):
    pitches = Pitch.query.filter_by(id = self.id).first()
    comments = Comment.query.filter_by(pitch_id = pitch.id).all()    
    return comments 

  @classmethod
  def get_pitches(cls,category):
    pitches = Pitch.query.filter_by(category=category).all()
    return pitches  

  @classmethod
  def get_pitch(cls,id):
    pitch=Pitch.query.filter_by(id=id).first()
    return pitch

  

class Comment(db.Model):
  
  __tablename__='comments'
  id = db.Column(db.Integer,primary_key=True)
  pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
  comment = db.Column(db.String)
  
  
  def save_comment(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def get_comments(cls, id):
      comment = Comment.query.filter_by(pitch_id = id).all()
      return comment
  
    

  def __repr__(self):
    
    return f'User {self.content}'  







