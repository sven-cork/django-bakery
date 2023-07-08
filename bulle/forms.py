from django.utils.text import slugify
from .models import Comment, Recipies
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecipieForm(forms.ModelForm):
    class Meta:
        model = Recipies
        fields = ('title', 'content', 'category')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title) 
        if commit:
            instance.save()
        return instance