theword
=======

.. image:: https://travis-ci.org/JimHaughwout/theword.svg?branch=master
    :target: https://travis-ci.org/JimHaughwout/theword

Inspired by Python's ``import this``, `The
Trashmen <https://www.youtube.com/watch?v=aPrtFxd9u9Y>`__, and `The
Family Guy <https://www.youtube.com/watch?v=2WNrx2jq184>`__, **theword**
is a quirky library to answer that eternal question, "What's the word?"

Installation
------------
From any command line:

.. code:: sh

    $ pip install theword

Emulating the Zen of Python
---------------------------

From any command line: 

.. code:: sh

    $ python -c "import theword"

    _Surfin' Bird_, by The Trashmen

    A well a everybody's heard about the bird
    Bird, bird, bird, b-bird's the word
    A well a bird, bird, bird, b-bird's the word
    A well a bird, bird, bird, b-bird's the word
    A well a bird, bird, b-bird's the word

General Usage
-------------

You can import any of the following:

.. code:: python

    from theword import TheWord, TheBird, what_is_the_word

Ask the question:

.. code:: python

    >>> what_is_the_word()
    <theword.theword.TheBird object at 0x10f582d90>   # Returns TheBird
    >>> what_is_the_word().answer
    '[E]verybody knows that the bird is the word!'
    >>> print what_is_the_word()  # We overloaded __str__
    {"answer": "[E]verybody knows that the bird is the word!", "question": "What's the word?", "id": "The Bird"}

More quirky fun:

.. code:: python

    >>> what_is_the_word().play()  # Turn on the volume, ensure your WiFi is on
    {'artist': 'The Trashmen', 'title': "Surfin' Bird", 'question': "What's the word?", 'released': 1964, 'answer': '[E]verybody knows that the bird is the word!', 'id': 'The Bird'}
    >>> what_is_the_word().celebrate() # Be prepared to laugh
    {'answer': '[E]verybody knows that the bird is the word!', 'celebrated_on': "FOX's The Family Guy", 'question': "What's the word?", 'id': 'The Bird', 'celebrated_by': 'Seth MacFarlane'}
    >>>

If you watch all the skits you will recognize this:

    Sir, our math shows that the Bird is greater than or equal to the
    Word!

.. code:: python

    >>> isinstance(TheBird(), TheWord)
    True
    >>> issubclass(TheBird, TheWord)
    True

.. |Build Status| image:: https://travis-ci.org/geopy/geopy.svg?branch=master
   :target: https://travis-ci.org/JimHaughwout/theword.svg?branch=dev
