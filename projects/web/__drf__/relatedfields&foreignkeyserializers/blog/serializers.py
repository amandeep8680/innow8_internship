from rest_framework import serializers
from .models import Album , Track


class AlbumStringSerializer(serializers.ModelSerializer):
    tracks  = serializers.StringRelatedField(many = True)
    class Meta:
        model = Album
        fields = ['id','name','tracks']


# read only
class AlbumPrimaryKeySerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True , read_only = True)
    class Meta:
        model = Album
        fields = ['id','name','tracks']

# write version
class AlbumPrimaryKeyWritableSerializer(serializers.ModelSerializer):
    tracks = serializers.PrimaryKeyRelatedField(many=True,
                                                queryset = Track.objects.all())
    class Meta:
        model = Album
        fields = ['id','name','tracks']




class AlbumSlugSerializer(serializers.ModelSerializer):
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
class TrackSerializer (serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','title']

class AlbumNestedSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True , read_only = True)

    class Meta:
        model = Album
        fields = ['id','name','tracks']


# writable
class TrackwritableSerializer (serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id','title']

class AlbumNestedwritableSerializer(serializers.ModelSerializer):
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