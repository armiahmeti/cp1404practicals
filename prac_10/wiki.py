"""Wikipedia search CLI using the 'wikipedia' package.

- Prompts user for a page title or search phrase until blank.
- On success: prints title, summary, URL.
- Handles DisambiguationError and PageError gracefully.
"""
from __future__ import annotations

try:
    import wikipedia  # type: ignore
except Exception as e:
    wikipedia = None  # type: ignore


def main() -> None:
    if wikipedia is None:
        print("The 'wikipedia' package is not installed. Install it first to use this program.")
        return

    while True:
        title = input("Enter page title: ").strip()
        if title == "":
            print("Thank you.")
            break
        try:
            # Try exact page first without autosuggest to avoid surprising redirects
            page = wikipedia.page(title, autosuggest=False)
            print(page.title)
            print(wikipedia.summary(page.title))
            print(page.url)
        except wikipedia.DisambiguationError as ex:  # type: ignore[attr-defined]
            print("We need a more specific title. Try one of the following, or a new search:")
            print(ex.options[:20])
        except wikipedia.PageError:  # type: ignore[attr-defined]
            print(f'Page id "{title}" does not match any pages. Try another id!')
        except Exception as ex:
            print(f"Unexpected error: {ex}")


if __name__ == "__main__":
    main()
