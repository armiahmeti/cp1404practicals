from kivy.app import App
    from kivy.lang import Builder
    from kivy.uix.label import Label

    KV = """
BoxLayout:
    orientation: "vertical"
    padding: 10
    BoxLayout:
        orientation: "vertical"
        id: main
    """


    class DynamicLabelsApp(App):
        def build(self):
            self.title = "Dynamic Labels"
            root = Builder.load_string(KV)
            self._names = ["Armi", "Tim", "Rita", "Chris", "Zara"]
            for name in self._names:
                root.ids.main.add_widget(Label(text=name))
            return root


    if __name__ == "__main__":
        DynamicLabelsApp().run()
