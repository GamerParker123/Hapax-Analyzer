from collections import Counter
import re
import matplotlib.pyplot as plt

def analyze_hapaxes(filepath):
    # Load and preprocess text
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read().lower()

    # Tokenize words
    words = re.findall(r'\b\w+\b', text)

    # Initialize data for plotting
    hapax_rates = []
    seen_counts = Counter()

    # Iterate through the words, updating counts and computing hapax rate
    for i, word in enumerate(words):
        seen_counts[word] += 1
        hapaxes = sum(1 for count in seen_counts.values() if count == 1)
        hapax_rate = hapaxes / (i + 1)
        hapax_rates.append(hapax_rate)

    # Plot the hapax rate over the progression of the text
    plt.figure(figsize=(14, 6))
    plt.plot(hapax_rates, color='blue', linewidth=1)
    plt.title("Hapax Legomena Rate Over Journal Progression")
    plt.xlabel("Word Index")
    plt.ylabel("Hapax Rate")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# PUT FILE HERE
analyze_hapaxes('Thought Journal.txt')