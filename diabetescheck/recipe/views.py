from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import (
    Recipe,
    FoodItem,
)

from .serializers import (
    FoodItemSerializer,
    RecipeSerializer,
)


class RecipeListView(ListCreateAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'


class FoodItemListView(ListCreateAPIView):

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer


class FoodItemDetailView(RetrieveUpdateDestroyAPIView):

    queryset = FoodItem.objects.all()
    serializer_class = FoodItemSerializer
    lookup_field = 'pk'
