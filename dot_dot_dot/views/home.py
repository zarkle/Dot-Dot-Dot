from pyramid.view import view_config
from pyramid.security import NO_PERMISSION_REQUIRED
import requests
from datetime import datetime as dt


@view_config(
    route_name='home',
    renderer='../templates/index.jinja2',
    permission=NO_PERMISSION_REQUIRED)
def home_view(request):
    """home view displays all the queries and answers"""
    response = requests.get('https://ovnqlx5nog.execute-api.us-east-1.amazonaws.com/wolfman/data')
    data = response.json()
    for item in data['Items']:
        item['time_stamp'] = dt.fromtimestamp(item['time_stamp')//1000).strftime('%m-%d-%Y')
    return {'data': data['Items']}



