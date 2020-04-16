#!/bin/python3

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lettersl = []
for l in letters:
  lettersl.append(l.lower())
letters = letters + lettersl
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10,1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {a:b for (a,b) in  zip(letters, points)}

# print(letter_to_points)

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for i in word:
    if i in letter_to_points:
      point_total += letter_to_points[i]
  return point_total

def play_word(player, word):
  player_to_words[player].append(word)


# Sadie SInk point
brownie_points = score_word("BROWNIE")
# print(brownie_points)

player_to_words = {
  "player1": ["BLUE", "TENNIS", "EXIT" ],
  "wordNerd":	[ "EARTH","EYES","MACHINE"],
   "Lexi Con": ["ERASER" ,"BELLY" ,"HUSKY"]	,
    "Prof Reader": ["ZAP","COMA","PERIOD"] }

player_to_points = {}

def update_points_total():
  for player,words in player_to_words.items():
    player_points = 0
    for wo in words:
      player_points +=  score_word(wo)
    player_to_points[player] = player_points

update_points_total()
# print(player_to_points)
play_word("Lexi Con", "DANCE")
# print(player_to_words)
update_points_total()  
  




