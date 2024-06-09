import unittest
from bs4 import BeautifulSoup
import requests

from src.utils import tweet_parser


class TestTweetParser(unittest.TestCase):
    def test_parse_single_tweet(self):
        # Arrange
        selected_name = "twitter_handle"  # Replace with Twitter handle to test
        url = f"https://x.com/{selected_name}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        expected_output = ""  # TODO: Set to desired output

        # Act
        parsed_tweets = tweet_parser.parse(soup)

        # Assert
        self.assertEquals(parsed_tweets, expected_output)
