from django.db import models

# Create your models here.

class Location(models.Model):
    street_num = models.CharField(max_length=200, null=True, blank=True)
    street_name = models.CharField(max_length=200, null=True, blank=True)
    street_name_post_type = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=140, null=True, blank=True)
    latitude = models.FloatField(default=0, null=True, blank=True)
    longitude = models.FloatField(default=0, null=True, blank=True)

    # def save(self, **kwargs):
    #     if self.latitude is None or self.longitude is None or int(self.latitude) == 0 or int(self.longitude) == 0:
    #         try:
    #             geolocator = GoogleV3()
    #             self.address, (self.latitude, self.longitude) = geolocator.geocode(self.address)
    #         except:
    #             self.latitude = 0
    #             self.longitude = 0
    #     super(Location, self).save()
