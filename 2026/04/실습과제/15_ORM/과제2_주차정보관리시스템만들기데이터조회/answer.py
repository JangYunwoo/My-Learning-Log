import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parking_management.settings')
django.setup()

from garages.models import Garage

print(Garage.objects.filter(location='독도'))
print(Garage.objects.filter(capacity__lte=30))
locations = Garage.objects.filter(is_parking_avaliable=1).values_list('location', flat=True)
for location in locations:
    print(location)