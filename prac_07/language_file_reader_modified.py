
# language_file_reader.py

from programming_language import ProgrammingLanguage

def main():
    languages = load_languages()
    display_languages(languages)

def load_languages(filename="languages.csv"):
    """Load languages from a CSV file."""
    languages = []
    with open(filename, "r") as file:
        file.readline()  # Skip the header
        for line in file:
            parts = line.strip().split(',')
            reflection = parts[2].lower() == 'yes'
            pointer_arithmetic = parts[3].lower() == 'yes'
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic)
            languages.append(language)
    return languages

def display_languages(languages):
    """Display all loaded languages."""
    print("Programming Languages:")
    for language in languages:
        print(language)

if __name__ == "__main__":
    main()
