from kivy.app import App
    from kivy.lang import Builder


    KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: self.minimum_height
        spacing: 10
        Button:
            text: "Clear"
            on_press: app.handle_clear()
        TextInput:
            id: input_name
            text: ""
            multiline: False
        Button:
            text: "Greet"
            on_press: app.handle_greet()

    Label:
        text: "Enter your name"
        color: (1, 1, 0, 1)

    Label:
        id: output_label
        text: ""
    """


    class BoxLayoutDemoApp(App):
        def build(self):
            self.title = "BoxLayout Demo (Greet/Clear)"
            return Builder.load_string(KV)

        def handle_greet(self):
            name = self.root.ids.input_name.text.strip()
            self.root.ids.output_label.text = f"Hello {name}" if name else ""

        def handle_clear(self):
            self.root.ids.input_name.text = ""
            self.root.ids.output_label.text = ""


    if __name__ == "__main__":
        BoxLayoutDemoApp().run()
