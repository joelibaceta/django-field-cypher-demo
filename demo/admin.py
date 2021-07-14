from django.contrib import admin
from demo.models import Member


# Register your models here.
@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name',)
    # list_filter = ('first_name', 'last_name',)

# admin.site.register(Member, MemberAdmin)
