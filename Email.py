import os
from email.message import EmailMessage
import ssl
import smtplib

def mail(rec_mail,sub,content):
    try:
        sender_email = "techub1802@gmail.com"
        receiver_email = rec_mail
        password = os.environ.get('PASSWORD')


        subject=sub
        body=content

        em=EmailMessage()
        em['From']=sender_email
        em['to']=receiver_email
        em['Subject']=subject
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            smtp.login(sender_email,password)
            smtp.sendmail(sender_email,receiver_email,em.as_string())

    except Exception as e:
        return "Mail not Delivered"


