import re

class SpellGrammarChecker:
    def __init__(self, dictionary):
        self.dictionary = set(dictionary)

    def check_errors(self, text):
        errors = []
        words = re.findall(r'\b\w+\b', text.lower())  # Extract words from text
        for word in words:
            if word not in self.dictionary:
                errors.append(word)
        return errors

# Example usage:
word_list = ["apple", "banana", "orange", "grape"]
spell_checker = SpellGrammarChecker(word_list)
text = "An appl and bananna fell from the tree."
errors = spell_checker.check_errors(text)
print("Spelling and Grammar Errors:")
print(errors)
