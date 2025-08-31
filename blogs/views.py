from django.shortcuts import render,HttpResponse, redirect
from blogs.models import Blogs, Category,Comment
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import HttpResponseRedirect

# Create your views here.
def posts_by_category(request,category_id):
    # Fetch the post belongs to category according the the category id
    posts = Blogs.objects.filter(status='published', category=category_id)
    # user this method when you want to perform some custom action when category is not present
    try:
       category =Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    # use this method when you want to show 404 error message if category is not present
    # category = get_object_or_404(Category, pk=category_id)
    #print (posts)
    context = {
        'posts': posts,
        'category': category
    }
    return render(request, 'posts_by_category.html',context)

#blogs
def blogs(request,slug):
    single_post = get_object_or_404(Blogs, slug=slug, status ='published')
    # getting comment for blogs.html file
    if request.method == "POST":
        form_comment = Comment()
        form_comment.user = request.user
        form_comment.blog = single_post
        form_comment.comment= request.POST['comment']
        form_comment.save()
        return HttpResponseRedirect(request.path_info)

    # comment get
    comments = Comment.objects.filter(blog = single_post)
    comment_count = comments.count()
    # print(comments)
    context = {
        'single_post':single_post,
        'comments' : comments,
        'comment_count': comment_count
    }

    return render(request,'blogs.html',context)

# Blog Search function
def search(request):
    # get_keyword is the variable to store the keyword the word by which we are searching
    # keyword is the name of input text box in the form inside search.html page
    get_keyword = request.GET.get("keyword")
    #print (get_keyword)
    blogs = Blogs.objects.filter(Q(title__icontains =get_keyword) | Q(short_description__icontains =get_keyword) | Q(blog_body__icontains =get_keyword) , status='published')
    category = Category.objects.all()
   # print (blog)
    context = {
       'blogs': blogs,
       'get_keyword': get_keyword,
       'category': category 
    }
    return render(request,'search.html',context)