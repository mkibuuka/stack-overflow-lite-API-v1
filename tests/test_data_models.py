import unittest
from tests.base import BaseTestCase
from app.models.models import Question, Answer


class TestDataModels(BaseTestCase):
    """
     Test suite for data models

    Arguments:
        BaseTestCase {Class} -- Base test class for running custom tests
    """

    def test_question_model(self):
        """
        Test question model instance
        """

        question_1 = Question('testing',
                              'check if this class initialiser works',
                              'unittests')
        self.assertIsInstance(question_1, Question)
        self.assertTrue(question_1.title, 'testing')
        self.assertTrue(
            question_1.body, 'check if this class initialiser works')
        self.assertTrue(question_1.tag, 'unittests')

    def test_answer_model(self):
        """
         Test Answer model instance
        """
        answer_1 = Answer(1, 'answer to the first question')
        self.assertIsInstance(answer_1, Answer)
        self.assertTrue(answer_1.body, 'answer to the first question')
        self.assertEqual(answer_1.id, 1)
