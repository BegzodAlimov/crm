from django.db import models
from tools.models import BasedModel
from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.validators import FileExtensionValidator

image_validator = FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])

# Create your models here.
class User(BasedModel, AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ("parent", "Parent"),
    ]
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('archive', 'Archive'),
    ]
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    phone_number = models.CharField(max_length=30)
    email = models.EmailField(unique=False, null=True, blank=True)
    middle_name = models.CharField(max_length=120, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    avatar = models.ImageField(upload_to='avatars/', default='avatars/default.png', validators=[image_validator])
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')
    
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
