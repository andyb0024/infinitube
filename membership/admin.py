from django.contrib import admin
from .models import UserMembership,Membership,Subscription
# Register your models here.
admin.site.register(Membership)
admin.site.register(Subscription)
admin.site.register(UserMembership)