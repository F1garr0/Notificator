from django.contrib import admin
from .models import User, UserTask, TaskConfig

# Register your models here.
admin.site.register(User)
admin.site.register(UserTask)
admin.site.register(TaskConfig)
