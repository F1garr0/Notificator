from django.db import models
from django.core.validators import validate_email

# Create your models here.

class User(models.Model):
    """docstring for AnkeyUser."""
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=128, validators=[validate_email])
    phone = models.CharField(max_length=128)
    
    class Meta:
        db_table = "users"


class UserTask(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING) 
    task_name = models.CharField(max_length=128)

    class Meta:
        db_table = "user_task"


class TaskConfig(models.Model):
    id = models.AutoField(primary_key=True)
    task_id = models.ForeignKey(UserTask, on_delete=models.DO_NOTHING)
    args = models.CharField(max_length=128, null=True)

    class Meta:
        db_table = "task_config"
