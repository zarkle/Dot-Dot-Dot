![alt text](random_from_andrii/alexa_skills_kit_architecture_diagram-620x350.png "Alexa")

1)

The user speaks to Echo, using trigger words so that Echo knows that it is being addressed, and identifies the Skill that the user wishes to interact with. For example, “Alexa, ask BART when are the trains from Balboa Park”. In this case, “Alexa” is the trigger word to make the Echo listen, and “BART” identifies the skill that the user wants to direct their enquiry to.


2)

Echo sends the request to the Alexa Service Platform, which handles speech recognition, turning the user’s speech into tokens identifying the “intent” and any associated contextual parameters. In our example, the “intent” would be that the user wants to know about train times, and the context for that would be that they are interested specifically in train times for the Balboa Park station. Intents, and possible parameter values for them are held by the Alexa Service Platform as configuration items for the Skill.

3)

The intent and parameters for the user’s request are then sent as a JSON encoded text document to the server side Skill implementation for processing. The Alexa Service Platform knows where to send these requests as it maintains a set of backend URLs - Wolfram Alpha API

4)

Wolfram Alpha API receives the JSON via a HTTPs request. Parses the JSON, reading the intent and context, and then performs suitable processing to retrieve data

5)

A response JSON document is then sent back to the Alexa Service Platform containing both the text that Alexa should speak to the user and markup containing text and an optional image URL for a “card” that appears in the Alexa app.

6)

The Alexa Service Platform receives the response, and uses text to speech to speak the response to the user whilst also pushing a card to the companion app.

For this example, we’re going to use an AWS Lambda function for our Custom Skill logic, and we’ll implement that logic in Python. This saves us the overhead of setting up our own server to host and run the skill, avoids the requirement to obtain an SSL certificate for our server, and allows us to benefit from the auto scaling features of AWS Lambda should our skill become popular and receive a lot of traffic from Echo owners.


