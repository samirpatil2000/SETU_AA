from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


class AccountAdmin(UserAdmin):

	list_display = ('email','date_joined', 'last_login', 'is_admin','is_staff')

	search_fields = ('email', )
	ordering = ('email',)

	readonly_fields=('date_joined', 'last_login')  #the fields that can't be change

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()
	add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )


# Register your models here.


admin.site.register(Account, AccountAdmin)


from django.contrib.auth.models import Group

admin.site.unregister(Group)