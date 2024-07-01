import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def mail(toaddr,body):

    fromaddr = "arunraj0861@gmail.com"
    # toaddr = "cyberprismsoftwarelimited@gmail.com"

    # instance of MIMEMultipart
    msg = MIMEMultipart()
    toaddr = "arunraj0861@gmail.com"
    # storing the senders email address
    msg['From'] = fromaddr

    # storing the receivers email address
    msg['To'] = toaddr

    # storing the subject
    msg['Subject'] = "Hostel Attendance Report"
    # msg['Subject'] = subject

    # string to store the body of the mail


    # attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))



    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()


    # Authentication
    s.login(fromaddr, "esperenza")

    # Converts the Multipart msg into a string
    text = msg.as_string()

    # sending the mail
    s.sendmail(fromaddr, toaddr, text)

    # terminating the session
    s.quit()
