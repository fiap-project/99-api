from portage.repository import portage_repository


class PortageService():
    def find_driver_service(latitude, longitude, car_type):
        return portage_repository.PortageRepository.search_nearby_drivers(latitude, longitude, car_type)
