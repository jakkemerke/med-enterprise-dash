from pyramid.response import Response
import pyramid.httpexceptions as exc
from cas import CASClient
from utils import get_profile_route_name, get_home_route_name, get_login_route_name

cas_client = CASClient(
    version=3,
    service_url=f"http://localhost:6543/login?next={get_profile_route_name()}",
    server_url="https://django-cas-ng-demo-server.herokuapp.com/cas/",
)


def get_username(request):
    if request.session:
        return request.session["username"]
    else:
        return ""


def get_home_view(request):
    return {
        "name": get_home_route_name(),
        "username": get_username(request),
    }


def is_logged_in(request):
    return get_username(request) != ""


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

    # app.logger.debug('ticket: %s', ticket)
    # app.logger.debug('next: %s', next)

    try:
        user, attributes, pgtiou = cas_client.verify_ticket(ticket)

        # app.logger.debug(
        #     'CAS verify ticket response: user: %s,
        #     attributes: %s, pgtiou: %s', user, attributes, pgtiou)

        if not user:
            return Response('Failed to verify ticket. <a href="/login">Login</a>')
        else:
            request.session["username"] = user
            raise exc.HTTPFound(request.route_url(next))

    except Exception as exception:
        # app.logger.error(exception)
        return Response('Error trying to verify ticket. <a href="/login">Login</a>')


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
    return {"name": "Apps"}


def profile(request):
    session = request.session
    if "username" in session:
        return {
            "name": get_profile_route_name(),
            "username": get_username(request),
        }
    else:
        raise exc.HTTPFound(request.route_url(get_login_route_name()))
