from rest_framework.generics import ListAPIView
from  rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from Videos.models import Album,Music
from .serializers import AlbumSerializer,MusicSerializer

class AlbumListApiView(ListAPIView):
    serializer_class = AlbumSerializer
    def get_queryset(self):
        qs=Album.objects.all()
        return qs



class AlbumDetailApiView(APIView):
    def get_object(self,pk):
        try:
            return Album.objects.get(pk=pk)
        except Album.DoesNotExists():
            raise Http404

    def get(self,request,pk):
            qs=self.get_object(pk)
            serializer=AlbumSerializer(qs)
            return Response(serializer.data)

class MusicDetailApiView(APIView):
    def get(self,request,pk,music_slug,*args,**kwargs):
        album_qs=Album.objects.filter(pk=pk)
        if album_qs.exists():
            album=album_qs.first()
        music_qs=album.musics.filter(slug=music_slug)
        if music_qs.exists():
            music=music_qs.first()
        serializer=MusicSerializer(music)
        context = {
                'Music': serializer.data
            }
        return Response(context)


























