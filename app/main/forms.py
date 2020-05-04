from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitch(FlaskForm):
  title = StringField("Pitch Title", validators = [Required()])
  pitch = TextAreaField("Description", validators = [Required()])  
  
  submit=SubmitField("Add Pitch")