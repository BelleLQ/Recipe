from django import forms
from .models import Recipe
from django.utils.translation import gettext_lazy as _


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['recipe_name',
                  'prep_time_minute',
                  'cook_time_minute',
                  'yield_servings',
                  'recipe_img_url',
                  'rating',
                  'difficulty_id',
                  'diet_style_id',
                  'category_id']
        labels = {
            'difficulty_id': _('difficulty'),
            'diet_style_id': _('diet style'),
            'category_id': _('category'),
        }
