from django.core.management.base import BaseCommand, CommandError
import csv
import os
from os.path import dirname, realpath
from potholes.models import Location
import geopy
import logging

logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        Location.objects.all().delete()

        current_dir = os.path.dirname(realpath(__file__))
        file_path = current_dir + '/potholes.csv'
        with open(file_path, 'rU') as csvfile:
            reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in reader:

                print('ROW 23!!')
                row_content = row[0].split(',')
                latitude = row_content[0]
                # print(lat) 
                longitude = row_content[1]
                location = Location.objects.create(latitude=latitude,
                                                 longitude=longitude)
                location.save() 
                print(str(location.id) + " has been saved.")




