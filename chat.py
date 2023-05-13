#intents => tags and input, response
from Intents import intents
import random

intent = intents
intent_num = len(intent) #4

occurence = 0
accuracy = []
ignore = [",",".",";","?","!"]



def process(input):
  global occurence
  global accuracy
  summ = 0

  words = input.split()
  accuracy = []
  for dataNum in range(0, intent_num):
    occurence = 0
    total = 0
    for word in words:
      for symbol in range(0,len(ignore)-1): #ignore specific symbols
        word = word.replace(ignore[symbol], '')
      for SepString in range(0, len(intent[dataNum][0])):
        total += 1
        if word in intent[dataNum][0][SepString].split():
          occurence += 1
          summ += 1
    if total == 0:
      accuracy.append(0.0)
    else:
      accuracy.append((occurence/total)*100) #calculate percentage instead of number of occurences
  print(accuracy)
  if summ == 0:
    return "Sorry, I don't quite understand you 🧐"
  else:
    return accuracy.index(max(accuracy))

def reply(text):
  accurate_response_num = process(text)
  if isinstance(accurate_response_num, int):
    response_list = intent[accurate_response_num][1]
  else:
    return accurate_response_num
  pick = random.randint(0,len(response_list)-1)
  return response_list[pick]