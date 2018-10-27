# Language Generator

## Markov chains

- takes an event and what probably comes next
- accuracy can possibly be added in predicting probability of series of events as opposed to one event. likely only possible for longer series.
- **Part of speech tagging** can likely give more information around each event in Markov chain so predictions next event can either be a specific word or a part of speech. 

Prospective model for best next choice.
```
event 
  what are the most likely next words?
  what are the most likely next parts of speech? (mad libs)
    what is their intersection?
```

Approach

1. Basic one file proof of concept
1. 1 small text, process, next word
1. 2 small texts, process, next word
1. 5 small texts, process, classify, next part of speech
1. 5 small texts, process, classify, next next part of speech
1. 1 large text, process, classify, [next word, next next word, next next part of speech, next part of speech]

Other things to think about:
module pattern https://docs.python.org/3/tutorial/modules.html
testing framework https://docs.python-guide.org/writing/tests/
concurrency https://www.blopig.com/blog/2016/08/processing-large-files-using-python/


Possible version 2 taking it into JavaScript and the browser with workers

