import time
import random
import sys
from sys import stdout

# List of responses
response = ["Yes, most definitely!", "The chances are high!", "Not likely!", "May the odds be ever in your favor.",
                        "You got no shot, kid.", "Try it out and see!", "23% of working", "99.9% success rate",
                        "Congratulations, yes!", "Ask a probably question," "Ask again later", "Better not tell you now",
           "Cannot predict now", "Concentrate and ask again", "Don't count on it"]

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
