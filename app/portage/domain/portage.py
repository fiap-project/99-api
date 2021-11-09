import json
from portage.controller import portage_controller
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


class PortageDomain():
    @csrf_exempt
    def nearby_drivers(request):
        request_body = json.loads(request.body)
        latitude = request_body['latitude']
        longitude = request_body['longitude']
        car_type = request_body['car_type']

        if car_type == "camionete" or car_type == "van":
            response = JsonResponse(portage_controller.PortageController.find_driver(latitude, longitude, car_type))
        else:
            response = JsonResponse("Vehycle not allowed")

        return response

