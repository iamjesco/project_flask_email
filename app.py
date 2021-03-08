from flask import Flask, render_template, redirect, url_for, request, flash
from forms import ContactForm
from flask_mail import Mail, Message
from config import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'awehaweh24345tqwgqwg'
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = mail_username
app.config['MAIL_PASSWORD'] = mail_password

mail = Mail(app)


@app.route('/')
def home():
	return render_template('home.html')


@app.route('/about')
def about():
	return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		name = request.form.get('name'),
		email = request.form.get('email'),
		inquiry = request.form.get('inquiry')
		msg = Message(
			subject=f'Mail from {name}',
			body=f'E-mail: {email}\nMessage: {inquiry}',
			sender=mail_username,
			recipients=['jurgen.schoobaar@hotmail.com'])
		mail.send(msg)
		flash('Inquiry sent successfully!', 'success')
		return redirect(url_for('contact'))

	return render_template('contact.html', form=form)


if __name__ == '__main__':
	app.run(debug=True)
