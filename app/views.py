from flask import render_template, request, flash, jsonify
from flask_restful import Resource, Api
from app import app
from .forms import EmailForm
from validate_email import validate_email

@app.route('/', methods=['GET', 'POST'])
@app.route('/email', methods=['GET', 'POST'])
def login():
    form = EmailForm()
    if request.method == 'POST':
        valid_email = check_email(str(form.email.data))
        if (valid_email):
            flash(str(form.email.data) + " is valid ")
            return render_template('email.html',
                            msg_color="green",
                            form=form)
        else:
            flash(str(form.email.data) + " is invalid ")
            return render_template('email.html',
                            msg_color="red",
                            form=form)
    elif request.method == 'GET':
        return render_template('email.html',
                            # msg_color="green",
                            form=form)
def check_email(email):
    res = validate_email(email.strip(),verify=True, check_mx=True, debug=True, smtp_timeout=10)
    return res

api = Api(app)
class CheckEmailExists(Resource):
    def get(self, email):
        return jsonify({email: check_email(email)})

    def put(self, email):
        return jsonify({email: check_email(email)})

api.add_resource(CheckEmailExists, '/emails/<string:email>')