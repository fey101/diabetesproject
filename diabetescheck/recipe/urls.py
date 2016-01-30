from django.conf.urls import url

from .views import (
    RecipeListView,
    RecipeDetailView,
    FoodItemListView,
    FoodItemDetailView,
    FoodCategoryListView,
    FoodCategoryDetailView,
    FoodItemCategoryListView,
    FoodItemCategoryDetailView
)


urlpatterns = [
    url(r'^recipes/', RecipeListView.as_view(), name='recipe_list'),
    url(r'^recipes/(?P<pk>[0-9]+)$',
        RecipeDetailView.as_view(), name='recipe_detail'),

    url(r'^food_items/',
        FoodItemListView.as_view(), name='food_item_list'),
    url(r'^food_items/(?P<pk>[0-9]+)$',
        FoodItemDetailView.as_view(), name='food_item_detail'),

    url(r'^food_category/',
        FoodCategoryListView.as_view(), name='food_category_list'),
    url(r'^food_category/(?P<pk>[0-9]+)$',
        FoodCategoryDetailView.as_view(), name='food_category_detail'),

    url(r'^fooditem_category/',
        FoodItemCategoryListView.as_view(), name='fooditem_category_list'),
    url(r'^fooditem_category/(?P<pk>[0-9]+)$',
        FoodItemCategoryDetailView.as_view(), name='fooditem_category_detail'),
]
