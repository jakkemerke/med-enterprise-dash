from apps.appointments import *
from apps.appointments_alternate import *
from apps.data_entry import *
from apps.events import *
from apps.portal import *
from apps.lookup import *
from apps.status import *


def includeme(config):
    config.include("apps.appointments.includeme")
    config.include("apps.appointments_alternate.includeme")
    config.include("apps.data_entry.includeme")
    config.include("apps.events.includeme")
    config.include("apps.portal.includeme")
    config.include("apps.lookup.includeme")
    config.include("apps.status.includeme")
