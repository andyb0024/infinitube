from django.urls import path
from.views import AlbumListApiView,AlbumDetailApiView,MusicDetailApiView
urlpatterns = [
   path('album/', AlbumListApiView.as_view(), name='list'),
   path('album/<int:pk>/', AlbumDetailApiView.as_view(), name='album-detail-api'),
   path('album/<int:pk>/<music_slug>', MusicDetailApiView.as_view(), name='lesson_detail')

   # path('course-list/<slug:slug>/', CourseDetailApiView.as_view(), name='course-detail-api'),
   # path('course-list/<course_slug>/<lesson_slug>', LessonDetailApiView.as_view(), name='lesson_detail')


]