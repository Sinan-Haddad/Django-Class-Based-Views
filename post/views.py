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
    model = post ## in template [object_list,post_list]
    # context_object_name='all_posts'
    ordering =['-created_at']
    # queryset=post.objects.filter(active=True)
    # template_name='post/test.html'
    def get_queryset(self):
        return post.objects.filter(active=True)
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['myname']='sinan haddad'
        return context

class PostDetail(DetailView):
    model = post



class PostCreate(CreateView):
    pass


class PostDelete(DeleteView):
    pass


class PostUpdate(UpdateView):
    pass
