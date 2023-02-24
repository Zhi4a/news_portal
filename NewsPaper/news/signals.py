from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post, SubscribersCategory, User


@receiver(post_save, sender=Post)
def notify_subscribers(sender, instance, created, **kwargs):
    subject = f'''Новый пост: "{instance.title}" в категории {instance.category}'''
    if created:
        subs = list(SubscribersCategory.objects.filter(category=instance.category).values('subscribers'))
        emails = []
        for sub in subs:
            emails.append(User.objects.filter(id=sub.id).values('email'))
        for email in emails:
            send_mail(
                subject=subject,
                message=instance.text[:50],
                recipient_list=[email],
            )
        print(f'''Новый пост: "{instance.post.title}" в категории {instance.category.category}''')
