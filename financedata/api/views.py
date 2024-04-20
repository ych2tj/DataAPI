from rest_framework import viewsets
from .serializer import sharepriceSerial
from ..models import shareprice

class sharepriceViewSet(viewsets.ModelViewSet):
    queryset = shareprice.objects.all()
    serializer_class = sharepriceSerial