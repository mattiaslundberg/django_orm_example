from examplemodel.models import Track

for track in Track.objects.raw("select * from examplemodel_track"):
    print(track)
