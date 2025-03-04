from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from users.models import User, Admin, Moderator, Teacher, Student, Parent

def delete_existing_profiles(user):
    Admin.objects.filter(user=user).delete()
    Moderator.objects.filter(user=user).delete()
    Teacher.objects.filter(user=user).delete()
    Student.objects.filter(user=user).delete()
    Parent.objects.filter(user=user).delete()

@receiver(pre_save, sender=User)
def before_update_or_create_related_profile(sender, instance, **kwargs):
    if instance.pk:
        instance._old_data = User.objects.get(pk=instance.pk)

@receiver(post_save, sender=User)
def update_or_create_related_profile(sender, instance, created, **kwargs):
    get_old_user = getattr(instance, '_old_data', None)
    if not created and get_old_user.role != instance.role:
        delete_existing_profiles(instance)

    role_map = { 'admin': Admin, 'moderator': Moderator, 'teacher': Teacher, 'student': Student, 'parent': Parent}

    ProfileModel = role_map.get(instance.role)
    if ProfileModel:
        ProfileModel.objects.update_or_create(user=instance)