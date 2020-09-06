from django.urls import path, include
from apps.user import views
from rest_framework.routers import DefaultRouter


app_name = 'user'

router = DefaultRouter()
router.register('', views.UserViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls))
]
