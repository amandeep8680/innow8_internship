from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('tracks', TrackviewSet)
router.register('album-string', AlbumStringSerializer)
router.register('album-pk', AlbumPrimaryKeySerializer)
router.register('album-pk-write', AlbumPrimaryKeyWritableSerializer)
router.register('album-slug', AlbumSlugSerializer)
router.register('album-hyperlink', AlbumHyperlinkSerializer)
router.register('album-nested', AlbumNestedSerializer)
router.register('album-nested-write', AlbumNestedwritableSerializer)

urlpatterns = [
    path('', include(router.urls)),
]