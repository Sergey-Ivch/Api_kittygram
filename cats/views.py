from .models import Cat
from rest_framework import viewsets, filters
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """
    Конечная точка API, позволяющая просматривать и редактировать Cats.
    """

    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

    filterset_fields = ['breed', 'life_expectancy', 'cat_size']  # Enable filtering on these fields
    search_fields = ['breed', 'personality']  # Enable search on these fields
    ordering_fields = ['breed', 'life_expectancy', 'cat_size'] #Enable ordering
    ordering = ['breed']