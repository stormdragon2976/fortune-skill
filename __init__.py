# Copyright (C) 2020 Storm Dragon

# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:

# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


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
            try:
                fortune = subprocess.check_output(["fortune", specific.replace(' ', '-')])
            except:
                self.speak_dialog("No " + specific + " fortunes found.")
                return
        for line in fortune.strip().decode().splitlines():
            self.speak_dialog(line)


    @intent_file_handler('listfortunes.intent')
    def handle_listfortunes_intent(self, message):
        fortuneList = ""
        # Fortunes are in different directories for different distros.
        if os.path.exists("/usr/share/fortune"):
            fortunePath = "/usr/share/fortune"
        elif os.path.exists("/usr/share/games/fortunes"):
            fortunePath = "/usr/share/games/fortunes"
        for i in glob.glob(fortunePath + "/*.dat"):
            fortuneList += pathlib.Path(i).stem + ", "
        fortuneList = fortuneList[:-2]
        fortuneList = ', and '.join(fortuneList.rsplit(', ', 1))
        self.speak_dialog(fortuneList)


def create_skill():
    return Fortune()

