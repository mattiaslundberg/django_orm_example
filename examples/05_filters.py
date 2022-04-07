from django.db.models import Q
from examplemodel.models import Download, User, Track


# Simple examples

user, created = User.objects.get_or_create(email="one@example.com")
print("Get or create", user, created)

user = User.objects.get(email="one@example.com")
print("get", user)
try:
    user = User.objects.get(email="nonexisting")
    print("get fail", user)
except Exception:
    print("not found user", user)

user = User.objects.filter(email="one@example.com").first()
print("first", user)

user = User.objects.filter(email="nonexisting").first()
print("first failed", user)
