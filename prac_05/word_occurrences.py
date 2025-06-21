"""
Word Occurrences
Estimate: 20 minutes
Actual: 25 minutes
"""

def main():
    word_counts = {}
    user_text = input("Text: ")
    words = user_text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_length = max((len(w) for w in word_counts))
    for word in sorted(word_counts):
        print(f"{word:{max_length}} : {word_counts[word]}")

main()