from django.contrib import admin
from accounts.models import *

# Register your models here.
admin.site.site_header="Oyo Clone"
admin.site.site_title="Oyo Clone"
admin.site.site_url="Oyo Clone"
admin.site.register(HotelUser)