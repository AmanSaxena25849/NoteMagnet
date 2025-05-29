from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def send_notification(subject:str, message:str) -> str:
    
    users = User.objects.filter(notifications = True)
    print("start sending mails.")
    
    
    for user in users:
        print(f"sent to {user.first_name} ")
        send_mail(
            subject = subject,
            message = message,
            from_email="no-reply@notemagnet.com",
            recipient_list=[user.email],
            fail_silently=True,
        )
        
    return f"Notification sent to {users.count()} users."

