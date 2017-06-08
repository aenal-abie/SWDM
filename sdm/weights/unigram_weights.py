import features.features
from sdm.weights.weights import Weights

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class UnigramWeights(Weights):
    def __init__(self, parameters):
        self.parameters = parameters
        Weights.__init__(self, self.parameters)
        self.features = features.features.Features(self.parameters)
        self.feature_names = {
            "norm_term_count",
            "norm_document_count",
            "unigrams_cosine_similarity_with_orig",
            "td_norm_unigram_count",
            "td_norm_unigram_document_count"
        }

    def compute_weight(self, term, term_dependent_feature_parameters):

        self.feature_parameters = self.parameters.params['feature_parameters']['UnigramWeights']
        self.features_weights = self.parameters.params['features_weights']['UnigramWeights']

        unigram_nearest_neighbor = term_dependent_feature_parameters["unigram_nearest_neighbor"]
        self.feature_parameters.update({
            "unigrams_cosine_similarity_with_orig": {
                'unigram_nearest_neighbor': unigram_nearest_neighbor
            }
        })

        return Weights.compute_weight(self, term, term_dependent_feature_parameters)
