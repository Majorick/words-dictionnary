from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LangueViewSet, MotViewSet, PropositionViewSet

router = DefaultRouter()
router.register(r'langues', LangueViewSet)
router.register(r'mots', MotViewSet)
router.register(r'propositions', PropositionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
