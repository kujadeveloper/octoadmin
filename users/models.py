from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    class Meta:
        ordering = ['id']
        db_table = 'users'

    user = models.ForeignKey('user', on_delete=models.CASCADE, blank=True, null=True, related_name='user_user')
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    confirm_code = models.CharField(max_length=6, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    anonym = models.UUIDField(default=uuid.uuid4, editable=False)
    confirm_token = models.CharField(max_length=500, blank=True,null=True)

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone']

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def undelete(self, *args, **kwargs):
        self.is_deleted = False
        self.save()
