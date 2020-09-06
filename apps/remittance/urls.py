from django.urls import path, include
from apps.remittance import views
from rest_framework.routers import DefaultRouter


app_name = 'remittance'

router = DefaultRouter()
router.register('', views.RemittanceViewSet)

urlpatterns = [
    path('', include(router.urls))
]
