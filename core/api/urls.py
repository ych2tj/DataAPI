from rest_framework.routers import DefaultRouter
from django.urls import path, include
from customers.api.urls import customer_router
from financedata.api.urls import shareprice_router

router = DefaultRouter()

# customers
# financedata
router.registry.extend(customer_router.registry)
router.registry.extend(shareprice_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]