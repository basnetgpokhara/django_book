from django.shortcuts import render,redirect
from blogs.models import Category,Blogs
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm,PostForm
from django.shortcuts import get_object_or_404
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import AddUserForm,EditUserForm
# Create your views here.

#  To show the dashboard for authenticate users
@login_required(login_url='login')
def dashboard(request):
    category_counts = Category.objects.all().count()
    blogs_counts = Blogs.objects.all().count()
    context = {
        'category_counts': category_counts,
        'blogs_counts': blogs_counts
    }
    return render(request, "dashboard/dashboard.html",context)

# To display categories in dashboard url
def categories(request):
    return render(request, 'dashboard/categories.html')

# To add new categories from dashboard
def add_categories(request):
    if request.method=="POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Added Successfully.")    
            return redirect('categories') 
    form = CategoryForm()
    context = {
        'form': form,
       
       
    }
    return render(request, 'dashboard/add_categories.html',context)

# To edit/modify categories from dashboard
def edit_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method=="POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save() 
            messages.success(request, "Category Updated Successfully.")   
            return redirect('categories') 

    form= CategoryForm(instance=category)
    context = {
        'form': form,
        'category': category
        
    }
    return render(request,"dashboard/edit_categories.html",context)

# Creating delete_categories function to delete the category from dashboard.
def delete_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Category Deleted Successfully.")
    return redirect ('categories')
    #return render(request,'dashboard/delete_category.html')

# posts function to display the posts in dashboard
def posts(request):
    posts = Blogs.objects.all()
    context = {
        'posts': posts
    }
    return render(request,'dashboard/posts.html', context)

# add_posts function to add new post from dashboard
def add_posts(request):
  
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()   
            title = form.cleaned_data['title']# to obtailed the title from blogs model
            post.slug = slugify(title)# to create a slug based on title
            post.save()
            messages.success(request, "Books Added Successfully.")
            return redirect('posts') 
    form= PostForm()
    context = {
        'form': form
    }
    return render(request,'dashboard/add_posts.html',context)

# To edit/modify posts from dashboard
def edit_posts(request,pk):
    posts = get_object_or_404(Blogs, pk=pk)
    if request.method=="POST":
        form = PostForm(request.POST, request.FILES, instance=posts)
        if form.is_valid():
            post = form.save(commit=False) 
            post.author = request.user
            post.save()   
            title = form.cleaned_data['title']# to obtailed the title from blogs model
            post.slug = slugify(title)# to create a slug based on title
            post.save()
            messages.success(request, "Books Updated Successfully.")
            return redirect('posts') 
    form= PostForm(instance=posts)
    context = {
        'form': form,
        'post': posts
    }
    return render(request,'dashboard/edit_posts.html',context)


# delete_posts function to delete post from dashboard
def delete_posts(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    messages.success(request, "Books Deleted Successfully.")
    return redirect('posts')


# users urls
# users function to display users from dashboard
def users(request):
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'dashboard/users.html',context)

# add users function  from dashboard
def add_users(request):
    if request.method=="POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User Added Successfully.")    
            return redirect('users') 
    form = AddUserForm()
    context = {
        'form': form
    }
    return render(request, 'dashboard/add_users.html',context)

# edit_users function  from dashboard to edit the users
def edit_users(request,pk):
    user = get_object_or_404(User, pk=pk)
    if request.method=="POST":
        form = EditUserForm(request.POST, instance=user) # this form will not show password
        # form = AddUserForm(request.POST, instance=user) # this form will show password
        if form.is_valid():
            form.save() 
            messages.success(request, "User Updated Successfully.")   
            return redirect('users')
    form= EditUserForm(instance=user)# this form will not show password
    # form= AddUserForm(instance=user) this form will show password
    context = {
                'form': form,
                'user': user
                } 

    return render(request,'dashboard/edit_users.html',context)

# delete_users function to delete the users from dashboard
def delete_users(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request, "User Deleted Successfully.")  
    return redirect('users')