from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LangueViewSet, MotAdminViewSet, MotViewSet, PropositionViewSet

router = DefaultRouter()
router.register(r'langues', LangueViewSet)
router.register(r'mots', MotViewSet)
router.register(r'propositions', PropositionViewSet)
#router.register(r'mots-admin', MotAdminViewSet)


urlpatterns = [
    path('', include(router.urls)),
]

