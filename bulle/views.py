from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect 
from .models import Recipies, Comment
from django.urls import reverse_lazy
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


class RecipieLike(View):

    def post(self, request, slug):
        recipie = get_object_or_404(Recipies, slug=slug)  
        if recipie.likes.filter(id=request.user.id).exists():
            recipie.likes.remove(request.user)
        else:
            recipie.likes.add(request.user)  
        
        return HttpResponseRedirect(reverse('recipies_content', args=[slug]))


class AddRecipie(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    model = Recipies
    template_name = 'addrecipie.html'
    success_url = reverse_lazy('home')
    form_class = RecipieForm

    def form_valid(self, form):
        if self.request.POST.get('status'):
            form.instance.status = int(self.request.POST.get('status'))
        form.instance.author = self.request.user

        messages.success(self.request, 'Recipe added successfully.')
        return super().form_valid(form)


class UpdateRecipie(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = Recipies
    form_class = RecipieForm
    template_name = 'updaterecipie.html'
    success_url = reverse_lazy('home')
    success_message = 'Your recepie was successfully updated!'


def delete_recipie(request, recipie_id):
    recipie = get_object_or_404(Recipies, id=recipie_id)
    if recipie.author == request.user:    
        recipie.delete()
        messages.success(request, "Recipie successfully deleted.")
    else:
        messages.error(request, "Unable to delete recipie.")
    return redirect('/')