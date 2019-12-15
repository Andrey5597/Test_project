from django.urls import path

from .views import AlbumCreateView, UserAlbumsView, PictureCreateView, PictureCreateBase64View, PicturesView, AlbumDetailsView, PictureDetailsView
app_name = 'foto_album'

urlpatterns = [
    path('albums/', UserAlbumsView.as_view(), name='albums'),
    path('albums/create/', AlbumCreateView.as_view(), name='create album'),
    path('pictures/create/', PictureCreateView.as_view(), name='pictures'),
    path('pictures/create/base64/', PictureCreateBase64View.as_view(), name='pictures'),
    path('pictures/', PicturesView.as_view(), name='pictures'),
    path('albums/<int:album_id>/', AlbumDetailsView.as_view(), name='pictures'),
    path('pictures/<int:picture_id>/', PictureDetailsView.as_view(), name='pictures'),

]
