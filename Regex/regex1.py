import re
# 1. Question: Write a regular expression to match any string that starts with the letter "a" and is followed by exactly one character and then "b" (e.g., "axb", "a1b", "a b").

def Que1():
    pattern = "a.b"
    string = input("Enter the string  : ")
    result = re.findall(pattern,string)
    for i in result :
        print(i)
    return
#2. Question: Create a regular expression that matches strings that contain a sequence of digits, followed by a hyphen, and then more digits. For example, it should match "123-456", but not "123456" or "123-abc".
def Que2():
    pattern = "^\d+-\d+$"
    string = "123-456"
    result = re.search(pattern,string)
    print(result.group())
    
# 3. Question: Write a regular expression that matches any string containing a word that starts with "a" and ends with "z", with any number of characters (including zero) in between. The word must be at least two characters long (e.g., "abz", "applez").
def Que3():
    pattern = "a.+z"
    string = "abz"
    result = re.search(pattern,string)
    print(result.group())
#4. Question: Create a regular expression that matches a valid email address. The email should start with one or more letters, followed by the "@" symbol, and then a domain name with a dot and at least two characters (e.g., "test@example.com", "hello@domain.co").
def Que4():
    pattern = "^[a-zA-Z]+@[a-z]+.com"
    string = "saleemjibran813@gmail.com"
    result = re.search(pattern,string)
    if result:
        print(result.group())
    else:
        print("Not matched")
        
# 5. Question: Write a regular expression to match any string that contains a sequence of letters (lowercase or uppercase) followed by any number of spaces and ends with a digit. For example, it should match "abc 123", "XYZ 4", but not "abc123" or " 123".
def Que5():
    pattern = "^[a-zA-Z]+\s+\d+$"
    string = "abc 123"
    result = re.search(pattern,string)
    if result:
        print(result.group())
    else:
        print("Not matched")
    
# 6. Question: Write a regular expression to match any string that starts with a digit, followed by any number of alphanumeric characters (letters or digits), and ends with a special character (e.g., "!").


def Que6():
    pattern = "^[0-9]+\w+[!@#$%^&*]$"
    string = "9data%"
    result = re.search(pattern,string)
    if result:
        print(result.group())
        print("Matched")
    else:
        print("Not matched")
    
# 7. Question: Create a regular expression to match a valid phone number. The phone number should be in the format of (xxx) xxx-xxxx, where x is a digit (e.g., (123) 456-7890).

def Que7():
    pattern = "^\(\d{3}\) \d{3}-\d{4}$"
    string = "(123) 456-7890"
    result = re.search(pattern,string)
    if result:
        print(result.group())
        print("Matched")
    else:
        print("Not matched")
Que7()  

