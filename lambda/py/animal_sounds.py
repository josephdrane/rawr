from ask_sdk_core.handler_input import HandlerInput

BASE_URL = "<audio src='https://animal-sound-clips.s3.amazonaws.com/"

ANIMAL_SOUNDS = {
    "bat": "bat_01.mp3",
    "dog": "dog_01.mp3",
    "hedgehog": "hedgehog_01.mp3",
    "whale": "humpback-whale_01.mp3",
    "leopard": "leopard_01.mp3",
    "lion": "lion_01.mp3",
    "owl": "owl_01.mp3",
    "pig": "pig_01.mp3",
    "raccoon": "raccoon_01.mp3",
    "robin": "robin_01.mp3",
    "turkey": "turkey_01.mp3",
}

END_URL = "'/>"


class AnimalSound:
    def __init__(self, handler_input: HandlerInput):
        slots = handler_input.request_envelope.request.intent.slots
        animal_slot = slots["animal"]
        animal = animal_slot.value
        self.sound = f"{BASE_URL}{ANIMAL_SOUNDS[animal]}{END_URL}"
