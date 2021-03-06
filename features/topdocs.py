from math import log

import index.index
from features.collection import Collection

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class Topdocs(Collection):
    def __init__(self, parameters):
        super().__init__(parameters)
        self.index = index.index.Index(parameters)
        self.index.init_query_env()
        self.runs = None

    def init_top_docs_run_query(self, query):
        self.runs = self.index.run_query_doc_names(query)

    def td_uw_expression_count(self, term, feature_parameters):
        return sum(self.index.expression_list_in_top_docs(term, "#uw", feature_parameters["window_size"],
                                                          feature_parameters["n_top_docs"], self.runs).values())

    def td_od_expression_count(self, term, feature_parameters):
        return sum(self.index.expression_list_in_top_docs(term, "#od", feature_parameters["window_size"],
                                                          feature_parameters["n_top_docs"], self.runs).values())

    def td_uw_expression_document_count(self, term, feature_parameters):
        return len(self.index.expression_list_in_top_docs(term, "#uw", feature_parameters["window_size"],
                                                          feature_parameters["n_top_docs"], self.runs))

    def td_od_expression_document_count(self, term, feature_parameters):
        return len(self.index.expression_list_in_top_docs(term, "#od", feature_parameters["window_size"],
                                                          feature_parameters["n_top_docs"], self.runs))

    def td_unigram_term_count(self, term, feature_parameters):
        return len(self.index.expression_list_in_top_docs_exp(expression=term, runs=self.runs,
                                                              n_top_docs=feature_parameters["n_top_docs"]))

    def td_unigram_document_count(self, term, feature_parameters):
        return sum(self.index.expression_list_in_top_docs_exp(expression=term, runs=self.runs,
                                                              n_top_docs=feature_parameters["n_top_docs"]).values())

    def td_uw_expression_norm_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        bigram = self.gram_pair_2_bigarm(gram_pair)
        total_terms = self.index.document_length_docs_names(self.runs[:feature_parameters["n_top_docs"]])
        return -log((self.td_uw_expression_count(bigram, feature_parameters) + 1) / total_terms)

    def td_od_expression_norm_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        bigram = self.gram_pair_2_bigarm(gram_pair)
        total_terms = self.index.document_length_docs_names(self.runs[:feature_parameters["n_top_docs"]])
        return -log((self.td_od_expression_count(bigram, feature_parameters) + 1) / total_terms)

    def td_uw_expression_norm_document_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        bigram = self.gram_pair_2_bigarm(gram_pair)
        return -log(
            (self.td_uw_expression_document_count(bigram, feature_parameters) + 1) / feature_parameters["n_top_docs"])

    def td_od_expression_norm_document_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        bigram = self.gram_pair_2_bigarm(gram_pair)
        return -log(
            (self.td_od_expression_document_count(bigram, feature_parameters) + 1) / feature_parameters["n_top_docs"])

    def td_unigram_norm_term_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        unigram = self.gram_pair_2_unigarm(gram_pair)
        total_terms = self.index.document_length_docs_names(self.runs[:feature_parameters["n_top_docs"]])
        return -log((self.td_unigram_term_count(unigram, feature_parameters) + 1) / total_terms)

    def td_unigram_norm_document_count(self, gram_pair, feature_parameters):
        if self.runs is None:
            raise ValueError("runs are empty")
        unigram = self.gram_pair_2_unigarm(gram_pair)
        return -log(
            (self.td_unigram_document_count(unigram, feature_parameters) + 1) / feature_parameters["n_top_docs"])
