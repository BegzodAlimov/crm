from django.db.models.signals import post_save
from django.dispatch import receiver

from users.models import User, Admin, Moderator, Teacher, Student, Parent


def delete_existing_profiles(user):
    Admin.objects.filter(user=user).delete()
    Moderator.objects.filter(user=user).delete()
    Teacher.objects.filter(user=user).delete()
    Student.objects.filter(user=user).delete()
    Parent.objects.filter(user=user).delete()


@receiver(post_save, sender=User)
def update_or_create_related_profile( instance, created, **kwargs):
    if not created:
        delete_existing_profiles(instance)

    if instance.status == 'admin':
        Admin.objects.update_or_create(user=instance)
    elif instance.status == 'moderator':
        Moderator.objects.update_or_create(user=instance)
    elif instance.status == 'teacher':
        Teacher.objects.update_or_create(user=instance)
    elif instance.status == 'student':
        Student.objects.update_or_create(user=instance)
    elif instance.status == 'parent':
        Parent.objects.update_or_create(user=instance)