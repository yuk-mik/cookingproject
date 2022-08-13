from django.contrib import admin

#from cookingproject.cookrecord.models import RecordModel
from .models import RecordModel
from .models import Account

# Register your models here.

admin.site.register(RecordModel)
admin.site.register(Account)