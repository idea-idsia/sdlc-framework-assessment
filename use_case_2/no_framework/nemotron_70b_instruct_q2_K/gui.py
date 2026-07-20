from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_type = request.form['user_type']
        # Dummy check for demo purposes only
        if user_type == 'helpdesk' or user_type == 'simple_user':
            return render_template('ticket_management.html')
    return render_template('login.html')

if __name__ == '__main__':
    app.run()