from django import forms
from blogs.models import Category,Blogs
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Creating a CategoryForm To get the Category form for Category urls in dashboard app
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

# Creating PostForm to get posts for Posts urls in dashboard app
class PostForm(forms.ModelForm):
    class Meta:
        model=Blogs
        fields=('title','category','blog_image','pdf_file','short_description','blog_body','status','is_featured')

# Creating UserFrom to get users to show from dashboard app
class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')

class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')


