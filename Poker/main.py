import random
import numpy as np
from matplotlib import pyplot as plt

cards = list(range(0, 52))

possibilities = {"high_card": 0, "pair": 0, "two_pair": 0, "three_of_a_kind": 0, \
                 "straight": 0, "flush": 0, "full_house": 0, \
                  "four_of_a_kind": 0, "straight_flush": 0, "royal_flush": 0}

# returns color and value
def get_card(card):
  return (card//13, card%13)


def check_pair(cards):
  stored_values = {}
  for i in range(0, 14):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[1]] += 1

  return 2 in stored_values.values()

def check_two_pair(cards):
  stored_values = {}
  for i in range(0, 14):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[1]] += 1

  count = 0
  for i in range(0, 14):
    if(stored_values[i] == 2):
      count += 1
  
  return count == 2

def check_three_of_a_kind(cards):
  stored_values = {}
  for i in range(0, 14):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[1]] += 1

  return 3 in stored_values.values()

def check_four_of_a_kind(cards):
  stored_values = {}
  for i in range(0, 14):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[1]] += 1

  return 4 in stored_values.values()

def check_flush(cards):
  stored_values = {}
  for i in range(0, 4):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[0]] += 1

  count = 0
  for i in range(0, 4):
    if(stored_values[i] == 5):
      count += 1

  return count == 1

def check_full_house(cards):
  stored_values = {}
  for i in range(0, 14):
    stored_values[i] = 0

  for i in cards:
    stored_values[get_card(i)[1]] += 1

  return 3 in stored_values.values() and 2 in stored_values.values()

def check_straight(cards):
  numbers = list(map(lambda x: get_card(x)[1], cards))
  min_num = min(numbers)
  n = list(range(min_num, min_num+5))
  n.sort()
  numbers.sort()
  royal_straight = [1, 10, 11, 12, 9]
  royal_straight.sort()
  return set(n) == set(numbers) or numbers == royal_straight

def draw(card_list, how_many):
  cards = random.sample(card_list, how_many)
  if check_flush(cards):
    values = list(map(lambda card: get_card(card)[1], cards))
    values.sort()
    royal_straight = [1, 10, 11, 12, 9]
    royal_straight.sort()

    if values == royal_straight:
      possibilities["royal_flush"]
    elif check_straight(cards):
      possibilities["straight_flush"] += 1
    else:
      possibilities["flush"] += 1
  elif check_straight(cards):
      possibilities["straight"] += 1
  elif check_four_of_a_kind(cards):
    possibilities["four_of_a_kind"] += 1
  elif check_full_house(cards):
    possibilities["full_house"] += 1
  elif check_three_of_a_kind(cards):
    possibilities["three_of_a_kind"] += 1
  elif check_two_pair(cards):
    possibilities["two_pair"] += 1
  elif check_pair(cards):
    possibilities["pair"] += 1
  else:
    possibilities["high_card"] += 1
  
  
  
  

draws = 1000000

for i in range(draws):
  draw(cards, 5)

fig, ax = plt.subplots()

for key, value in possibilities.items():
  p = ax.bar(key, 100*value / draws, label=(str(100*value / draws) + " %"))
  ax.bar_label(p, label_type="edge")
  print(key, 100 * value / draws, "%")
plt.show()