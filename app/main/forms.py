from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField,FileField
from wtforms.validators import Required

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class NewPitch(FlaskForm):
  title = StringField("Pitch Title", validators = [Required()])
  pitch = TextAreaField("Description", validators = [Required()])  
  category = SelectField("Category",
  choices=[("pun","pun"),("quote","quote"),("tongue twister","tongue twister")],validators = [Required()])
  submit=SubmitField("Add Pitch")