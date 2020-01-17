from django.contrib import admin
from .models import Meeting,Meetingminutes,Resource,Event

# Register your models here.
admin.site.register(Meeting)
admin.site.register(Meetingminutes)
admin.site.register(Resource)
admin.site.register(Event)
