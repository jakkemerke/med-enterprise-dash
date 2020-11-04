from pyramid.response import Response
import pyramid.httpexceptions as exc

from med_enterprise_dash.auth import get_cas_client
from med_enterprise_dash.config import (
    developer_auto_login_enabled,
    get_developer_username,
)
from med_enterprise_dash.routes import get_profile_route_name
from med_enterprise_dash.utils.toml import get_med_config
from med_enterprise_dash.utils.session import is_logged_in


def get_param(request, key, failsafe=None):
    return (
        failsafe
        if not request or not request.params or not request.params[key]
        else request.params[key]
    )


def get_next(request):
    return get_param(request, "next", get_profile_route_name())


def get_ticket(request):
    return get_param(request, "ticket")


def pass_users_with_existing_auth(request, med_config):
    if developer_auto_login_enabled(med_config):
        request.session["username"] = get_developer_username(med_config)
    if is_logged_in(request):
        raise exc.HTTPFound(request.route_url(get_profile_route_name()))


def login(request):
    med_config = get_med_config()

    pass_users_with_existing_auth(request, med_config)

    next = get_next(request)
    ticket = get_ticket(request)
    cas_client = get_cas_client(med_config)

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
