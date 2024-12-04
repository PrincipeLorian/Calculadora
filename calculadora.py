from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class CalculatorApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_operator = None
        self.last_was_operator = False
        self.result = TextInput(font_size=32, readonly=True, halign="right", multiline=False)
        layout = GridLayout(cols=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '.', '0', 'C', '+'
        ]

        for button in buttons:
            layout.add_widget(Button(text=button, on_press=self.on_button_press))

        equals_button = Button(text='=', on_press=self.on_solution)
        layout.add_widget(self.result)
        layout.add_widget(Button(text=''))
        layout.add_widget(Button(text=''))
        layout.add_widget(equals_button)

        return layout

    def on_button_press(self, instance):
        current = self.result.text
        button_text = instance.text

        if button_text == 'C':
            self.result.text = ''
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == '' and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.result.text = new_text

        self.last_was_operator = button_text in self.operators
        self.last_operator = button_text

    def on_solution(self, instance):
        text = self.result.text
        if text:
            try:
                solution = str(eval(self.result.text))
                self.result.text = solution
            except Exception:
                self.result.text = 'Error'

if __name__ == '__main__':
    CalculatorApp().run()
