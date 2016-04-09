from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from .models import (
    Recipe,
    Ingredients,
    RecipeIngredient,
    Nutrients,
    RecipeNutrients
)

from .serializers import (
    RecipeSerializer,
    IngredientSerializer,
    RecipeIngredientSerializer,
    NutrientsSerializer,
    RecipeNutrientSerializer,
)


class RecipeIngredientListView(ListCreateAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer


class RecipeIngredientDetailView(RetrieveUpdateDestroyAPIView):
    queryset = RecipeIngredient.objects.all()
    serializer_class = RecipeIngredientSerializer
    lookup_field = 'pk'


class RecipeListView(ListCreateAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'pk'


class IngredientsListView(ListCreateAPIView):

    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer
    lookup_field = 'pk'


class NutrientsListView(ListCreateAPIView):

    queryset = Nutrients.objects.all()
    serializer_class = NutrientsSerializer

    # def create(self, request):
    #     from pdb import set_trace
    #     set_trace()
    #     data = request.data
    #     serializer = self.serializer_class(data=data)
    #     if serializer.is_valid():
    #         from_q = data.pop('category')
    #         to_q = data.pop('caloric_value_per_gram')
    #         # queue = Queue.objects.get(id=from_q)
    #         # g = models.VisitsTransitionGraph1.objects.create(
    #         #     t_source=queue,
    #         #     organisation=request.user.organisation)
    #         # for item in to_q:
    #         #     g.t_destination.add(Queue.objects.get(id=item))
    #         g = FoodCategory.objects.create(
    #             category=from_q, caloric_value_per_gram=to_q)
    #         return Response(self.serializer_class(g).data, status=201)
    #     else:
    #         return Response(serializer.errors, status=400)


class NutrientDetailView(RetrieveUpdateDestroyAPIView):

    queryset = Nutrients.objects.all()
    serializer_class = NutrientsSerializer
    lookup_field = 'pk'


class RecipeNutrientListView(ListCreateAPIView):

    queryset = RecipeNutrients.objects.all()
    serializer_class = RecipeNutrientSerializer


class RecipeNutrientDetailView(RetrieveUpdateDestroyAPIView):

    queryset = RecipeNutrients.objects.all()
    serializer_class = RecipeNutrientSerializer
    lookup_field = 'pk'
