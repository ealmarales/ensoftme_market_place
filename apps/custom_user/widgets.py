from django.conf import settings
from django_google_maps.widgets import GoogleMapsAddressWidget

class CustomGoogleMapsAddressWidget(GoogleMapsAddressWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({'data-map-type': 'roadmap', 'data-marker-draggable': 'true'})  # Add marker draggable attribute

    class Media:
        css = {'all': ('https://maps.googleapis.com/maps/api/js?key={}&libraries=places'.format(settings.GOOGLE_MAPS_API_KEY),)}
        js = (
            'https://maps.googleapis.com/maps/api/js?key={}&libraries=places'.format(settings.GOOGLE_MAPS_API_KEY),
            'js/map.js',  # Path to your map.js file
        )