from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/helpdesk')
def helpdesk_redirect():
    return redirect(url_for('ticket_management.helpdesk_view'))

@app.route('/simpleuser')
def simple_user_redirect():
    return redirect(url_for('ticket_management.simple_user_view'))

if __name__ == '__main__':
    app.run(debug=True)