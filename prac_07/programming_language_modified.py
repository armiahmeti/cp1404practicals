
# programming_language.py

class ProgrammingLanguage:
    """Represents a programming language with various properties."""
    
    def __init__(self, name, typing, reflection, pointer_arithmetic=False):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic

    def __str__(self):
        pointer_support = "supports" if self.pointer_arithmetic else "does not support"
        return f"{self.name}, Typing: {self.typing}, Reflection: {self.reflection}, Pointer Arithmetic: {pointer_support}"

    def is_dynamic(self):
        """Check if the language is dynamically typed."""
        return self.typing.lower() == "dynamic"

# Sample usage for testing
if __name__ == "__main__":
    language = ProgrammingLanguage("Python", "Dynamic", True, False)
    print(language)
