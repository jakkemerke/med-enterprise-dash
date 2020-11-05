from pyramid.httpexceptions import HTTPFound
from med_enterprise_dash.routes import (
    get_profile_route_name,
    get_login_verification_route_name,
    get_logout_route_name,
)
from med_enterprise_dash.utils.session import get_username
from med_enterprise_dash.micro_services.permissions import get_sysadmin


# TODO: Wire this up to a testing micro service.
def login_manually(is_sysadmin, username_sso, username_input, password):
    return False


# TODO: Wire this up to a testing micro service.
def login_automatically(username):
    return True


def get_login_verification_view(request):
    if "username" not in request.session:
        raise HTTPFound(get_url_to_login(request))

    if (
        "username" in request.POST
        and "password" in request.POST
        and login_manually(
            get_sysadmin(request.session["permissions_dict"]),
            get_username(request),
            request.POST["username"],
            request.POST["password"],
        )
    ) or login_automatically(get_username(request)):
        request.session["login_verification"] = True
        raise HTTPFound(
            request.route_url(
                request.session.get("last_stop", get_profile_route_name())
            )
        )

    return {
        "name": "foo",
        "cancel": request.route_url(get_logout_route_name()),
        "form_action": request.route_url(get_login_verification_route_name()),
    }
