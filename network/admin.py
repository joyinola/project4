from django.contrib import admin

# Register your models here.
from .models import User,Posts,Follows,Like
admin.site.register(User)
admin.site.register(Posts)
admin.site.register(Like)
admin.site.register(Follows)