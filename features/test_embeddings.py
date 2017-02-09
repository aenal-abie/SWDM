from unittest import TestCase

import features.embeddings


class TestEmbeddings(TestCase):
    def test_cosine_similarity_with_orig(self):
        feature_parameters = {
            'unigram_nearest_neighbor': [('hello', 1), ('world', 0.65)]}

        res = features.embeddings.Embeddings.cosine_similarity_with_orig('world', feature_parameters)
        expected_res = 0.65

        self.assertEqual(res, expected_res)