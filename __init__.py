from mycroft import MycroftSkill, intent_file_handler
import glob
import pathlib
import subprocess


class Fortune(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        super().__init__()
        self.learning = True

    @intent_file_handler('fortune.intent')
    def handle_fortune_intent(self, message):
        specific = message.data.get('specific', None)
        if specific is None:
            fortune = subprocess.check_output(["fortune"])
        else:
            fortune = subprocess.check_output(["fortune", specific.replace(' ', '-')])
        for line in fortune.strip().decode().splitlines():
            self.speak_dialog(line)


    @intent_file_handler('listfortunes.intent')
    def handle_listfortunes_intent(self, message):
        for i in glob.glob("/usr/share/fortune/*.dat"):
            self.speak_dialog(pathlib.Path(i).stem)


def create_skill():
    return Fortune()

