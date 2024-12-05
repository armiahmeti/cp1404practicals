
import wikipedia

def fetch_wikipedia_page():
    """Prompt user for a Wikipedia page and print details."""
    while True:
        title = input("Enter page title: ").strip()
        if not title:
            print("Exiting program.")
            break
        try:
            page = wikipedia.page(title)
            print(f"Title: {page.title}\nSummary: {page.summary[:500]}\nURL: {page.url}")
        except wikipedia.DisambiguationError as e:
            print(f"Disambiguation required: {e.options[:5]}")
        except wikipedia.PageError:
            print("Page not found. Try again.")

fetch_wikipedia_page()
