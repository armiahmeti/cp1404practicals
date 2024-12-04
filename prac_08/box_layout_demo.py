"""
CP1404/CP5632 Practical
Modified Box Layout Demo with Greet and Clear functionality.
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemoApp(App):
    """Kivy App for demonstrating Box Layout with added features."""

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Box Layout Demo - Enhanced"
        self.root = Builder.load_file('box_layout_demo.kv')
        return self.root

    def handle_greet(self):
        """Greet the user by name."""
        name = self.root.ids.input_name.text
        self.root.ids.output_label.text = f"Hello {name}"

    def handle_clear(self):
        """Clear the input and output fields."""
        self.root.ids.input_name.text = ""
        self.root.ids.output_label.text = ""


if __name__ == '__main__':
    BoxLayoutDemoApp().run()
