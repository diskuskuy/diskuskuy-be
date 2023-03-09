from django.contrib import admin
from .models import *

admin.site.register(InitialPost)
admin.site.register(ReplyPost)
admin.site.register(NestedReplyPost)