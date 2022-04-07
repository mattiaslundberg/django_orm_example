from examplemodel.models import Artist


artists = Artist.objects.all()
print(artists.query)


artists = Artist.objects.filter(name="Ooyy")
print(artists.query)
