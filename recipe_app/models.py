from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.


class RecipeDifficultyLevel(models.Model):
    difficulty_id = models.AutoField(primary_key=True)
    difficulty_title = models.CharField(max_length=100)

    def __str__(self):
        return self.difficulty_title


class RecipeCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_title = models.CharField(max_length=100)

    def __str__(self):
        return self.category_title


class RecipeDietStyle(models.Model):
    diet_style_id = models.AutoField(primary_key=True)
    diet_style_title = models.CharField(max_length=100)

    def __str__(self):
        return self.diet_style_title


class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=255)
    recipe_img_url = models.CharField(max_length=255, blank=True, null=True)
    prep_time_minute = models.IntegerField(blank=True, null=True)
    cook_time_minute = models.IntegerField(blank=True, null=True)
    yield_servings = models.FloatField(blank=True, null=True)
    rating = models.IntegerField(default=0, blank=True, null=True)
    difficulty_id = models.ForeignKey(RecipeDifficultyLevel, on_delete=models.CASCADE)
    diet_style_id = models.ForeignKey(RecipeDietStyle, on_delete=models.CASCADE, blank=True, null=True)
    category_id = models.ForeignKey(RecipeCategory, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.recipe_name

    @property
    def rating_range(self):
        return range(self.rating)

    @property
    def empty_rating_range(self):
        empty_count = 5 - self.rating
        return range(empty_count)


class RecipeInstruction(models.Model):
    instruction_id = models.AutoField(primary_key=True)
    instruction_title = models.CharField(max_length=255, default=" ")
    instruction_text = models.CharField(max_length=1000, blank=True, null=True)
    instruction_img_url = models.CharField(max_length=255, blank=True, null=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class RecipeComments(models.Model):
    comment_id = models.AutoField(primary_key=True)
    comment_title = models.CharField(max_length=255, default=" ")
    comment_text = models.CharField(max_length=1000, blank=True, null=True)
    comment_img_url = models.CharField(max_length=255, blank=True, null=True)
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.TimeField(default=timezone.now)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
