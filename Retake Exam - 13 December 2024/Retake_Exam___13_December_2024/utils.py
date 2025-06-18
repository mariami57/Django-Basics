from traveler.models import Traveler


def get_traveler():
    return Traveler.objects.first()