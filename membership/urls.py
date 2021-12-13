from django.urls import path
from.views import MembershipSelectView
urlpatterns = [
    path('', MembershipSelectView.as_view(),name='select'),
#     path('album/<int:pk>/', AlbumDetail.as_view(), name='album-detail'),
#     path('<int:pk>/<music_slug>', MusicDetail.as_view(), name='music_detail')
 ]