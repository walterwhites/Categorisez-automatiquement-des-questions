import unittest
from api.app import preprocessing
import nltk

class TestRemoveUrls(unittest.TestCase):
    def test_remove_urls(self):
        self.assertEqual(preprocessing.remove_urls("Check this link: https://example.com"), "Check this link: ")
        self.assertEqual(preprocessing.remove_urls("http://example.com is a website"), " is a website")
        self.assertEqual(preprocessing.remove_urls("No URL here"), "No URL here")

class TestCustomClean(unittest.TestCase):
    def test_custom_clean(self):
        self.assertEqual(preprocessing.custom_clean(["Hello\nWorld"]), ["Hello World"])
        self.assertEqual(preprocessing.custom_clean(["Multiple     spaces"]), ["Multiple spaces"])

class TestLowercaseText(unittest.TestCase):
    def test_lowercase_text(self):
        self.assertEqual(preprocessing.lowercase_text("ALL CAPS"), "all caps")

class TestTokenization(unittest.TestCase):
    def test_tokenization(self):
        nltk.download('punkt')
        self.assertEqual(preprocessing.tokenization("This is a sentence. This is another."), ["This is a sentence.", "This is another."])

class TestLemmatization(unittest.TestCase):
    nltk.download('wordnet')
    def test_lemmatization(self):
        self.assertEqual(preprocessing.lemmatization(["running", "cars"]), ["running", "car"])


class TestRemoveStopwords(unittest.TestCase):
    nltk.download('stopwords')
    def test_remove_stopwords(self):
        self.assertEqual(preprocessing.remove_stopwords(["this is a test"]), ["test"])
        self.assertEqual(preprocessing.remove_stopwords(["another example here"]), ["another example"])

class TestClearPunctuation(unittest.TestCase):
    def test_clear_ponctuation(self):
        self.assertEqual(preprocessing.clear_ponctuation(["Hello, world!"]), ["Hello world"])

class TestExtractTextFromHtml(unittest.TestCase):
    def test_extract_text_from_body(self):
        html = "<html><body><p>Hello World</p></body></html>"
        self.assertEqual(preprocessing.extract_text_from_body(html), "Hello World")

if __name__ == '__main__':
    unittest.main()
#%%
