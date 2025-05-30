from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
import logging

User = get_user_model()

@shared_task
def send_notification(subject:str, message:str) -> str:
    """sends notification to add users with notifications on.

    Args:
        subject (str): subject of the mail
        message (str): message for the mail.

    Returns:
        str: count of user mail is sent to and failed mails..
    """
    
    users = User.objects.filter(notifications = True)
    logger = logging.getLogger(__name__)
    
    success_count = 0
    failed = []
    
    for user in users:
        logger.info(f"[Celery] Sending to: {user.email}")
        try:
            send_mail(
                subject = subject,
                message = message,
                from_email="no-reply@notemagnet.com",
                recipient_list=[user.email],
                fail_silently=True,
            )
            success_count += 1
        except Exception as e:
            failed.append((user.username, str(e)))
            continue
        
    return f"Notification sent to {success_count} users. Failed: {len(failed)}"

