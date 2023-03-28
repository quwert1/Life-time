from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
	def build(self):
		self.solution = TextInput()
		return Button(text="Hello")


if __name__ == '__main__':
	MainApp().run()