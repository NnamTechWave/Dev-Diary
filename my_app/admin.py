from django.contrib import admin
from .models import blog

# Register your models here.

class blogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(blog)
# admin.site.register(Category)