from django.shortcuts import render
from .models import post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView,CreateView


# Create your views here.
# def post_list(request):
#     post_list=post.objects.all()
#     return render(request,'post/list.html',{"post_list":post_list})
# def post_detail(request,id):
#     pass
class PostList(ListView):
    model = post


class PostDetail(DetailView):
    model = post



class PostCreate(CreateView):
    pass


class PostDelete(DeleteView):
    pass


class PostUpdate(UpdateView):
    pass
