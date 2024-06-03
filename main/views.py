from rest_framework import viewsets
from .models import English
from .serializers import EnglishSerializer
from rest_framework.response import Response
from rest_framework import status


class EnglishViewSet(viewsets.ModelViewSet):
    queryset = English.objects.all()
    serializer_class = EnglishSerializer  # Укажите ваш сериализатор

    def get_queryset(self):
        queryset = English.objects.all()
        name = self.request.query_params.get('name', None)
        translate = self.request.query_params.get('translate', None)
        category = self.request.query_params.get('category', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if translate:
            queryset = queryset.filter(translate__icontains=translate)
        if category:
            queryset = queryset.filter(category__icontains=category)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
