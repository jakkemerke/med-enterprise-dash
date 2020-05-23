from apps.appointments import *
from apps.appointments_alternate import *
from apps.data_entry import *
from apps.events import *
from apps.portal import *
from apps.lookup import *
from apps.status import *


def get_appointments_route():
    return "/appointments"


def get_appointments_alternate_route():
    return "/appointments_alternate"


def get_data_entry_route():
    return "/data_entry"


def get_events_route():
    return "/events"


def get_lookup_route():
    return "/lookup"


def get_portal_route():
    return "/portal"


def get_status_route():
    return "/status"


def includeme(config):
    config.add_route(get_appointments_route_name(), get_appointments_route())
    config.add_view(get_appointments_view, route_name=get_appointments_route_name())

    config.add_route(
        get_appointments_alternate_route_name(), get_appointments_alternate_route()
    )
    config.add_view(
        get_appointments_alternate_view,
        route_name=get_appointments_alternate_route_name(),
    )

    config.add_route(get_data_entry_route_name(), get_data_entry_route())
    config.add_view(get_data_entry_view, route_name=get_data_entry_route_name())

    config.add_route(get_events_route_name(), get_events_route())
    config.add_view(get_events_view, route_name=get_events_route_name())

    config.add_route(get_lookup_route_name(), get_lookup_route())
    config.add_view(get_lookup_view, route_name=get_lookup_route_name())

    config.add_route(get_portal_route_name(), get_portal_route())
    config.add_view(get_portal_view, route_name=get_portal_route_name())

    config.add_route(get_status_route_name(), get_status_route())
    config.add_view(get_status_view, route_name=get_status_route_name())
