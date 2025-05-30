from celery import shared_task
from django.core.mail import send_mail



@shared_task
def send_note_notification(title:str, message:str, emails, author:str) -> str:
    """send notification to all followers upon creation of new note by author.

    Args:
        title (str): title of the note.
        message (str): content of the note.
        emails (_type_): list of user emails.
        author (str): name of the author.

    Returns:
        str: number of successfull email sent and failed attampts.
    """
    
    success_count = 0
    failed = []
    
    for email in emails:
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