from portage.repository import portage_repository


class PortageService():
    def find_driver_service(latitude, longitude):
        return portage_repository.PortageRepository.nearby_drivers(latitude, longitude)