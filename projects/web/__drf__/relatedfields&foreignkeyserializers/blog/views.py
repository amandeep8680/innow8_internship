from rest_framework import viewsets
from .models import Album, Track
from .serializers import *



class TrackviewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class =  TrackSerializer



# 🔹 Different Album APIs for each relation



class AlbumStringSerializer(viewsets.ModelViewSet):
    queryset = Album.objects.all().prefetch_related('tracks')
    serializer_class = AlbumStringSerializer

# read only
class AlbumPrimaryKeySerializer(viewsets.ModelViewSet):
    tracks = serializers.PrimaryKeyRelatedField(many=True , read_only = True)
    class Meta:
        model = Album
        fields = ['id','name','tracks']

# write version
class AlbumPrimaryKeyWritableSerializer(viewsets.ModelViewSet):
    tracks = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset = Track.objects.all())
    class Meta:
        model = Album
        fields = ['id','name','tracks']




class AlbumSlugSerializer(viewsets.ModelViewSet):
    tracks = serializers.SlugRelatedField(many=True , read_only = True , 
                                          slug_field = 'title')
    class Meta:
        model = Album
        fields = ['id','name','tracks']





class AlbumHyperlinkSerializer(serializers.HyperlinkedModelSerializer):
    tracks = serializers.HyperlinkedRelatedField(many=True , read_only = True,
                                                view_name = 'track-detail')
    class Meta:
        model = Album
        fields = ['url','id','name','tracks']



# readable
class TrackSerializer (viewsets.ModelViewSet):
    class Meta:
        model = Track
        fields = ['id','title']

class AlbumNestedSerializer(viewsets.ModelViewSet):
    tracks = TrackSerializer(many=True , read_only = True)

    class Meta:
        model = Album
        fields = ['id','name','tracks']


# writable
class TrackwritableSerializer (viewsets.ModelViewSet):
    class Meta:
        model = Track
        fields = ['id','title']

class AlbumNestedwritableSerializer(viewsets.ModelViewSet):
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id','name','tracks']

    def create(self , validated_data):
        track_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)

        for track in track_data:
            Track.objects.create(album=album , **track)
        return album