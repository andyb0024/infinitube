from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from .models import Music, Album
from membership.models import Membership, UserMembership


# Create your views here.
class MembershipAlbumView(ListView):
    context_object_name = 'object_list'
    queryset = Membership.objects.all()
    template_name = "Videos/album_list.html"

def album(request):
    qs = Album.objects.all()
    membership_qs=Membership.objects.all()
    for x in membership_qs:
        print(x.album)
    context = {
        "qs": qs,
        "object":membership_qs
    }
    return render(request, 'Videos/album_list.html', context)


class AlbumDetail(DetailView):
    model = Album



class MusicDetail(View):
    def get(self, request, pk, music_slug, *args, **kwargs):
        album_qs = Album.objects.filter(pk=pk)
        if album_qs.exists():
            album = album_qs.first()

        music_qs = album.musics.filter(slug=music_slug)
        if music_qs.exists():
            music = music_qs.first()
        user_membership = UserMembership.objects.filter(user=request.user.id).first()
        user_membership_type = user_membership.membership.membership_type
        album_allowed_mem_types = album.allowed_memberships.all()
        context = {
            "object": None
        }
        if album_allowed_mem_types.filter(membership_type=user_membership_type).exists():
           context = {
              "object": music
           }

        return render(request, 'Musics/music_list.html', context)
