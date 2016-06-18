import unittest
import requests
import theword as tw 

class TheWordTest(unittest.TestCase):

	def test_inheritance(self):
		"""
		Tests class inheritance
		"""
		self.assertIsInstance(tw.TheWord(), tw.TheBird)


	def test_assignment(self):
		"""
		Tests assignment
		"""
		self.assertEquals(1964, tw.TheBird().released)


	def test_question(self):
		"""
		Tests results of external function call
		"""
		self.assertEquals("Bird, bird, bird, b-bird's the word", 
			tw.what_is_the_word().message)


	def test_song_link(self):
		"""
		Tests if _The Trashmen_ link is active
		"""
		request = requests.get('https://www.youtube.com/watch?v=aPrtFxd9u9Y')
		self.assertEquals(200, request.status_code)


	def test_parody_link(self):
		"""
		Tests if _The Family Guy_ link is active
		"""
		request = requests.get('https://www.youtube.com/watch?v=2WNrx2jq184')
		self.assertEquals(200, request.status_code)
