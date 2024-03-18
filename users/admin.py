from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class UserAdmin(UserAdmin):
    model = User
    list_display = ['id', 'email', 'username', 'is_active', 'is_staff']
    list_filter = ['id', 'email', 'username', 'is_active', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        # ... Diğer özelleştirmeleri burada ekleyebilirsiniz ...
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id','email', 'password1', 'password2', 'is_active', 'is_staff')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']

admin.site.register(User, UserAdmin)