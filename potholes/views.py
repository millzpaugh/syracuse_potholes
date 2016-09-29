from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.views.generic import View, TemplateView
import geopy
from geopy import GoogleV3
from potholes.forms import MapSearchForm
from potholes.models import Location
import geopy.distance



class MapSearchView(View):
    template = 'search.html'
    form = MapSearchForm()

    def get(self, request, *args, **kwargs):
        syracuse = [43.0481, -76.1474]
        geodata = []

        return render(request,  self.template, {'geodata':geodata,
                                                'center':syracuse,
                                                'form':self.form})

    def post(self, request, *args, **kwargs):
        form = MapSearchForm(request.POST)
        geodata = []
        radius = 1
        if form.is_valid():
            form_data = form.cleaned_data
            location = form_data['location']
            if form_data['radius']:
                radius = form_data['radius']

            geolocator = GoogleV3()
            address, (latitude, longitude) = geolocator.geocode(location)
            center = [latitude, longitude]

            geocenter = geopy.Point(latitude, longitude)

            locations = Location.objects.all()
            pothole_locations = []
            for l in locations:
                player_location = geopy.Point(l.latitude, l.longitude)
                if geopy.distance.distance(geocenter, player_location).miles < radius and l.address:
                    pothole_locations.append(l)

            geodata = [{'properties':{'title': l.player.tmf_name, 'description': 'TMF Player!',  'marker-symbol': 'pitch'}, 'geometry': {'coordinates': [l.latitude, l.longitude], 'type': 'Point'}, 'type': 'Feature'} for l in pothole_locations]

            return render(request,  self.template, {'geodata':geodata,
                                                'center':center,
                                                'post':True,
                                                'players':len(player_locations),
                                                'radius':radius})
        else:
            alexandria = [38.9047, -77.0164]

            return render(request,  self.template, {'form':form,
                                                'center':alexandria,
                                                'geodata':geodata,
                                                'post':False})


