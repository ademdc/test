from django.contrib import admin
from .models import todo, users,emails_sub,contact_page_model

admin.site.register(todo)
admin.site.register(users)
admin.site.register(emails_sub)
admin.site.register(contact_page_model)