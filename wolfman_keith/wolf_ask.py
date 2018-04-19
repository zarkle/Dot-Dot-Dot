"""
this is an alexa skill to access the wolfram alpha conversational api.
"""

"""global imports"""
from __future__ import print_function
from xml.etree.ElementTree as xml_etree
import os

try:
    from urllib.request import urlopen
    from urllib.parse import urlencode
except ImportError:
    from urllib2 import urlopen
    from urllib import urlencode


def lambda_handler(event, context):
    """
    this function is a route handler that routes incoming launchRequest or intentRequsts
    referenced: https://github.com/n8henrie
    """

    print("event.session.appliationID=" + event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestID': event['request']['requestedID']}, event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])

    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])

    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    print("on_session_stated")
