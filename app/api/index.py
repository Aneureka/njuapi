from flask import render_template
from flask import Blueprint

index = Blueprint('index', __name__)


@index.route('/', methods=['GET'])
def welcome():
    return render_template('index.html')
