#!/usr/bin/python3.6

"""
Lambda
"""

import logging
from pprint import pprint

from animal_sounds import AnimalSound, BASE_URL, ANIMAL_SOUNDS, END_URL
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
import ask_sdk_core.utils as ask_utils

from ask_sdk_model import Response

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)


class LaunchRequestHandler(AbstractRequestHandler):
    "LaunchRequestHandler"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = (
            "Welcome, you can say Hello or Help. Which would you like to try?"
        )
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class AnimalSoundIntentHandler(AbstractRequestHandler):
    "AnimalSoundIntentHandler"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AnimalSoundIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        # slots = handler_input.request_envelope.request.intent.slots
        # animal_slot = slots["animal"]
        # animal = animal_slot.value
        # speak_output = (
        #     "<audio src='https://animal-sound-clips.s3.amazonaws.com/lion_01.mp3'/>"
        # )
        animal = AnimalSound(handler_input)
        return handler_input.response_builder.speak(animal.sound).response


class HelpIntentHandler(AbstractRequestHandler):
    "HelpIntentHandler"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AMAZON.HelpIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = "You can say hello to me! How can I help?"
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):
    "CancelOrStopIntentHandler"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name("AMAZON.CancelIntent")(
            handler_input
        ) or ask_utils.is_intent_name("AMAZON.StopIntent")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = "Goodbye!"
        return handler_input.response_builder.speak(speak_output).response


class SessionEndedRequestHandler(AbstractRequestHandler):
    "HANDLER"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        return handler_input.response_builder.response


class IntentReflectorHandler(AbstractRequestHandler):
    "HANDLER"

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type("IntentRequest")(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        intent_name = ask_utils.get_intent_name(handler_input)
        speak_output = "You just triggered " + intent_name + "."
        return handler_input.response_builder.speak(speak_output).response


class CatchAllExceptionHandler(AbstractExceptionHandler):
    "HANDLER"

    def can_handle(self, handler_input: HandlerInput, exception) -> bool:
        return True

    def handle(self, handler_input: HandlerInput, exception) -> Response:
        LOGGER.error(exception, exc_info=True)
        speak_output = "Sorry, I had trouble doing what you asked. Please try again."
        return (
            handler_input.response_builder.speak(speak_output)
            .ask(speak_output)
            .response
        )


SB = SkillBuilder()

SB.add_request_handler(LaunchRequestHandler())
# SB.add_request_handler(HelloWorldIntentHandler())
SB.add_request_handler(AnimalSoundIntentHandler())
SB.add_request_handler(HelpIntentHandler())
SB.add_request_handler(CancelOrStopIntentHandler())
SB.add_request_handler(SessionEndedRequestHandler())
SB.add_request_handler(IntentReflectorHandler())

SB.add_exception_handler(CatchAllExceptionHandler())

# MUST BE LOWERCASE OR AWS CAN NOT FIND IT
handler = SB.lambda_handler()
