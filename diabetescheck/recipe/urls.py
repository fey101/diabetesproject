from django.conf.urls import url

from .views import (
    RecipeListView,
    RecipeDetailView,
    IngredientsListView,
    IngredientDetailView,
    RecipeIngredientListView,
    RecipeIngredientDetailView,
    NutrientsListView,
    NutrientDetailView,
    RecipeNutrientListView,
    RecipeNutrientDetailView,
)


urlpatterns = [
    url(r'^recipe_ingredients/', RecipeIngredientListView.as_view(),
        name='recipe_ingredients_list'),
    url(r'^recipe_ingredients/(?P<pk>[0-9]+)$',
        RecipeIngredientDetailView.as_view(),
        name='recipe_ingredient_detail'),

    url(r'^recipes/', RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipes/(?P<pk>[0-9]+)$',
        RecipeDetailView.as_view(), name='recipe_detail'),

    url(r'^ingredients/',
        IngredientsListView.as_view(), name='ingredients_list'),
    url(r'^ingredient/(?P<pk>[0-9]+)$',
        IngredientDetailView.as_view(), name='ingredient_detail'),

    url(r'^nutrients/',
        NutrientsListView.as_view(), name='nutrients_list'),
    url(r'^nutrient/(?P<pk>[0-9]+)$',
        NutrientDetailView.as_view(), name='nutrient_detail'),

    url(r'^recipe_nutrients/',
        RecipeNutrientListView.as_view(), name='recipe_nutrients_list'),
    url(r'^recipe_nutrient/(?P<pk>[0-9]+)$',
        RecipeNutrientDetailView.as_view(), name='recipe_nutrient_detail'),
]
