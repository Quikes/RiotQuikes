from django.shortcuts import render

from config.settings import CACHE_TTL
from .serializers import ImageSerializer
from .models import Image
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from django.core.cache import cache
from django.utils.cache import _generate_cache_header_key
from rest_framework import viewsets,permissions
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class ImageViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]


    def get_queryset(self):
        user = self.request.user
        return Image.objects.filter(author=user)

    
    def get_serializer_class(self):
        return ImageSerializer

    @method_decorator(cache_page(CACHE_TTL,key_prefix='images_list'))
    @method_decorator(vary_on_cookie)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)