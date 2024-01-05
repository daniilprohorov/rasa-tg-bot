# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction


class ActionChangeSlotSetNull(Action):
    def name(self) -> Text:
        return "action_change_slot_set_null"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("change_slot", "not_set")]

class ActionRegisterFormSlotsReset(Action):
    def name(self) -> Text:
        return "action_register_form_slots_reset"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("engine_slot", None),
            SlotSet("transmission_slot", None),
            SlotSet("model_slot", None),
            SlotSet("photo_slot", None),
            SlotSet("register_form_filled_slot", False)]

class ActionRegisterFormFilledSlotTrue(Action):
    def name(self) -> Text:
        return "action_register_form_filled_slot_true"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("register_form_filled_slot", True)]

class ActionRegisterFormFilledSlotFalse(Action):
    def name(self) -> Text:
        return "action_register_form_filled_slot_false"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return [SlotSet("register_form_filled_slot", False)]

class ActionCheck(Action):
    def name(self) -> Text:
        return "action_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        metadata = tracker.latest_message
        print(tracker.current_state()['sender_id'])
        model = tracker.get_slot('model_slot')
        engine = tracker.get_slot('engine_slot')
        transmission = tracker.get_slot('transmission_slot')
        photo = tracker.get_slot('photo_slot')
        if model and engine and transmission and photo:
            return [FollowupAction("utter_all_params")]
        else:
            return [FollowupAction("utter_slots_null")]
