from django.db.models import Q
from examplemodel.models import Download, User, Track

tracks = Track.objects.all().select_related("artist")
print(tracks.query)
