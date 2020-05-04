from flask import render_template
from . import main
# from ..models import Review,User
from flask_login import login_required, current_user
# from .. import db,photos
# import markdown2

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    title = 'Pitch'

    return render_template('index.html', title = title)