# theword

Inspired by Python's `import this`, [*The Trashmen*](https://www.youtube.com/watch?v=aPrtFxd9u9Y), and [*The Family Guy*](https://www.youtube.com/watch?v=2WNrx2jq184), 
**theword** is quirky library to answer that eternal question, "What's the word?".

## Installation
TODO - Will use pip

## What's the word?
*Zen of Python*-style fun from any command line:
```sh
$ python -c "import theword"

Surfin' Bird, by The Trashmen

A well a everybody's heard about the bird
Bird, bird, bird, b-bird's the word
A well a bird, bird, bird, b-bird's the word
A well a bird, bird, bird, b-bird's the word
A well a bird, bird, b-bird's the word

```
## Using the word
You can import any of the following:
```python
from theword import TheWord, TheBird, what_is_the_word
```

Seeing the question:
```python
>>> TheWord().question
"What's the word?"
```

Asking the question (and seeing the answer):
```python
>>> what_is_the_word()
<theword.TheBird object at 0x10a77a290>   # Returns TheBird
>>> what_is_the_word().message
"Bird, bird, bird, b-bird's the word"
```

More quirky fun:
```python
# Fun with TheBird class
>>> b = TheBird()
>>> b.__dict__
{'released': 1964, 'message': "Bird, bird, bird, b-bird's the word", 'artist': 'The Trashmen', 'title': "Surfin' Bird"}
>>> b.play() # Hear the word
>>> b.celebrate() # Prepare to laugh

# TheWord inherets TheBird - everyone's heard this
>>> isinstance(TheWord(), TheBird)
True
>>> TheWord().__dict__
{'released': 1964, 'message': "Bird, bird, bird, b-bird's the word", 'artist': 'The Trashmen', 'question': "What's the word?", 'title': "Surfin' Bird"}
```
