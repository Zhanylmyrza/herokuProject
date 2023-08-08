from django.contrib import admin
from courseApp.models import Category, Branch, Contact, Course


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Contact)
admin.site.register(Branch)

