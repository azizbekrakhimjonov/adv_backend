from rest_framework.viewsets import ModelViewSet
from .models import Advertisement
from .serializers import AdvertisementSerializer

class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all().order_by('-created_at')
    serializer_class = AdvertisementSerializer
