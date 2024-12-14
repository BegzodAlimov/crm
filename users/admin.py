from django.contrib import admin

from users.models import User, Moderator, Teacher, Parent, Student, Admin

# Register your models here.

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Moderator)
admin.site.register(Teacher)
admin.site.register(Parent)
admin.site.register(Student)
