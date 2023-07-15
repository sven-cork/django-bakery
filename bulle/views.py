from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect 
from .models import Recipies, Comment
from django.urls import reverse_lazy, reverse
from .forms import CommentForm, RecipieForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView


class RecipieList(generic.ListView):
    model = Recipies
    queryset = Recipies.objects.filter(status=1).order_by('-created_on')
    template_name = "index.html"
    paginate_by = 9

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bake_category_cover'] = Recipies.bake_category_cover
        return context

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            queryset = self.queryset.filter(category=category)
        else:
            queryset = self.queryset
        return queryset


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
                "comment_form": CommentForm(),
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

def recipie_like(request, slug):
    recipie = get_object_or_404(Recipies, slug=slug)  
    if recipie.likes.filter(id=request.user.id).exists():
        recipie.likes.remove(request.user)
    else:
        recipie.likes.add(request.user)  
    
    return HttpResponseRedirect(reverse('recipies_content', args=[slug]))


def add_recipie(request):
    if request.method == 'POST':
        form = RecipieForm(request.POST)
        if form.is_valid():
            recipie = form.save(commit=False)
            if request.POST.get('status'):
                recipie.status = int(request.POST.get('status'))
            recipie.author = request.user
            recipie.save()
            messages.success(request, 'Recipe added successfully.')
            return redirect('home')
    else:
        form = RecipieForm()
    return render(request, 'addrecipie.html', {'form': form})


def update_recipie(request, slug):
    recipie = get_object_or_404(Recipies, slug=slug)
    form = RecipieForm(request.POST or None, instance=recipie)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'updaterecipie.html', {'form': form, 'recipie': recipie})


def delete_recipie(request, recipie_id):
    recipie = get_object_or_404(Recipies, id=recipie_id)
    if recipie.author == request.user:    
        recipie.delete()
        messages.success(request, "Recipie successfully deleted.")
    else:
        messages.error(request, "Unable to delete recipie.")
    return redirect('/')


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.success(request, "Comment successfully deleted.")
    else:
        messages.error(request, "Unable to delete comment.")

    return redirect('recipies_content', slug=comment.recipie.slug)
