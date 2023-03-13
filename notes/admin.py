from django.contrib import admin
from notes.models import Userinfo
from notes.models import Document

# Register your models here.
admin.site.register(Userinfo)
admin.site.register(Document)