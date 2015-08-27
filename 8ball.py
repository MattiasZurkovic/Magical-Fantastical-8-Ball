import time
import random
import sys
from sys import stdout

# List of responses
response = ['hi', 'bue']

def __init__():
    ask()

def ask():
    print('The Fanstical Magicical 8 Ball')
    time.sleep(0.25)
    question = input('Ask your question: ')
    time.sleep(0.25)
    print('Thinking')
    thinking(3)

    print(random.choice(response))
    time.sleep(0.25)
    again()

def again():
  ans = input('Ask again? (Y/N): ')
  if ans == 'Y':
    ask()
  elif ans == 'N':
    print('Thanks!')


def thinking(amount):
    i = 0
    while i <= amount:     
      i = i + 1  
      print('.')
      time.sleep(0.75)



__init__()
