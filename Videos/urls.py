from django.urls import path
from.views import album,AlbumDetail,MusicDetail,MembershipAlbumView
urlpatterns = [
    path('album', MembershipAlbumView.as_view(),name='list'),
    path('album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
    path('<int:pk>/<music_slug>', MusicDetail.as_view(), name='music_detail')
]