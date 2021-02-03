import pyramid.httpexceptions as exc

from med_enterprise_dash.config import (
    get_branding,
    get_installation_subdirectory,
    get_med_config,
    get_static_path_offset,
)
from med_enterprise_dash.micro_services.permissions import get_apps_routes
from med_enterprise_dash.routes import (
    get_login_route_name,
    get_login_verification_route_name,
)
from med_enterprise_dash.utils.footer import get_footer
from med_enterprise_dash.utils.session import get_username
from med_enterprise_dash.views.data_entry.route_names import (
    get_data_entry_countries_route_name,
    get_data_entry_events_route_name,
    get_data_entry_organizations_route_name,
    get_data_entry_programs_route_name,
    get_data_entry_route_name,
    get_data_entry_submission_route_name,
    get_data_entry_terms_route_name,
    get_data_entry_traceability_route_name,
    get_data_entry_tracks_route_name,
)


def get_clientside_path_offset():
    return get_static_path_offset(get_installation_subdirectory(get_med_config()))


def get_data_entry_view_apis(request):
    return {
        "countries": request.route_url(get_data_entry_countries_route_name()),
        "events": f"{request.route_url(get_data_entry_events_route_name())}?id=",
        "organizations": f"{request.route_url(get_data_entry_organizations_route_name())}?s=",
        "programs": request.route_url(get_data_entry_programs_route_name()),
        "submit": request.route_url(get_data_entry_submission_route_name()),
        "terms": request.route_url(get_data_entry_terms_route_name()),
        "traceability_tags": request.route_url(
            get_data_entry_traceability_route_name()
        ),
        "tracks": request.route_url(get_data_entry_tracks_route_name()),
    }


def get_data_entry_view(request):
    if "login_verification" not in request.session:
        request.session["last_stop"] = get_data_entry_route_name()
        raise exc.HTTPFound(request.route_url(get_login_verification_route_name()))

    if "username" in request.session and "permissions_dict" in request.session:
        return {
            "branding": get_branding(),
            "name": get_data_entry_route_name(),
            "username": get_username(request),
            "route_prefix": get_clientside_path_offset(),
            "apps": get_apps_routes(request.session["permissions_dict"]),
            "footer": get_footer(),
            "apis": get_data_entry_view_apis(request),
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
