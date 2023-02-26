from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .models import Recipe
from django.shortcuts import render, redirect
from .forms import RecipeForm
from django.conf import settings


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})


def about(request):
    return render(request, 'about_us.html')


def contact_us(request):
    return render(request, 'contact_us.html')


def blog_post(request):
    return render(request, 'blog_post.html')


def recipe_post(request):
    return render(request, 'recipe_post.html')


def recipe_post_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipe_post_list.html', {'recipes': recipes})


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.created_by = request.user
            recipe.save()
            return render(request, 'recipe_post_list.html')
    else:
        form = RecipeForm()
    return render(request, 'add_recipe.html', {'form': form})


class RecipeView(LoginRequiredMixin, CreateView):
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

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def save(self, *args, **kwargs):
        self.instance.created_by =  self.request.user
        return super().save(*args, **kwargs)