from flask import Flask, render_template, send_from_directory, request, redirect, url_for,flash
from form import MessageForm
from flask_bootstrap import Bootstrap5
import smtplib
import os

my_email = os.environ.get('EMAIL')
password = os.environ.get('EMAIL_PASSCODE')


app = Flask(__name__)  # name of current directory
app.config['SECRET_KEY'] = os.environ.get("FLASK_KEY")
Bootstrap5(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    message_form = MessageForm()
    if message_form.validate_on_submit():
        name = message_form.name.data
        email = message_form.email.data
        sub=message_form.subject.data
        message = message_form.message.data
        flash(message="Message Sent",category='success')
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="erprp99@gmail.com",
                                msg=f"Subject:{sub}\n\n{message}\n\nFrom:{name}\n{email}")
            connection.sendmail(from_addr=my_email,to_addrs=email,
                                msg=f"Subject:Message Received\n\n\nThanks for contacting me {name}. I'll reach out to you soon.\n\n\nSincerly,\n\nPrashanna Raj Pandit")
        return redirect(url_for('home'))
    return render_template("index.html", form=message_form)


@app.route('/skills')
def skills():
    return render_template("skills.html")


@app.route('/download')
def download():
    return send_from_directory('static', path='files/resume.pdf')

@app.route('/recent_works')
def all_recent_work():
    return render_template("recent_work.html")

if __name__ == "__main__":
    app.run(debug=True)
