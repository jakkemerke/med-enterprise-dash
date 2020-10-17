import pyramid.httpexceptions as exc


from auth import get_cas_client
from routes import get_logout_callback_route_name
from utils.toml import get_med_config


def logout(request):
    cas_client = get_cas_client(get_med_config())
    redirect_url = request.route_url(get_logout_callback_route_name())
    cas_logout_url = cas_client.get_logout_url(redirect_url)

    # NOTE: Not all CAS instances have enabled callbacks.
    request.session.invalidate()
    raise exc.HTTPFound(cas_logout_url)
