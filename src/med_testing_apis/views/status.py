def get_status_pub_health_route_name():
    return "status_pub_health"


def get_status_pub_health(request):
    return [
        {"system": "belts", "status": "good"},
        {"system": "cogs", "status": "good"},
        {"system": "fans", "status": "good"},
        {"system": "gears", "status": "good"},
        {"system": "rotors", "status": "good"},
        {"system": "sprockets", "status": "good"},
        {"system": "widgets", "status": "good"},
    ]
