import re

# Match any string that contains exactly three digits.
def Que1():
    pattern = r"\d{3}"  # Raw string to avoid escaping backslashes
    string = "abc123xyz, a1b2c, 4567"
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")

# Extract all words that start with a capital letter from a text.
# Input: "The Quick Brown Fox jumps Over the Lazy Dog"
def Que2():
    pattern = r"\b[A-Z][a-z]*"  # Raw string to avoid escaping backslashes
    string = "The Quick Brown Fox jumps Over the Lazy Dog"
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")
# Identify all email addresses from a given string.
# Input: "Contact us at support@example.com or sales@domain.org"
def Que3():
    pattern = r"[a-zA-Z]+@[a-zA-Z]+\.[a-z]{3}"  # Raw string to avoid escaping backslashes
    string = "Contact us at support@example.com or sales@domain.org"
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")
# Capture the year, month, and day from dates in the format YYYY-MM-DD.
# Input: "Today's date is 2024-08-30, and yesterday was 2024-08-29."
def Que4():
    pattern = r"\d{4}-\d{2}-\d{2}"  # Raw string to avoid escaping backslashes
    string = "Today's date is 2024-08-30, and yesterday was 2024-08-29."
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")
# Extract the domain name from a URL.
# Input: "Visit our website at https://www.example.com or http://blog.site.org"
def Que5():
    pattern = r"https?://[a-zA-Z0-9]+\.[a-zA-Z]+\.[a-z]{3,}"  # Raw string to avoid escaping back/slashes
    string = "Visit our website at https://www.example.com or http://blog.site.org."
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")
# Identify and group all words that start and end with the same letter.
# Input: "Level, Radar, noon, Apple, banana"        
def Que6():
    string = "Level, Radar, noon, Apple, banana"
    pattern = r"^\b([a-zA-Z])*\1\$" 
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")
# Finding All Hashtags in a Text
# Write a Python program that finds all hashtags (words starting with a # symbol) in a given string of text. The hashtag can contain letters, numbers, and underscores but cannot contain spaces or special characters other than the # symbol. The program should return a list of unique hashtags found in the text.
def Que7():
    pattern = r"#[a-zA-z0-9_]+"
    string = "Follow us on #Instagram for daily updates! Don't miss out on #fitness_tips and #health_goals."
    ans = re.findall(pattern, string)  # Find all matches of the pattern
    if ans:
        for match in ans:
            print(match)
    else:
        print("Not matched")