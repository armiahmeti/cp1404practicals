from kivy.app import App
    from kivy.lang import Builder
    from kivy.properties import StringProperty

    MILES_TO_KM = 1.60934

    KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    BoxLayout:
        orientation: "horizontal"
        spacing: 10
        Button:
            text: "Up"
            on_press: app.handle_increment(1)
        TextInput:
            id: miles_input
            text: ""
            multiline: False
            on_text: app.handle_text_change(self.text)
            input_filter: "float"
        Button:
            text: "Down"
            on_press: app.handle_increment(-1)

    # Convert button intentionally commented out per stage 2 instruction
    # Button:
    #     text: "Convert"
    #     on_press: app.handle_convert()

    Label:
        id: output_label
        text: app.km_text
    """


    class MilesToKmApp(App):
        km_text = StringProperty("0.0 km")

        def build(self):
            self.title = "Miles to Kilometres"
            return Builder.load_string(KV)

        def _get_current_miles(self) -> float:
            text = self.root.ids.miles_input.text.strip()
            try:
                return float(text)
            except (TypeError, ValueError):
                return 0.0

        def _update_output(self, miles: float):
            km = miles * MILES_TO_KM
            self.km_text = f"{km:.3f} km"

        def handle_convert(self):
            self._update_output(self._get_current_miles())

        def handle_text_change(self, _text: str):
            self.handle_convert()

        def handle_increment(self, delta: int):
            miles = self._get_current_miles()
            miles += delta
            self.root.ids.miles_input.text = str(int(miles) if miles.is_integer() else miles)
            self.handle_convert()


    if __name__ == "__main__":
        MilesToKmApp().run()
