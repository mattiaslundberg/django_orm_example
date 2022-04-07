from django.db.models import Q
from examplemodel.models import Download, User, Track

tracks = Track.objects.filter(Q(artist__name="Ooyy") | Q(artist__name="Raccy"))
print(tracks.query)
