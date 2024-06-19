from django.contrib import admin
from main.models import Contact, Flan
# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    pass

class FlanAdmin(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactAdmin)
admin.site.register(Flan, FlanAdmin)