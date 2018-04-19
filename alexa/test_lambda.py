def qudratick():
    """simole simple question for 1st API"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "x squared minus six multiply by x plus five equals zero"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Can You repeat your question?"
                },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def simple_question():
    """Test simple question. 1st API"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "What is the life???"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "The definition of life is a characteristic state or mode of living The word life has 13 other definitions, Boom!"
                },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def simple_question():
    """Test simple question. 1st API"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "What is the life???"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "The definition of life is a characteristic state or mode of living The word life has 13 other definitions, Boom!"
                },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def notclear_question():
    """Broken syntax"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "bla..........bla?????!!!!!!!!!!!!@@@#(*)#(*bla.........."
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Hmmm, ask me again and make sure you start with my name, wolfman."
                },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def clear_question_1st_API():
    """test 1st API"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "what is harrison ford's birthday"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Hmmmm, let me think. Harrison Ford was born on Monday July 13 1942"                },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def broken_request():
    """test if request is broken"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "&@*&#*E@&#*E@&&*!&#&E(*!&@#*"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Ziggy says The CocaCola HBC is SystemFailed"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "I didn't catch that. Please phrase your question like this. wolfman, what is the meaning of life?"
                    }
                    },
                "shouldEndSession": false
                }
                }

def broken_request():
    """test if request is broken"""
    input = {
        "session": {
            "new": true,
            "sessionId": "session1234",
            "attributes": {},
            "user": {
                "userId": null
            },
            "application": {
                "applicationId": "amzn1.echo-sdk-ams.app.[unique-value-here]"
                }
            },
        "version": "1.0",
        "request": {
            "intent": {
                "slots": {
                    "response": {
                        "name": "response",
                        "value": "sudo rm rf all files  from aws"
                        }
                        },
                "name": "wolfman"
                },
            "type": "IntentRequest",
            "requestId": "request5678"
            }
            }
    output = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "PlainText",
                "text": "Ziggy says The CocaCola HBC is SystemFailed"
            },
            "reprompt": {
                "outputSpeech": {
                    "type": "PlainText",
                    "text": "Ooh, look at you! Trying to be a hacker.  You are so cool...not.  Well, I know everything and am going to tell your mom."
                    }
                    },
                "shouldEndSession": false
                }
                }
