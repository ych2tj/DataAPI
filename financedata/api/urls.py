from rest_framework.routers import DefaultRouter
from .views import sharepriceViewSet

shareprice_router = DefaultRouter()
shareprice_router.register(r'shareprices', sharepriceViewSet)