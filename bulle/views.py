from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect 
from .models import Recipies, Comment
from .forms import CommentForm


class RecipieList(generic.ListView):
    model = Recipies
    queryset = Recipies.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 9


class RecipieDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipies.objects.filter(status=1)
        recipie = get_object_or_404(queryset, slug=slug)
        comments = recipie.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipie.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipie_content.html",
            {
                "recipie": recipie,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
            
        )
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Recipies.objects.filter(status=1)
        recipie = get_object_or_404(queryset, slug=slug)
        comments = recipie.comments.filter(approved=True).order_by('created_on')
        liked = False
        if recipie.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        comment_form = CommentForm(data=request.POST)
        print(" comment from ", comment_form)

        if comment_form.is_valid():
            print(" in is valid")
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.author = request.user
            comment = comment_form.save(commit=False)
            comment.recipie = recipie
            print("comment recipe is ", comment)
            comment.save()
        else:
            comment_form = CommentForm()


        return render(
            request,
            "recipie_content.html",
            {
                "recipie": recipie,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },          
        )

class RecipieLike(View):

    def post(self, request, slug):
        recipie = get_object_or_404(Recipies, slug=slug)  
        if recipie.likes.filter(id=request.user.id).exists():
            recipie.likes.remove(request.user)
        else:
            recipie.likes.add(request.user)  
        
        return HttpResponseRedirect(reverse('recipies_content', args=[slug]))