from django.contrib.auth.models import AbstractUser
from django.db import models

from tools.models import BasedModel
from rest_framework_simplejwt.tokens import RefreshToken



# Create your models here.
class User(BasedModel, AbstractUser):
    STATUS_CHOICES = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ("parent", "Parent"),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True, blank=True, default='male')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png')
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def token(self):
        token = RefreshToken.for_user(self)
        return {
            "access_token": str(token.access_token),
            'refresh_token': str(token),
        }
    
    def hashing_password(self):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)

    def save(self, *args, **kwargs):
        self.hashing_password()
        super(User, self).save(*args, **kwargs)


class Admin(BasedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admins')
    def __str__(self):
        return self.user.get_full_name

class Moderator(BasedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='moderators')
    def __str__(self):
        return self.user.get_full_name

class Teacher(BasedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teachers')
    def __str__(self):
        return self.user.get_full_name

class Parent(BasedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='parents')
    children = models.ManyToManyField('Student', related_name='children', null=True, blank=True)
    def __str__(self):
        return self.user.get_full_name

class Student(BasedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='students')
    def __str__(self):
        return self.user.get_full_name