import datetime


def mili_to_date(milisecond):
    """ this function converts milisecond to date """
    a = datetime.datetime.fromtimestamp(float(milisecond)/1000)
    a = a.strftime('%Y-%m-%d %H:%M:%S.%f')

    return a
