from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UsersSpotify, ArtistsSpotify

router = DefaultRouter(trailing_slash = False)

router.register(r'users', UserViewSet, basename = 'users')
router.register(r'users-spotify', UsersSpotify, basename = 'users-spotify')
router.register(r'artists-spotify', ArtistsSpotify, basename = 'artists-spotify')

urlpatterns = router.urls