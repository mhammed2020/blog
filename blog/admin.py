from django.contrib import admin
from .models import Post
admin.site.site_header = "Centre National de previsions"
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'author', 'publish', 'status')
  list_filter = ('status', 'created', 'publish', 'author')
  search_fields = ('title', 'body')
  prepopulated_fields = {'slug': ('title',)}
  raw_id_fields = ('author',)
  date_hierarchy = 'publish'
  ordering = ('status', 'publish')


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#  list_display = ('title', 'slug', 'author', 'publish', 'status')

# class PostAdmin(admin.ModelAdmin):
#     list_filter = ['status','created']
#     list_display = ['title','created','status']
#     search_fields = ['title','body']
# admin.site.register(Post,PostAdmin)

