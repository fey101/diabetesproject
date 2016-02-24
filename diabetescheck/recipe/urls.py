from django.conf.urls import url

from .views import (
    RecipeListView,
    RecipeDetailView,
    FoodItemListView,
    FoodItemDetailView,
    FoodCategoryListView,
    FoodCategoryDetailView,
    NutritionalValueListView,
    NutritionalValueDetailView
)


urlpatterns = [
    url(r'^recipes/', RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipes/(?P<pk>[0-9]+)$',
        RecipeDetailView.as_view(), name='recipe_detail'),

    url(r'^food_items/',
        FoodItemListView.as_view(), name='food_item_list'),
    url(r'^food_items/(?P<pk>[0-9]+)$',
        FoodItemDetailView.as_view(), name='food_item_detail'),

    url(r'^food_categories/',
        FoodCategoryListView.as_view(), name='food_category_list'),
    url(r'^food_categories/(?P<pk>[0-9]+)$',
        FoodCategoryDetailView.as_view(), name='food_category_detail'),

    url(r'^nutritional_values/',
        NutritionalValueListView.as_view(), name='nutritional_value_list'),
    url(r'^nutritional_values/(?P<pk>[0-9]+)$',
        NutritionalValueDetailView.as_view(), name='nutritional_value_detail'),
]
