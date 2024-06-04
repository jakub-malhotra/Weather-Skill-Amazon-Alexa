# -*- coding: utf-8 -*-

""" 
This is the Weather Tool using the Alexa Skills Kit SDK for Python.
Created By: Jakub Malhotra
Created On: June 2024
"""

import logging
import ask_sdk_core.utils as ask_utils
import requests
import constants

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def get_weather_info():
    try:
        api_url = f"https://api.openweathermap.org/data/2.5/weather?lat={constants.LATITUDE}&lon={constants.LONGITUDE}&appid={constants.API_KEY}&units=metric"
        response = requests.get(api_url)
        response.raise_for_status()
        return response
    except requests.RequestException as error_code:
        logger.error(f"Error fetching weather data: {error_code}")
        return None

class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        speak_output = "Welcome to the Weather Tool Skill. You can ask me about the weather."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):
    """Handler for Hello World Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("HelloWorldIntent")(handler_input)

    def handle(self, handler_input):
        api_response = get_weather_info()
        if api_response:
            status_code = api_response.status_code
            speak_output = f"Hello World!, The API status code is {status_code}."
        else:
            speak_output = "Hello World!, There was an error fetching the weather information."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class WeatherIntentHandler(AbstractRequestHandler):
    """Handler for Weather Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("WeatherIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You triggered weather intent."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class TemperatureIntentHandler(AbstractRequestHandler):
    """Handler for Temperature Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("TemperatureIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You triggered temperature intent."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class ClothingIntentHandler(AbstractRequestHandler):
    """Handler for Clothing Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("ClothingIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You triggered clothing intent."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class MiscIntentHandler(AbstractRequestHandler):
    """Handler for Temperature Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("MiscIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You triggered miscellaneous intent."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )

class HelpIntentHandler(AbstractRequestHandler):
    """Handler for Help Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = "You can say hello to me! How can I help?"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    """Single handler for Cancel and Stop Intent."""
    def can_handle(self, handler_input):
        return (ask_utils.is_intent_name("AMAZON.CancelIntent")(handler_input) or
                ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input))

    def handle(self, handler_input):
        speak_output = "Goodbye!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class FallbackIntentHandler(AbstractRequestHandler):
    """Single handler for Fallback Intent."""
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("AMAZON.FallbackIntent")(handler_input)

    def handle(self, handler_input):
        logger.info("In FallbackIntentHandler")
        speech = "Hmm, I'm not sure. You can say Hello or Help. What would you like to do?"
        reprompt = "I didn't catch that. What can I help you with?"

        return handler_input.response_builder.speak(speech).ask(reprompt).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handler for Session End."""
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        # Any cleanup logic goes here.
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    """The intent reflector is used for interaction model testing and debugging.
    It will simply repeat the intent the user said. You can create custom handlers
    for your intents by defining them above, then also adding them to the request
    handler chain below.
    """
    def can_handle(self, handler_input):
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input):
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = f"You just triggered {intent_name}."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class CatchAllExceptionHandler(AbstractExceptionHandler):
    """Generic error handling to capture any syntax or routing errors. If you receive an error
    stating the request handler chain is not found, you have not implemented a handler for
    the intent being invoked or included it in the skill builder below.
    """
    def can_handle(self, handler_input, exception):
        return True

    def handle(self, handler_input, exception):
        logger.error(exception, exc_info=True)

        speak_output = "Sorry, I do not understand what you asked, please try again."

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

# The SkillBuilder object acts as the entry point for your skill, routing all request and response
# payloads to the handlers above. Make sure any new handlers or interceptors you've
# defined are included below. The order matters - they're processed top to bottom.

sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(WeatherIntentHandler())
sb.add_request_handler(TemperatureIntentHandler())
sb.add_request_handler(ClothingIntentHandler())
sb.add_request_handler(MiscIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(FallbackIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())
sb.add_request_handler(IntentReflectorHandler())  # make sure IntentReflectorHandler is last so it doesn't override your custom intent handlers

sb.add_exception_handler(CatchAllExceptionHandler())

lambda_handler = sb.lambda_handler()
