from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    pass


@admin.register(RecipeCategory)
class RecipeCategoryAdmin(admin.ModelAdmin):
    # list_display = ('difficulty_id', 'difficulty_title',)
    pass

@admin.register(RecipeDifficultyLevel)
class RecipeDifficultyLevelAdmin(admin.ModelAdmin):
    list_display = ('difficulty_id', 'difficulty_title',)


@admin.register(RecipeDietStyle)
class RecipeDietStyleAdmin(admin.ModelAdmin):
    list_display = ('diet_style_id', 'diet_style_title',)
