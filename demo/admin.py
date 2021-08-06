from django.contrib import admin
from demo.models import Member, Person


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name',)


@admin.register(Person)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', )
    # list_display = ('name', 'phone', 'name_cipher', 'phone_cipher',)
