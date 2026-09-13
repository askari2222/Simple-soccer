from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button


class DrawCheckerApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        title = Label(
            text='Draw Pattern Checker',
            font_size='24sp',
            size_hint_y=0.2
        )
        layout.add_widget(title)

        info = Label(
            text='App is running!\n\nYour Kivy Android app works!',
            font_size='16sp'
        )
        layout.add_widget(info)

        return layout


if __name__ == '__main__':
    DrawCheckerApp().run()