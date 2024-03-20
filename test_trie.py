import unittest
from trie import Trie


class TestPrefixTrieUncompressed(unittest.TestCase):
    def test_one(self):
        data = ["apple", "app", "app", "apricot", "april", "apartment"]
        uncompressed_trie = Trie(is_compressed=False)
        uncompressed_trie.construct_trie_from_text(data)
        self.assertEqual(uncompressed_trie.search_and_get_depth("apple"), 5)
        self.assertEqual(uncompressed_trie.search_and_get_depth("app"), 3)
        self.assertEqual(uncompressed_trie.search_and_get_depth("apricot"), 7)
        self.assertEqual(uncompressed_trie.search_and_get_depth("april"), 5)
        self.assertEqual(uncompressed_trie.search_and_get_depth("apartment"), 9)
        self.assertEqual(uncompressed_trie.search_and_get_depth("ap"), -1)
        self.assertEqual(uncompressed_trie.search_and_get_depth("apricots"), -1)
        self.assertEqual(uncompressed_trie.search_and_get_depth("aprilfool"), -1)


class TestPrefixTrieCompressed(unittest.TestCase):
    def test_one(self):
        data = ["apple", "app", "apricot", "april", "apartment", "apache"]
        compressed_trie = Trie(is_compressed=True)
        compressed_trie.construct_trie_from_text(data)
        self.assertEqual(compressed_trie.search_and_get_depth("apple"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("app"), 2)
        self.assertEqual(compressed_trie.search_and_get_depth("apricot"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("april"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("apartment"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("apache"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("ap"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("apricots"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("aprilfool"), -1)

    def test_two(self):
        data = [
            "1900",
            "1901",
            "190111",
            "1910",
            "1920",
            "1930",
            "1935",
            "1935abc",
            "1940",
            "1950",
        ]
        compressed_trie = Trie(is_compressed=True)
        compressed_trie.construct_trie_from_text(data)
        self.assertEqual(compressed_trie.search_and_get_depth("1900"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("1910"), 2)
        self.assertEqual(compressed_trie.search_and_get_depth("1920"), 2)
        self.assertEqual(compressed_trie.search_and_get_depth("1930"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("1935"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("1935abc"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("1940"), 2)
        self.assertEqual(compressed_trie.search_and_get_depth("1950"), 2)
        self.assertEqual(compressed_trie.search_and_get_depth("19"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("193"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("1936"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("1935a"), -1)

    def test_three(self):
        data = ["facebook", "face", "this", "there", "then"]
        compressed_trie = Trie(is_compressed=True)
        compressed_trie.construct_trie_from_text(data)
        self.assertEqual(compressed_trie.search_and_get_depth("there"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("therein"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("th"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("fab"), -1)

    def test_four(self):
        data = [
            "romane",
            "romanus",
            "romulus",
            "rubens",
            "ruber",
            "rubicon",
            "rubicundus",
        ]
        compressed_trie = Trie(is_compressed=True)
        compressed_trie.construct_trie_from_text(data)
        self.assertEqual(compressed_trie.search_and_get_depth("romane"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("romanus"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("romulus"), 3)
        self.assertEqual(compressed_trie.search_and_get_depth("rubens"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("ruber"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("rubicon"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("rubicundus"), 4)
        self.assertEqual(compressed_trie.search_and_get_depth("rom"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("rub"), -1)
        self.assertEqual(compressed_trie.search_and_get_depth("rubi"), -1)


class TestSuffixTrieUncompressed(unittest.TestCase):
    def test_one(self):
        data = ["alpha"]
        uncompressed_suffix_tree = Trie(is_compressed=False)
        uncompressed_suffix_tree.construct_suffix_tree_from_text(data)
        self.assertEqual(uncompressed_suffix_tree.search_and_get_depth("alpha"), 5)


class TestSuffixTrieCompressed(unittest.TestCase):
    def test_one(self):
        data = ["alpha", "lpha"]
        compressed_suffix_tree = Trie(is_compressed=True)
        compressed_suffix_tree.construct_suffix_tree_from_text(data)
        self.assertEqual(compressed_suffix_tree.search_and_get_depth("alpha"), 2)
        self.assertEqual(compressed_suffix_tree.search_and_get_depth("lpha"), 1)


if __name__ == "__main__":
    unittest.main()
