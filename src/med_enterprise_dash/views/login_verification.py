import pyramid.httpexceptions as exc
from med_enterprise_dash.routes import get_profile_route_name


def get_login_verification_view(request):
    from pyramid.response import Response

    request.session["login_verification"] = True
    raise exc.HTTPFound(
        request.route_url(request.session.get("last_stop", get_profile_route_name()))
    )
