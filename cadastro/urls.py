from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import VetViewSet, TutorViewSet, CadastroViewSet

router = DefaultRouter()
router.register(r'vets', VetViewSet)
router.register(r'tutores', TutorViewSet)
router.register(r'cadastros', CadastroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
