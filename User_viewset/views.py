from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from.models import User
from .serializer import UserSerializer
from .apiSpotify import get_user_data, get_artist_data

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'id'

class UsersSpotify(viewsets.ViewSet):
    @action(detail = False, methods=['get'], url_path=r'spotify-user/(?P<spotify_id>[^/.]+)')
    def get_data(self, request, spotify_id = None):
        try:
            user_data = get_user_data(spotify_id)
            return Response(user_data, status=status.HTTP_200_OK)
        except not user_data:
            return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ArtistsSpotify(viewsets.ViewSet):
    @action(detail = False, methods=['get'], url_path=r'spotify-artist/(?P<spotify_artists_id>[^/.]+)')
    def get_data_artists(self, request, spotify_artists_id = None):
        try:
            user_data = get_artist_data(spotify_artists_id)
            return Response(user_data, status=status.HTTP_200_OK)
        except not user_data:
            return Response({"detail": "Artists not found"}, status=status.HTTP_404_NOT_FOUND)