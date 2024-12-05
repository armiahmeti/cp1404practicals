"""
CP1404/CP5632 Practical - Modified Language Profile Client Code.
Client code to demonstrate the LanguageProfile class functionality.
"""
from prac_06.modified_programming_language import LanguageProfile

def main():
    """Create and display information on various programming languages."""
    ruby = LanguageProfile("Ruby", "Dynamic", True, 1995)
    python = LanguageProfile("Python", "Dynamic", True, 1991)
    visual_basic = LanguageProfile("Visual Basic", "Static", False, 1991)

    languages = [ruby, python, visual_basic]
    print("Languages with dynamic typing are:")
    for lang in languages:
        if lang.is_dynamic():
            print(f"- {lang.language_name}")

if __name__ == "__main__":
    main()
