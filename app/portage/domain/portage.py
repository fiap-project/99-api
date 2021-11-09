import json
from portage.controller import portage_controller
from django.http import JsonResponse
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pprint import pprint


class PortageDomain():
    @csrf_exempt
    def nearby_drivers(request):
        # pprint('Raw Data: "%s"' % request.body[''])

        request = json.loads(request.body)
        latitude = request['latitude']
        longitude = request['longitude']

        JsonResponse(portage_controller.PortageController.find_driver(latitude, longitude))

        # return HttpResponse(str(request['latitude']))

