class AutoSuggester:
    def __init__(self, words):
        self.words = set(words)
    def get_suggestions(self, prefix):
        suggestions = []
        for word in self.words:
            if word.startswith(prefix):
                suggestions.append(word)
        return suggestions

# Example usage:
word_list = ["apple", "banana", "apricot", "orange", "grape"]
autosuggester = AutoSuggester(word_list)
prefix = "ap"
suggestions = autosuggester.get_suggestions(prefix)
print("Suggestions for prefix '{}':".format(prefix))
print(suggestions)