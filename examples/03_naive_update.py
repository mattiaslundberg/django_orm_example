from examplemodel.models import Download, User, Track


user = User.objects.first()
track = Track.objects.first()

download = Download.objects.filter(user=user, track=track).get()

download.count += 1

download.save(update_fields=["count"])
