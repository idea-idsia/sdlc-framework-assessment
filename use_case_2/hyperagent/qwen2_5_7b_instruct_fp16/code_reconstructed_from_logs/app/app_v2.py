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