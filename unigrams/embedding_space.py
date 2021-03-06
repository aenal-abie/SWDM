from collections import defaultdict

from unigrams.original import Original
from unigrams.word2vec import Word2vec

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class EmbeddingSpace(Original):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.parameters = parameters
        self.word2vec = Word2vec()
        self.unigrams_in_embedding_space_history = defaultdict()

    def initialize(self):
        self.word2vec.pre_trained_google_news_300_model()
        print("word2vec model obtained.")

    def check_if_already_stem_exists(self, unigrams_in_embedding_space_pruned, unigram, orig_unigram):
        if self.index_.check_if_have_same_stem(unigram, orig_unigram):
            return True
        for other_unigram in unigrams_in_embedding_space_pruned:
            if self.index_.check_if_have_same_stem(unigram, other_unigram[0]):
                return True
        return False

    def _gen_similar_words(self, orig_unigram, word2vec):
        if orig_unigram not in self.unigrams_in_embedding_space_history:
            unigrams_in_embedding_space = word2vec.gen_similar_words(unigram=orig_unigram, topn=100)
            self.unigrams_in_embedding_space_history[orig_unigram] = unigrams_in_embedding_space
            return unigrams_in_embedding_space
        else:
            return self.unigrams_in_embedding_space_history[orig_unigram]

    def check_if_unigram_should_be_added(self, unigram, distance=1, unigrams_in_embedding_space_pruned=list(),
                                         orig_unigram=""):
        word2vec_upper_threshold = self.parameters.params["word2vec"]["upper_threshold"]
        word2vec_lower_threshold = self.parameters.params["word2vec"]["lower_threshold"]
        word2vec_n_max = self.parameters.params["word2vec"]["n_max"]

        unigram = unigram.lower()

        if not Original.check_if_unigram_should_be_added(self, unigram):
            return False
        if not self.index_.check_if_exists_in_index(orig_unigram):
            return False
        if len(unigrams_in_embedding_space_pruned) > word2vec_n_max:
            return False
        if distance > word2vec_upper_threshold:
            return False
        if distance < word2vec_lower_threshold:
            return False
        if self.check_if_already_stem_exists(unigrams_in_embedding_space_pruned, unigram, orig_unigram):
            return False
        return True

    def _find_unigrams_in_embedding_space_1(self, word2vec, orig_unigram):

        unigrams_in_embedding_space = self._gen_similar_words(orig_unigram, word2vec)

        unigrams_in_embedding_space_pruned = []
        for (unigram, distance) in unigrams_in_embedding_space:
            unigram = str(unigram).lower()
            if self.check_if_unigram_should_be_added(unigram, distance, unigrams_in_embedding_space_pruned,
                                                     orig_unigram):
                unigrams_in_embedding_space_pruned += [(unigram, distance)]

        return unigrams_in_embedding_space_pruned

    def find_unigrams(self, unigrams_original):
        for unigram in unigrams_original:
            yield unigram[1][0][0], self._find_unigrams_in_embedding_space_1(self.word2vec, unigram[1][0][0])
