# String Pattern Analyzer

# Get input string from the user
text = input("Enter a text string: ")

# 1️ Character frequency count (case-insensitive)
char_freq = {}
for char in text.lower():
    if char != " ":  # ignoring spaces in frequency
        char_freq[char] = char_freq.get(char, 0) + 1

# 2️ Word count
words = text.split()
word_count = len(words)

# 3️ Most common character (excluding spaces)
if char_freq:
    most_common_char = max(char_freq, key=char_freq.get)
else:
    most_common_char = None

# 4️ Palindrome check (ignoring spaces and case)
cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
is_palindrome = cleaned_text == cleaned_text[::-1]

# 5️ Reverse the string
reversed_text = text[::-1]

# Display results
print("\n== String Analysis Results ==")
print(f"Original string: {text}")
print(f"Character frequency (case-insensitive, spaces excluded): {char_freq}")
print(f"Word count: {word_count}")
print(f"Most common character (excluding spaces): {most_common_char}")
print(f"Is palindrome: {'Yes' if is_palindrome else 'No'}")
print(f"Reversed string: {reversed_text}")
