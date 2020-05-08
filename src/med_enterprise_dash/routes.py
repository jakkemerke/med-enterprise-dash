from pyramid.response import Response
import pyramid.httpexceptions as exc

from auth import get_auth_client
from utils import (
    get_profile_route_name,
    get_home_route_name,
    get_login_route_name,
    get_apps_route_name,
)

# import logging
# log = logging.getLogger(__name__)

cas_client = get_auth_client()


def get_username(request):
    if request.session:
        return request.session["username"]
    else:
        return ""


def has_username(username):
    return username and username != ""


def is_logged_in(request):
    return has_username(get_username(request))


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
    }


def login(request):
    if is_logged_in(request):
        raise exc.HTTPFound(request.route_url(get_profile_route_name()))

    next = None
    ticket = None

    if request.params:
        next = request.params["next"]
        ticket = request.params["ticket"]

    if not next:
        next = get_profile_route_name()

    if not ticket:
        raise exc.HTTPFound(cas_client.get_login_url())

    # log.debug('ticket: %s', ticket)
    # log.debug('next: %s', next)

    user, attributes, pgtiou = cas_client.verify_ticket(ticket)

    # log.debug(
    #     'CAS verify ticket response: user: %s,
    #     attributes: %s, pgtiou: %s', user, attributes, pgtiou)

    if not user:
        return Response('Failed to verify ticket. <a href="/login">Login</a>')
    else:
        request.session["username"] = user
        next_url = request.route_url(next)
        raise exc.HTTPFound(next_url)


def logout(request):
    redirect_url = request.route_url("logout_callback")
    cas_logout_url = cas_client.get_logout_url(redirect_url)

    # NOTE: Not all CAS instances have enabled callbacks.
    request.session.invalidate()
    raise exc.HTTPFound(cas_logout_url)


def logout_callback(request):
    request.session.invalidate()
    return Response('Logged out. <a href="/login">Login</a>')


def apps(request):
    session = request.session
    if "username" in session:
        return {
            "name": get_apps_route_name(),
            "username": get_username(request),
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))


def profile(request):
    session = request.session
    if "username" in session:
        return {
            "name": get_profile_route_name(),
            "username": get_username(request),
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
