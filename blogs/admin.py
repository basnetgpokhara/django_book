from django.contrib import admin
from .models import Category, Blogs,Comment

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('id','category_name','created_at','updated_at')
   list_display_links =('category_name',)
admin.site.register(Category,CategoryAdmin)

class BlogAdmin(admin.ModelAdmin):
    # to display the given fields in list view in admin
    list_display = ('id','title','slug','category','author','blog_image','pdf_file','status','is_featured')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'category__category_name', 'author__username')
    list_editable = ('status','is_featured')
    list_display_links =('category','title','slug')
admin.site.register(Blogs,BlogAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display =('user','blog','comment','created_at','updated_at')
    list_display_links =('user','blog')
    

admin.site.register(Comment,CommentAdmin)