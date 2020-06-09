'''
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Test for 'class AnonymousSurvey' ."""

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_responses('English')

        #To check if 'English' is in the list 'responses'.
        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ["English", "Spanish", "French"]
        for response in responses:
            my_survey.store_responses(responses)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
'''

#NOTE: The above is repitive, therefore we use
#The setUp() method
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Dutch']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_responses(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
