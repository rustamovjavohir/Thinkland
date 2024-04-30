from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AbstractUserAdmin
from apps.auth_user.models import User, Authors


@admin.register(User)
class UserAdmin(AbstractUserAdmin):
    list_display = ('id', 'username', 'full_name', 'is_active', 'is_staff', 'is_superuser')
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    ordering = ('-is_staff', '-is_superuser', '-is_active')
    fieldsets = (
        ('Персональная информация', {'fields': ('first_name', 'last_name', 'profile_photo')}),
        (None, {'fields': ('username', 'password')}),
        ('Разрешения', {'fields': ('groups', 'user_permissions')}),
        ('Роль пользователя', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Информация о дате', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'phone', 'password1', 'password2')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Groups', {'fields': ('groups',)}),

    )
    readonly_fields = ('full_name', 'last_login', 'date_joined')


@admin.register(Authors)
class AuthorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    ordering = ('name',)
    fieldsets = (
        ('Информация об авторе', {'fields': ('name',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('name',)}),
    )
