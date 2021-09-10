from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
app.secret_key = "helloworld"

admin_email = "admin@email.com"
admin_password = "12345678"

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField(label='Password', validators=[validators.DataRequired(), validators.length(min=8)])
    submit = SubmitField(label="Submit")





@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        print(login_form.email.data, login_form.password.data )
        if login_form.email.data == admin_email and login_form.password.data == admin_password:
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)