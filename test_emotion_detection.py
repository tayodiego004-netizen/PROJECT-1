import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Unit tests for the emotion detection function."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = (
            '{"emotionPredictions":[{"emotion":'
            '{"anger":0.01,"disgust":0.01,"fear":0.02,'
            '"joy":0.95,"sadness":0.01}}]}'
        )

        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.text = (
            '{"emotionPredictions":[{"emotion":'
            '{"anger":0.90,"disgust":0.01,"fear":0.02,'
            '"joy":0.03,"sadness":0.04}}]}'
        )

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input(self, mock_post):
        result = emotion_detector(" ")
        self.assertIsNone(result["dominant_emotion"])
        mock_post.assert_not_called()


if __name__ == "__main__":
    unittest.main()
