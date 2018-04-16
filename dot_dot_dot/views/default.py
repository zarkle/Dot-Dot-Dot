from pyramid.view import view_config
from . import DB_ERR_MSG

@view_config(route_name='home', renderer='../templates/base.jinja2')
def my_view(request):
    return {}
