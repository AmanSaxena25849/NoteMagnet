from celery import shared_task
from django.core.mail import send_mail



@shared_task
def send_note_notification(title:str, message:str, users, author:str) -> str:
    
    success_count = 0
    failed = []
    
    for email in users:
        try:
            send_mail(
                subject = f"{title} by {author}.",
                message = message,
                from_email="no-reply@notemagnet.com",
                recipient_list=[email],
                fail_silently=True,
            )
            success_count += 1
        
        except Exception as e:
            failed.append((email, str(e)))
            continue
        
    return f"Notification sent to {success_count} users. Failed: {len(failed)}"