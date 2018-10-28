import index as markov
def main():
  """
  Do Markov stuff
  """
  model = markov.prepare_data([
    'This is the first line.',
    'This is the second line.  It has another line after it as well.',
    'Which line is this? It\'s the third line of course. ',
    'This is boring.',
    'No one invited you.',
    'Hey 7, why am I so afraid of you?',
    'BECAUSE I ATE 9!!!',
    '',
    'What happend to 9? Oh... 7 ate him. I get the joke...I think.',
    'What kind of "joke" is this?'
  ])
  
  print(markov.generate(model))
  print(markov.generate(model))
  print(markov.generate(model))

if __name__ == '__main__':
    main()