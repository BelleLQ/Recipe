from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact_us, name="contact_us"),
    # needs to be changed to path('blog/<int:blog_id>', views.blog_post, 'name=blog_post') after I have my blog_id
    path('blog', views.blog_post, name="blog_post"),
    # needs to be changed to path('blog/<int:recipe_id>', views.recipe_post, 'name=recipe_post') after I have my recipe
    # id
    path('recipe', views.recipe_post, name="recipe_post"),
    path('recipe/add', views.add_recipe, name="add_recipe"),
    path('recipes', views.recipe_post_list, name="recipe_post_list"),

]