from django.shortcuts import render
from .models import Blog_Project
def all_blogs(request):
    blogs = Blog_Project.objects.order_by('-date')[:5]
    return render(request, 'blog/all_blogs.html', {'blogs':blogs})
# Create your views here.
