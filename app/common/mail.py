import logging

from smtplib import SMTPException
from threading import Thread

from flask import current_app
<<<<<<< HEAD
from extensions import mail
from flask_mail import Message



logger = logging.getLogger(__name__)


def _send_async_email(app, msg):
=======
from flask_mail import Message  # type: ignore

from extensions import mail

logger = logging.getLogger(__name__)

def _send_async_email(app, msg):

>>>>>>> 2fead90dc98d77b57613f64763ea4f4ad1a28b6e
    with app.app_context():
        try:
            mail.send(msg)
        except SMTPException:
<<<<<<< HEAD
            logger.exception("Ocurrió un error al enviar el email")


def send_email(subject, sender, recipients, text_body,
               cc=None, bcc=None, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc, bcc=bcc)
    msg.body = text_body
    if html_body:
        msg.html = html_body
    Thread(target=_send_async_email, args=(current_app._get_current_object(), msg)).start()


# https://chatgpt.com/share/684981ee-402c-800d-b6b1-98b8e7569d51
=======
            logger.exception("Occured a mistake to send the email")
            
def send_email(subject, sender,recipients, text_body, cc=None, bcc=None, html_body=None):
    msg = Message(subject, sender=sender, recipients=recipients, cc=cc, bcc=bcc)
    msg.body=text_body
    if html_body:
        msg.html = html_body
    Thread(target=_send_async_email, args=(current_app._get_current_object(),msg)).start()
>>>>>>> 2fead90dc98d77b57613f64763ea4f4ad1a28b6e
