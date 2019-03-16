from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
import requests
import urllib.request
import ssl
__author__ = 'denibademi'

LOGGER = getLogger(__name__)

class TodayHistorySkill(MycroftSkill):

    def __init__(self):
        super(TodayHistorySkill, self).__init__(name="TodayHistorySkill")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        random_event_intent = IntentBuilder("RandomEventIntent").\
            require("RandomEventKeyword").build()
        self.register_intent(random_event_intent, self.handle_first_lamp_on_intent)
        
        random_event_intent2 = IntentBuilder("RandomEventIntent2").\
            require("secondLightKeyword").build()
        self.register_intent(random_event_intent2, self.handle_second_lamp_on_intent)
        
        #random_event_intent3 = IntentBuilder("RandomEventIntent3").\
       #     require("RandomEventKeyword2").build()
       # self.register_intent(random_event_intent3, self.handle_first_lamp_off_intent)
        
       # random_event_intent4 = IntentBuilder("RandomEventIntent4").\
       #    require("secondLightKeyword2").build()
       # self.register_intent(random_event_intent4, self.handle_second_lamp_off_intent)

    def handle_first_lamp_on_intent(self, message):
        url="https://10.106.0.225/lamp1/1"
        r = urllib.request.urlopen("https://10.106.0.225/lamp1/1", context=ssl.SSLContext()).read()
        self.speak("As you wish") 
    
    def handle_second_lamp_on_intent(self, message):
        url="https://10.106.7.2/lamp2/1"
        r = urllib.request.urlopen("https://10.106.7.2/lamp2/1", context=ssl.SSLContext()).read()
        self.speak("As you wish") 
        
   # def handle_first_lamp_off_intent(self, message):
  #      url="https://10.106.0.225/lamp1/0"
  #      r = urllib.request.urlopen("https://10.106.0.225/lamp1/0", context=ssl.SSLContext()).read()
 #       self.speak("As you wish") 
    
#    def handle_second_lamp_off_intent(self, message):
   #     url="https://10.106.7.2/lamp2/0"
 #       r = urllib.request.urlopen("https://10.106.7.2/lamp2/0", context=ssl.SSLContext()).read()
 #       self.speak("As you wish")

    def stop(self):
        pass

def create_skill():
    return TodayHistorySkill()
