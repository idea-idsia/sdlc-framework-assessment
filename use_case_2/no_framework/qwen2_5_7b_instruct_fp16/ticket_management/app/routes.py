from flask import render_template, request, redirect, url_for, flash
from app import db, login_manager
from app.models import User, Ticket
from app.forms import LoginForm, TicketForm, MessageForm
from flask_login import login_user, logout_user, current_user


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('ticket_management'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('ticket_management'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@bp.route('/')
def ticket_management():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    tickets = Ticket.query.filter_by(user=current_user).all()

    open_tickets = [ticket for ticket in tickets if ticket.status == 'open']
    active_tickets = [ticket for ticket in tickets if ticket.status == 'active']

    return render_template('ticket_management.html', open_tickets=open_tickets, active_tickets=active_tickets)


@bp.route('/new_ticket', methods=['GET', 'POST'])
def new_ticket():
    form = TicketForm()

    if form.validate_on_submit():
        new_ticket = Ticket(
            user=current_user,
            category=form.category.data,
            description=form.description.data
        )
        db.session.add(new_ticket)
        db.session.commit()

        flash('Ticket created successfully', 'success')
        return redirect(url_for('ticket_management'))

    return render_template('new_ticket.html', form=form)


@bp.route('/edit_ticket/<int:ticket_id>', methods=['GET', 'POST'])
def edit_ticket(ticket_id):
    ticket = Ticket.query.get_or_404(ticket_id)

    if request.method == 'POST':
        ticket.category = request.form['category']
        ticket.description = request.form['description']
        db.session.commit()

        flash('Ticket updated successfully', 'success')
        return redirect(url_for('ticket_management'))

    form = TicketForm(
        category=ticket.category,
        description=ticket.description
    )

    return render_template('edit_ticket.html', form=form, ticket=ticket)