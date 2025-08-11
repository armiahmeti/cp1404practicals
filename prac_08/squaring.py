from kivy.app import App
    from kivy.lang import Builder
    from kivy.properties import StringProperty


    KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    # Top section: input, button, output arranged left-to-right
    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        TextInput:
            id: input_number
            text: ""
            multiline: False
            input_filter: "int"
        Button:
            text: "Square"
            on_press: app.handle_calculate(input_number.text)
        Label:
            id: output_label
            text: app.output_text
            color: (1, 0.4, 0.7, 1)  # pink

    # Bottom section: instruction label
    BoxLayout:
        orientation: "horizontal"
        size_hint_y: None
        height: self.minimum_height
        Label:
            text: "Enter a number and press \"Square\"."
    """


    class SquaringApp(App):
        output_text = StringProperty("")

        def build(self):
            self.title = "Squaring App (Modified)"
            return Builder.load_string(KV)

        def handle_calculate(self, text_value: str):
            try:
                number = int(text_value)
            except (TypeError, ValueError):
                self.output_text = "0"
                return
            self.output_text = str(number * number)


    if __name__ == "__main__":
        SquaringApp().run()
