import features.features

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class Weights:
    def __init__(self, parameters):
        self.features = features.features.Features(parameters)

        self.feature_names = set()

        self.features_weights = dict()

        self.feature_parameters = dict()

    def init_top_docs_run_query(self, query):
        self.features.init_top_docs_run_query(query)

    def compute_weight(self, term):
        return self.features.linear_combination(term, self.feature_names, self.features_weights,
                                                self.feature_parameters)
