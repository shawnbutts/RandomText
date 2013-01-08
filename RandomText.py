import sublime_plugin
import sublime
import string
import random


class RandomTextGenerateCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        name = self.view.settings().get("random_text_charset", 'printable')
        length = self.view.settings().get("random_text_length", 32)
        text = self.charset(name, length)
        self.view.insert(edit, self.view.sel()[0].begin(), text)

    def charset(self, name, length):
        if (name == 'printable'):
            # Printable string without whitespace or quotations
            chars = string.printable.translate(None, string.whitespace + '\'"')
        elif (name == 'alphanumeric'):
            chars = string.letters + string.digits
        elif (name == 'letters'):
            chars = string.letters
        elif (name == 'digits'):
            chars = string.digits
        else:
            chars = name

        # Generate and concatenate random characters from the charset
        charset = ''.join(random.SystemRandom().choice(chars) for i in xrange(length))

        return charset


class SetRandomTextCharsetCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Charset:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        line = str(text)
        self.window.active_view().settings().set("random_text_charset", line)


class SetRandomTextLengthCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_input_panel("Text Length:", "", self.on_done, None, None)
        pass

    def on_done(self, text):
        line = int(text)
        self.window.active_view().settings().set("random_text_length", line)