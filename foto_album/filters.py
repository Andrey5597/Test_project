from django_filters import rest_framework as filters
from foto_album.models import Album, Picture


class AlbumFilter(filters.FilterSet):
    id = filters.NumberFilter()
    title = filters.CharFilter()

    class Meta:
        model = Album
        fields = ('id', 'title',)


class PictureFilter(filters.FilterSet):
    id = filters.NumberFilter()
    title = filters.CharFilter()

    class Meta:
        model = Picture
        fields = ('id', 'title',)