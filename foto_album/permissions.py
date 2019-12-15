from rest_framework.permissions import BasePermission
from foto_album.models import Album, Picture
from django.shortcuts import get_object_or_404


class AlbumOwnerPermission(BasePermission):
    message = "You don't have access to this album."

    def has_permission(self, request, view):
        album = get_object_or_404(Album, id=view.kwargs['album_id'])
        if album.owner != request.user:
            return False
        view.album = album
        return True


class PictureOwnerPermission(BasePermission):
    message = "You don't have access to this picture."

    def has_permission(self, request, view):
        picture = get_object_or_404(Picture, id=view.kwargs['picture_id'])
        if picture.album.owner != request.user:
            return False
        view.picture = picture
        return True
