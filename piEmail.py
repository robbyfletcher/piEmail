import os
import smtplib
from email.mime.text import MIMEText
import datetime

# Change to your own account information
# Account Information
to = 'username@email.com' # Email to send to.
gmail_user = 'username@gmail.com' # Email to send from. (MUST BE GMAIL)
gmail_password = 'gmailpassword' # Gmail password.
smtpserver = smtplib.SMTP('smtp.gmail.com', 587) # Server to use.

smtpserver.ehlo()  # Says 'hello' to the server
smtpserver.starttls()  # Start TLS encryption
smtpserver.ehlo()
smtpserver.login(gmail_user, gmail_password)  # Log in to server
today = datetime.date.today()  # Get current time/date

ip = os.popen('hostname -I').read()

# Creates the text, subject, 'from', and 'to' of the message.
msg = MIMEText(ip)
msg['Subject'] = 'IPs For RaspberryPi on %s' % today.strftime('%b %d %Y')
msg['From'] = gmail_user
msg['To'] = to
# Sends the message
smtpserver.sendmail(gmail_user, [to], msg.as_string())
# Closes the smtp server.
smtpserver.quit()
