"""Client code that reads languages.csv into ProgrammingLanguage objects and displays them."""
from programming_language import ProgrammingLanguage


def str_to_bool(s: str) -> bool:
    return s.strip().lower() in {"y", "yes", "true", "1"}


def load_languages(filename: str) -> list[ProgrammingLanguage]:
    languages: list[ProgrammingLanguage] = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()  # discard header
        for line in in_file:
            if not line.strip():
                continue
            name, typing, reflection, year, pointer = [p.strip() for p in line.split(",")]
            language = ProgrammingLanguage(
                name=name,
                typing=typing,
                reflection=str_to_bool(reflection),
                year=int(year),
                pointer_arithmetic=str_to_bool(pointer),
            )
            languages.append(language)
    return languages


def main():
    filename = "languages.csv"
    languages = load_languages(filename)
    print(f"Loaded {len(languages)} languages from {filename}")
    for lang in languages:
        print(f" - {lang}")

    print("\nDynamic languages:")
    for lang in languages:
        if lang.is_dynamic():
            print(f" * {lang.name}")

    print("\nLanguages with pointer arithmetic:")
    for lang in languages:
        if lang.supports_pointer_arithmetic():
            print(f" * {lang.name}")


if __name__ == "__main__":
    main()
