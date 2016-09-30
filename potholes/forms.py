from django import forms
from geopy import GoogleV3
from django.shortcuts import render_to_response, redirect



class MapSearchForm(forms.Form):
    location = forms.CharField(required=True, label="Enter a Location in Syracuse", widget=forms.TextInput(attrs={'placeholder': 'Enter Location: 116 Avondale St'})
    )
    radius = forms.IntegerField(required=False, label="Radius (optional, defaults to 2 miles)", widget=forms.TextInput(attrs={'placeholder': 'Radius'})
    )

    def clean(self):
        cleaned_data = super(MapSearchForm, self).clean()
        location = cleaned_data.get("location")
        geolocator = GoogleV3()

        try:
            address, (latitude, longitude) = geolocator.geocode(location)
        except:
            msg = "Oops! We couldn't find that location."
            self.add_error("location", msg)
            return redirect('map-search')