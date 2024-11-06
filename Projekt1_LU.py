"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lenka Urban
email: lenka.vondr@gmail.com
discord: @lenkavonurban
"""

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

uzivatele = {
  'bob': '123', 
  'ann': 'pass123', 
  'mike': 'password123', 
  'liz': 'pass123'
  }

delimiter = "-" * 40

username = input("username: ")
password = input("password: ")

print(delimiter)

if uzivatele.get(username) != password:
  print("unregistered user, terminating the program..")
  exit()

print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")

print(delimiter)

selected_text = input("Enter a number btw. 1 and 3 to select: ")
if not selected_text.isdigit() or int(selected_text) not in range(1, 4):
  print("Invalid number, terminating the program..")
  exit()

text_idx = int(selected_text) - 1
print(delimiter)

text = TEXTS[text_idx]
text_array = text.split()
word_count = len(text_array)

stats = {
  "titlecase": 0,
  "uppercase": 0,
  "lowercase": 0,
  "numeric": 0,
}

for word in text_array:
  if word.istitle():
    stats["titlecase"] += 1
  if word.isupper() and word.isalpha():
    stats["uppercase"] += 1
  if word.islower():
    stats["lowercase"] += 1
  if word.isdigit():
    stats["numeric"] += 1


print(f"There are {word_count} words in the selected text.")

for key, value in stats.items():
  if key == "numeric":
    print(f"There are {value} numeric strings.")
  else:
    print(f"There are {value} {key} words.")

print(f"The sum of all the numbers {sum(int(word) for word in text.split() if word.isdigit())}.")

print(delimiter)

frequency = {}
for word in text.split():
  word = len(word.strip(",."))
  frequency[word] = frequency.get(word, 0) + 1

sorted_frequency = dict(sorted(frequency.items()))

print("LEN ".center(4) + "|" + "OCCURENCIES".center(30) + "|" " NR.".center(4))
print(delimiter)

for word, count in sorted_frequency.items():
  print(f"{str(word).rjust(3)} | {('*' * count).ljust(28)} |{str(count).rjust(3)} ")