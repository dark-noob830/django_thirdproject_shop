from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import Group
from .models import User , OtpCode


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number','code','created_at']


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'phone_number', 'is_admin']
    list_filter = ['is_admin']
    fieldsets = (
        (None,{'fields':['email','phone_number','full_name','password']}),
        ('Permissions',{'fields':['is_active','is_admin','last_login']}),
    )

    add_fieldsets = (
        (None, {'fields': ('email','phone_number','full_name','password1','password2')}),
    )
    search_fields = ["email",'full_name']
    ordering = ['full_name']
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
# Register your models here.
