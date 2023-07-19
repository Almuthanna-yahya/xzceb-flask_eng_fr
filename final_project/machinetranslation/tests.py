import unittest
from deep_translator import MyMemoryTranslator

class TestMyMemoryTranslator(unittest.TestCase):

    def setUp(self):
        self.translator = MyMemoryTranslator()

    def test_hello_translation(self):
        source_text = "Hello"
        target_text = self.translator.translate(text=source_text, to_lang="fr")
        self.assertEqual(target_text, "Bonjour")

    def test_bonjour_translation(self):
        source_text = "Bonjour"
        target_text = self.translator.translate(text=source_text, to_lang="en")
        self.assertEqual(target_text, "Hello")

    def test_hello_to_bonjour_and_back(self):
        source_text = "Hello"
        target_text = self.translator.translate(text=source_text, to_lang="fr")
        back_to_source = self.translator.translate(text=target_text, to_lang="en")
        self.assertEqual(back_to_source, source_text)

    def test_bonjour_to_hello_and_back(self):
        source_text = "Bonjour"
        target_text = self.translator.translate(text=source_text, to_lang="en")
        back_to_source = self.translator.translate(text=target_text, to_lang="fr")
        self.assertEqual(back_to_source, source_text)

if __name__ == '__main__':
    unittest.main()

