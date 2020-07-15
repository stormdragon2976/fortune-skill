from mycroft import MycroftSkill, intent_file_handler
import subprocess


class Fortune(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        super().__init__()
        self.learning = True

    @intent_file_handler('fortune.intent')

    def handle_fortune_intent(self, message):
        fortune = subprocess.check_output(["fortune"])
        for line in fortune.strip().decode().splitlines():
            self.speak_dialog(line)


def create_skill():
    return Fortune()

