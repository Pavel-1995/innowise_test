from django.core.mail import send_mail

from innowise.celery import app


@app.task
def send_email():
    """Send email about changes status"""
    send_mail(
        "status",
        "Status your ticket changed",
        "EMAIL_HOST_USER",
        [
            "EMAIL_RECIPIENT",
        ],
        fail_silently=False,
    )
