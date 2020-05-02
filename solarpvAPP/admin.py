# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(Certificate)
admin.site.register(Service)
admin.site.register(Registered_Company)
admin.site.register(Registered_User)
