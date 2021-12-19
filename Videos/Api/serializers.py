from rest_framework import serializers
from Videos.models import Album,Artiste,Music
from membership.Api.serializers import MembershipSerializer
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields =['name']

class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields =['title']

class AlbumSerializer(serializers.ModelSerializer):
    artiste =ArtistSerializer()

    class Meta:
        model = Album
        fields = ['title','artiste']
