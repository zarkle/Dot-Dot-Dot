import os
from urllib.request import urlopen
import urllib
import re
import string
import json
from random import randint


def lambda_handler(event, context):
    """
    this function is a route handler that routes incoming LaunchRequest or IntentRequest
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
    """
    Called when the user launches the skill without specifying what they want
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

    # Dispatch to your skill's intent handlers
    if intent_name == 'wolfman':
        return get_WolfRam(intent, session)


def on_session_ended(session_ended_request, session):
    """
    Called when the user ends the session.
    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup


# --------- below controls the skill interaction and behavior ------------
welcome_message = [
    'I am wolfman, Alexa\'s nerdy alter ego.  To ask me a question, phrase your question like this. wolfman, why are firetrucks red.',
    'Don\'t tell Alexa, but I am way smarter than she is.  To ask me a question, phrase your question like this. wolfman, how far away is the moon in inches.',
    'I am wolfman, Ask me a question like this. wolfman, why is the sky blue. or, wolfman, how far away is saturn.',
    'You can ask me almost any question, just make sure to start them with my name. wolfman'
    ]


def get_welcome_response():
    """controls welcome message on skill open"""
    session_attributes = {}
    card_title = 'Welcome to Wolfman'
    random = randint(0, 3)
    speech_output = welcome_message[random]
    reprompt_text = 'Can you repeat the question?'
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_WolfRam(intent, session):
    """controls get function to wolfram's APIs"""
    try:
        session_attributes = {}
        should_end_session = False
        reprompt_text = 'I didn\'t catch that. Please phrase your question like this. wolfman, what is the meaning of life?'
        speech_output = 'Try asking a question you would ask Wolfram Alpha.'
        appid = os.environ['WOLFRAM_ID']

        db_query = intent['slots']['response'].get('value')

        query = intent['slots']['response'].get('value')
        if 'sudo' in query:
            speech_output = "Ooooh, wow! Look at you. Are you trying to be a hacker or something?"
            return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
        if not query:
            speech_output = "Can you repeat your question?"
            return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
        query = re.sub('[%s]' % re.escape(string.punctuation), '', query).replace(' ', '+')
        url = 'http://api.wolframalpha.com/v1/spoken?i=' + query + '&appid=' + appid
        url1 = 'http://api.wolframalpha.com/v1/result?i=' + query + '&appid=' + appid

        # generate a random output response prefix
        custom_anwer = [
            'Ziggy says ',
            'That was easy to find, ',
            'Had to dust off the old encyclopedia on that one, ',
            'Boom! ',
            'Hal nine thousand says, ',
            'Hmmmm, let me think, ',
            'I don\'t know the answer to that, just kidding, '
            'My magic eight ball says ',
            'Beep bop boop boop beep boop bop beep. ',
            'Let me google that for you. '
            ]
        random = randint(0, 10)

        try:
            data = urlopen(url)
        except urllib.error.URLError:
            try:
                data = urlopen(url1)
            except urllib.error.URLError:
                try:
                    url2 = 'https://api.wolframalpha.com/v2/query?input=' + query + '&format=plaintext&output=JSON&appid=' + appid
                    data = urlopen(url2)
                    tree = data.read().decode('utf-8')
                    tree = json.loads(tree)
                    try:
                        tree = tree['queryresult']['pods'][1]['subpods'][0]['plaintext']
                        if len(tree) > 5:
                            tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)
                            db_tree = tree
                            speech_output = tree
                            create_record_dynamodb(db_query, db_tree)
                        else:
                            speech_output = 'I have no data'
                        return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))

                    except KeyError:
                        speech_output = 'Can you repeat your question?'
                        return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))
                except urllib.error.URLError:
                    speech_output = 'I may be smarter than alexa, but even I have my limits.  Try asking in a different way, and make sure you start your question with by saying my name, wolfman.'
                    return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))

        tree = data.read().decode('utf-8')
        db_tree = tree
        tree = re.sub('[%s]' % re.escape(string.punctuation), '', tree)

        speech_output = custom_anwer[random] + str(tree)
        create_record_dynamodb(db_query, db_tree)

        return build_response(session_attributes, build_speechlet_response(
            intent['name'], speech_output, reprompt_text, should_end_session))
    except:
        speech_output = 'Hmmm, ask me again and make sure you start with my name, wolfman.'
        return build_response(session_attributes, build_speechlet_response(intent['name'], speech_output, reprompt_text, should_end_session))


def create_record_dynamodb(db_query, db_tree):
    import boto3
    import time
    client = boto3.resource('dynamodb', region_name='us-east-1')
    table = client.Table('new_wolf_db')

    time = int(round(time.time()) * 1000)

    new_query_response = {
            'time_stamp': time,
            'time_sort_stamp': time,
            'wf_query': db_query,
            'wf_response': db_tree
        }

    table.put_item(Item=new_query_response)


def multiple_replace(dict, text):
    """
    regex solution
    """
    # Create a regular expression from the dictionary keys
    regex = re.compile("(%s)" % "|".join(map(re.escape, dict.keys())))
    # For each match, look-up corresponding value in dictionary
    return regex.sub(lambda mo: dict[mo.string[mo.start():mo.end()]], text)


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    """builds speechlet"""
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
    """builds resopnse"""
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
