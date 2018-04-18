from __future__ import print_function
import os
from urllib.request import urlopen
import urllib
from urllib.parse import urlencode as urlencode
import xml.etree.ElementTree as ET
import re, string
import json
from random import randint


def lambda_handler(event, context):
    """
    this function is a route handler that routes incoming launchRequest or intentRequsts
    referenced codebase from: https://github.com/n8henrie
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])
    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    print('intent', intent)
    print('intent name', intent_name)
    # Dispatch to your skill's intent handlers
    if intent_name == "wolfman":
        return get_WolfRam(intent, session)
    else:
        speech_output = "Can You repeat your question?"
        return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup



# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome to Wolfram"
    speech_output = "I am wolfman, Alexa's nerdy alter ego.  To ask me a question, phrase your question like this. wolfman, why are firetrucks red. or, wolfman, how many cups are there in a quart."
    reprompt_text = "Can you repeat the question"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_WolfRam(intent, session):


    session_attributes = {}
    should_end_session = False
    reprompt_text = "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
    speech_output = "Try asking a question you would ask Wolfram Alpha."
    appid = os.environ["WOLFRAM_ID"]

    query = intent['slots']['response'].get('value')
    if not query:
        speech_output = "Can You repeat your question?"
        return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
    query = re.sub('[%s]' % re.escape(string.punctuation), '', query).replace(' ', '+')
    url = "http://api.wolframalpha.com/v1/spoken?i="+query + "&appid=" + appid
    url1 = "http://api.wolframalpha.com/v1/result?i="+query + "%3F&appid=" + appid
    print('url - ', url)
    print('url2 - ', url1)
    if url == None:
        pass
    try:
        data = urlopen(url)
    except urllib.error.URLError as e:
        try:
            data = urlopen(url1)
        except urllib.error.URLError as e:
            try:
                url2 = "https://api.wolframalpha.com/v2/query?input="+query + "&format=plaintext&output=JSON&appid=" + appid
                print(url2)
                data = urlopen(url2)
                tree = data.read().decode('utf-8')
                tree = json.loads(tree)
                try:
                    tree = tree['queryresult']['pods'][1]['subpods'][0]['plaintext']
                    tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)
                    speech_output = "Wolfram Alpha says " + tree
                    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
                except e:
                    speech_output = "Can You repeat your question?"
                    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
            except urllib.error.URLError as e:
                speech_output = "I may be smarter than alexa, but even I have my limits.  Try asking in a different way, and make sure you start your question with by saying my name, wolfman."
                print(speech_output)
                return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))

    tree = data.read().decode('utf-8')
    tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)

    """generate a random output response prefix"""
    random = randint(1,5)
    # random = 5
    if random is 1:
        speech_output = "Ziggy says " + str(tree)
    if random is 2:
        speech_output = "That was easy to find, " + str(tree)
    if random is 3:
        speech_output = "Had to dust off the old encyclopedia on that one. " + str(tree)
    if random is 4:
        speech_output = str(tree) + ", Boom!"
    if random is 5:
        speech_output = "The bat pewter says " + str(tree)

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


def multiple_replace(dict, text):
    """
    regex solution referenced codebase from: https://github.com/n8henrie
    """
    # Create a regular expression  from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
