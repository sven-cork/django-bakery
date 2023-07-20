from django.utils.text import slugify
from .models import Comment, Recipies
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class RecipieForm(forms.ModelForm):
    default_image_url = 'https://res.cloudinary.com/dwxoyt0qz/image/upload/v1688292295/pexels-antonio-quagliata-227432_nwslyq.jpg'

    category = forms.ChoiceField(choices=Recipies.bake_category, required=False)
    allergy = forms.ChoiceField(choices=Recipies.allergy_category.items(), required=False)

    class Meta:
        model = Recipies
        fields = ('title', 'content', 'category', 'allergy')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)

        category = self.cleaned_data.get('category')
        if category:
            instance.featured_image = Recipies.bake_category_cover.get(category, self.default_image_url)
        else:
            instance.featured_image = self.fields['category_image'].initial

        if commit:
            instance.save()
        return instance
