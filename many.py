from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
import string
import secrets

class CyberYKS(App):

    def build(self):
        Window.clearcolor = (0.04, 0.02, 0.10, 1)

        layout = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        self.title = Label(
            text="CYBERYKS",
            font_size=32,
            color=(0.7, 0.4, 1, 1)
        )
        layout.add_widget(self.title)

        layout.add_widget(Label(
            text="CYBER SECURITY TOOL V1"
        ))

        self.password = TextInput(
            hint_text="Enter sample password",
            password=True,
            multiline=False,
            size_hint_y=None,
            height=50
        )
        layout.add_widget(self.password)

        check = Button(
            text="CHECK PASSWORD",
            size_hint_y=None,
            height=50
        )
        check.bind(on_press=self.check_password)
        layout.add_widget(check)

        self.result = Label(text="Security Report")
        layout.add_widget(self.result)

        generate = Button(
            text="GENERATE PASSWORD",
            size_hint_y=None,
            height=50
        )
        generate.bind(on_press=self.generate)
        layout.add_widget(generate)

        self.generated = Label(text="Generated password")
        layout.add_widget(self.generated)

        return layout

    def check_password(self, instance):
        p = self.password.text

        if not p:
            self.result.text = "Enter a password first"
            return

        score = sum([
            len(p) >= 8,
            any(c.islower() for c in p),
            any(c.isupper() for c in p),
            any(c.isdigit() for c in p),
            any(c in string.punctuation for c in p)
        ])

        level = (
            "WEAK" if score <= 2 else
            "MEDIUM" if score <= 3 else
            "STRONG"
        )

        self.result.text = (
            f"STRENGTH: {level}\n"
            f"SCORE: {score}/5"
        )

    def generate(self, instance):
        chars = string.ascii_letters + string.digits + "!@#$%"
        password = "".join(
            secrets.choice(chars) for _ in range(16)
        )
        self.generated.text = password


if __name__ == "__main__":
    CyberYKS().run()
