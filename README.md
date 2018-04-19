# Dot-Dot-Dot
[![Build Status](https://travis-ci.org/zarkle/Dot-Dot-Dot.svg?branch=master)](https://travis-ci.org/zarkle/Dot-Dot-Dot)

**Author**: Beverly Pham, Keith Eckert, Peter Kim, Andrii Glukhyi

**Version**: 0.1.0

## Overview
An Alexa Skill with an AWS Lambda function to query Wolfram Alpha through Amazon Echo Dot.

## Getting Started
1. Create an Alexa Skill using intents and sample utterances in `skill.json` and connect to your AWS Lambda function.
2. Create an AWS Lambda function using `lambda.py` and connect to your Alexa Skill. Make sure to use your own Wolfram Alpha appid also.
3. Test that it is working from the Alexa Skill web interface.
4. Add a function (`create_record_dynamodb`) to store reponse and request to Amazon DynamoDB in `lambda.py`.
5. Create and deploy Amazon Gateway API, uses another AWS Lambda function (`readDynamodb.py`) to return all queries and responses in json.
6. Connect to your Echo Dot and make sure it is working

## Architecture
- This application was written in Python 3
- Amazon Web Services Account
- Amazon Developer Account
- Wolfram Alpha API AppID

## API
1. Open your Alexa skill with your invocation name after triggering Alexa (ex: `open wolfman`)
2. Use your intent schema to ask a question (ex: `wolfman what is the population of Seattle`)
3. Point to https://dot-dot-dot-.herokuapp.com/ in your browser to view question and answer history

## Change Log
| Date | |
|:--|:--|
| 4-19-2018 | ___ |
| 4-18-2018 | Create and deploy AWS API Gateway, make front end and deploy on Heroku |
| 4-17-2018 | Connect Alexa Skill with AWS Lambda Function, Create DynamoDB  and connect to Lambda function |
| 4-16-2018 | Setup Alexa Skill |
| 4-15-2018 | Initial Scaffold |

## Resources
- gitignore.io
- coggle.it
- Wolfram Alpha API
- Amazon Alexa Skills Developer Kit
- Amazon DynamoDB
- Amazon API Gateway
- github.com/necolas/normalize.css
- Google Fonts
- coolors.co/
- github.com/n8henrie/alexa-wolfram-alpha
