from mycroft import MycroftSkill, intent_file_handler


class Fortune(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fortune.intent')
    def handle_fortune(self, message):
        self.speak_dialog('fortune')


def create_skill():
    return Fortune()

