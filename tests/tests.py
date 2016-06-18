import unittest
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