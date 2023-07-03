from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipies
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
                "liked": liked,
                "comment_form": CommentForm()
            },
            
        )