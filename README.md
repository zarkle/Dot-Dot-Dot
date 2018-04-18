# Dot-Dot-Dot
[![Build Status](https://travis-ci.org/zarkle/Dot-Dot-Dot.svg?branch=master)](https://travis-ci.org/zarkle/Dot-Dot-Dot)

**Author**: Beverly Pham, Keith Eckert, Peter Kim, Andrii Glukhyi

**Version**: 0.1.0

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
An Alexa Skill with an AWS Lambda function to query Wolfram Alpha through Amazon Echo Dot.

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
- Amazon Web Services Account
- Amazon Developer Account
- Wolfram Alpha API AppID

## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
1. Create an Alexa Skill using intents and sample utterances in `skill.json` and connect to your AWS Lambda function.
2. Create an AWS Lambda function using `lambda.py` and connect to your Alexa Skill. Make sure to use your own Wolfram Alpha appid also.
3. Test that it is working from the Alexa Skill web interface
4. Connect to your Echo Dot and make sure it is working

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
1. Open your Alexa skill with your invocation name after triggering Alexa (ex: `open wolfman`)
2. Use your intent schema to ask a question (ex: `wolfman what is the population of Seattle`)

## Change Log
| Date | |
|:--|:--|
| 4-20-2018 | Complete |
| 4-19-2018 | ___ |
| 4-18-2018 | ___ |
| 4-17-2018 | Connect Alexa Skill with AWS Lambda Function, set up DynamoDB |
| 4-16-2018 | Setup Alexa Skill |
| 4-15-2018 | Initial Scaffold |

## Resources
- gitignore.io
- coggle.it
- Wolfram Alpha API
- Amazon Alexa Skills Developer Kit
- github.com/necolas/normalize.css
- Google Fonts
- https://coolors.co/
- https://github.com/n8henrie/alexa-wolfram-alpha
