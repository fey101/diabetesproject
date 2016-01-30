from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import (
    Recipe,
    FoodItem,
    FoodCategory,
    FoodItemCategory
)

from .serializers import (
    FoodItemSerializer,
    RecipeSerializer,
    FoodCategorySerializer,
    FoodItemCategorySerializer
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


class FoodCategoryListView(ListCreateAPIView):

    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer

    def create(self, request):
        from pdb import set_trace
        set_trace
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            from_q = data.pop('category')
            to_q = data.pop('caloric_value_per_gram')
            # queue = Queue.objects.get(id=from_q)
            # g = models.VisitsTransitionGraph1.objects.create(
            #     t_source=queue,
            #     organisation=request.user.organisation)
            # for item in to_q:
            #     g.t_destination.add(Queue.objects.get(id=item))
            g = FoodCategory.objects.create(
                category=from_q, caloric_value_per_gram=to_q)
            return Response(self.serializer_class(g).data, status=201)
        else:
            return Response(serializer.errors, status=400)


class FoodCategoryDetailView(RetrieveUpdateDestroyAPIView):

    queryset = FoodCategory.objects.all()
    serializer_class = FoodCategorySerializer
    lookup_field = 'pk'


class FoodItemCategoryListView(ListCreateAPIView):

    queryset = FoodItemCategory.objects.all()
    serializer_class = FoodItemCategorySerializer


class FoodItemCategoryDetailView(RetrieveUpdateDestroyAPIView):

    queryset = FoodItemCategory.objects.all()
    serializer_class = FoodItemCategorySerializer
    lookup_field = 'pk'
