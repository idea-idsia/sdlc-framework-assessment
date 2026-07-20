@app.route('/login')
def login():
    # Placeholder route for login functionality
    return "Login as helpdesk/user"


@app.route('/tickets', methods=['GET', 'POST'])
def tickets():
    if request.method == 'POST':
        description = request.form['description']
        category = request.form['category']  # Should be validated to one of the categories
        new_ticket = Ticket(description=description, category=category)
        db.session.add(new_ticket)
        db.session.commit()

    all_tickets = Ticket.query.all()
    return render_template('tickets.html', tickets=all_tickets)


@app.route('/ticket/<int:tid>', methods=['GET', 'POST'])
def ticket(tid):
    ticket = Ticket.query.get_or_404(tid)
    if request.method == 'POST':
        # Modify the ticket
        pass

    messages = Message.query.filter_by(ticket_id=tid).all()
    return render_template('ticket.html', ticket=ticket, messages=messages)


if __name__ == '__main__':
    app.run(debug=True)