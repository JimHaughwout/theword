"""
Inspired by 'import this' and The Trashmen
Answering the eterinal question of "What is the word?"
"""

import webbrowser

# Show console users that the bird is the word
# Just like `import this`

print """_Surfin'_Bird_, by The Trashmen

A well a everybody's heard about the bird
Bird, bird, bird, b-bird's the word
A well a bird, bird, bird, b-bird's the word
A well a bird, bird, bird, b-bird's the word
A well a bird, bird, b-bird's the word
"""


class TheBird(object):
	"""
	[E]verybody's heard about the bird  
	"""

	def __init__(self):
		self.title = "Surfin' Bird"
		self.artist = "The Trashmen"
		self.released = 1964
		self.message = "Bird, bird, bird, b-bird's the word"


	def __str__(self):
		return "Bird, bird, bird, b-bird's the word"


	def play(self):
		"""
		Play _Surfin' Bird_ by The Trashmen
		"""
		webbrowser.open('https://www.youtube.com/watch?v=aPrtFxd9u9Y')
		return 

	def celebrate(self):
		"""
		See Seth MacFarlane celebrate the bird
		"""
		self.celebrated_by = "Seth MacFarlane"
		webbrowser.open('https://www.youtube.com/watch?v=2WNrx2jq184')
		return


class TheWord(TheBird):
	"""
	B-bird's the word...
	"""

	def __init__(self):
		self.question = "What's the word?"
		super(TheWord, self).__init__()

	def __str__(self):
		return self.message


def what_is_the_word():
	"""
	When asked what the word is, return TheBird()

	Some uses:
	>>> print what_is_the_word()
	>>> what_is_the_word().play()

	"""
	return TheBird()
