from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch
from flask_login import login_required, current_user
from .forms import UpdateProfile,NewPitch
from .. import db,photos
# import markdown2

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch'

    return render_template('index.html', title = title)


@main.route('/puns')
def pun():

    '''
    View root page function that returns the puns page and its data
    '''
    title = 'Pitch'
    pitches = Pitch.query.all()
    return render_template('puns.html', title = title, pitches = pitches)

@main.route('/quotes')
def quote():

    '''
    View root page function that returns the quote page and its data
    '''
    title = 'Pitch'
    return render_template('quotes.html', title = title)

@main.route('/twister')
def twister():

    '''
    View root page function that returns the tongue twister page and its data
    '''
    title = 'Pitch'
    return render_template('twister.html', title = title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/puns/new/<userID>', methods = ['GET','POST'])
@login_required
def add_pitch(userID):
  user = User.query.filter_by(username = userID).first()  
  form = NewPitch()
  if form.validate_on_submit():
    title = form.title.data
    pitch = form.pitch.data    

    # Updated pitch instance
    new_pitch = Pitch(title=title,description=pitch, user_id = user.id)

    # Save pitch method
    new_pitch.save_pitch()
    return redirect(url_for('.pun'))

  title = 'New pitch'
  return render_template('newpitch.html',title = title,pitch_form=form )

