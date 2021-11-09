from portage.service import portage_service


class PortageController():
    def find_driver(latitude, longitude):
        return portage_service.PortageService.find_driver_service(latitude, longitude)