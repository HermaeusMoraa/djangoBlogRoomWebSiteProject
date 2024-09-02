from django.contrib import admin

from thread_app.models import CategoryModel, ThreadModel

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(ThreadModel)

# admin.site.register(TagModel)