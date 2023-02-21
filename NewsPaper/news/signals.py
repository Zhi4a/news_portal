from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import PostCategory, SubscribersCategory


@receiver(post_save, sender=PostCategory)
def notify_subscribers(sender, instance, created, **kwargs):
    subject = f'''Новая статья: "{instance.post.title}" в категории {instance.category.category}'''
    subs = list(SubscribersCategory.objects.filter(category=instance.category).values('subscribers__email'))
    for sub in subs:
        send_mail(
            subject=subject,
            message=instance.text[:50],
            recipient_list=[sub],
        )
