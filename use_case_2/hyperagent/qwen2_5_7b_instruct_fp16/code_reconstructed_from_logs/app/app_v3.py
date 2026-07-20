from flask import Flask, render_template


def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return 'Welcome to the Ticket Management System'

    @app.route('/login')
    def login():
        from .forms import LoginForm
        form = LoginForm()
        return render_template('login.html', form=form)

    return app


from .forms import LoginForm  # Ensure this is defined in a forms.py file

if __name__ == '__main__':
    create_app().run(debug=True)
""")

# Create the forms.py file
with open("app/forms.py", "w") as f:
    f.write("""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')