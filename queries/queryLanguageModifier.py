import os
import re
import sys

from bs4 import BeautifulSoup

from embeddings.embedding_space import EmbeddingSpace
from parameters.parameters import Parameters
from sdm.expanded_sdm import ExpandedSdm

sys.path.insert(0, os.path.abspath('..'))
try:
    from runs.runs import Runs
    from queries.queries import Queries
except:
    raise

__author__ = 'Saeid Balaneshin-kordan'
__email__ = "saeid@wayne.edu"
__date__ = 11 / 21 / 16


class QueryLanguageModifier(object):
    def __init__(self, parameters):
        self.parameters = parameters
        self.embedding_space = EmbeddingSpace(self.parameters)
        self.expanded_sdm = ExpandedSdm(self.parameters)

    @staticmethod
    def find_all_queries(soup):
        queries = soup.findAll("query")
        return queries

    def gen_sdm_fields_texts(self, text):
        sdm_fields_texts = dict()
        unigrams_in_embedding_space = self.embedding_space.find_unigrams_in_embedding_space(text)
        sdm_fields_texts['u'] = self.expanded_sdm.gen_sdm_field_1_text(unigrams_in_embedding_space, "#combine")
        sdm_fields_texts['o'] = self.expanded_sdm.gen_sdm_field_1_text(unigrams_in_embedding_space, "#od")
        sdm_fields_texts['w'] = self.expanded_sdm.gen_sdm_field_1_text(unigrams_in_embedding_space, "#uw")
        return sdm_fields_texts

    @staticmethod
    def gen_combine_fields_text(field_weights, field_texts):
        new_q_text = "#weight(\n"
        for field_name, field_weight in field_weights.items():
            if field_weight > 0:
                q_text = field_texts.get(field_name)
                combine_text = str(field_weight) + q_text
                new_q_text += combine_text
        new_q_text += ")\n"
        return new_q_text

    def update_queries(self, queries, field_weights):
        for q in queries:
            q_text = q.find("text")
            q_text_ = q_text.text.strip()
            q_text_ = re.sub('[^0-9a-zA-Z]+', ' ', q_text_)
            field_texts = self.gen_sdm_fields_texts(q_text_)
            q_text.string = self.gen_combine_fields_text(field_weights, field_texts)

    @staticmethod
    def post_process_indri_run_query_cfg(soup_str):
        soup_str = soup_str.replace("<trecformat>", "<trecFormat>").replace("</trecformat>", "</trecFormat>")
        soup_str = soup_str.replace("<printquery>", "<printQuery>").replace("</printquery>", "</printQuery>")
        soup_str = soup_str.replace("<fbdocs>", "<fbDocs>").replace("</fbdocs>", "</fbDocs>")
        soup_str = soup_str.replace("<fbterms>", "<fbTerms>").replace("</fbterms>", "</fbTerms>")
        soup_str = soup_str.replace("</workingSetDocno>", "</workingSetDocno>\n")
        return soup_str

    def update_indri_query_file(self, soup, new_indri_query_file):
        with open(new_indri_query_file, 'w') as f:
            soup_str = str(soup.body.parameters)
            soup_str = self.post_process_indri_run_query_cfg(soup_str)
            print(soup_str, file=f)

    @staticmethod
    def update_index_dir(soup, index_dir):
        index = soup.find('index')
        index.string = index_dir

    @staticmethod
    def get_runs_for_re_rank(previous_runs_file):
        if previous_runs_file is None:
            return None
        else:
            return Runs().runs_file_to_documents_dict(previous_runs_file)

    @staticmethod
    def update_relevance_feedback(soup, fb_terms, fb_docs):
        if fb_terms > 0 and fb_docs > 0:
            soup_parameters = soup.find("parameters")
            soup_tmp = BeautifulSoup("", "lxml")
            fb_terms_tag = soup_tmp.new_tag('fbTerms')
            fb_terms_tag.string = str(fb_terms)
            soup_parameters.append(fb_terms_tag)
            fb_docs_tag = soup_tmp.new_tag('fbDocs')
            fb_docs_tag.string = str(fb_docs)
            soup_parameters.append(fb_docs_tag)

    def run(self):

        self.embedding_space.initialize()
        self.run_no_word2vec_initialization()

    def run_no_word2vec_initialization(self):
        soup = Queries().indri_query_file_2_soup(self.parameters.params["query_files"]["old_indri_query_file"])

        self.update_index_dir(soup, self.parameters.params["repo_dir"])

        queries = self.find_all_queries(soup)
        self.update_queries(queries, self.parameters.params["sdm_field_weights"])

        self.update_relevance_feedback(soup, self.parameters.params["prf"]["fb_terms"],
                                       self.parameters.params["prf"]["fb_docs"])

        self.update_indri_query_file(soup, self.parameters.params["query_files"]["new_indri_query_file"])


if __name__ == "__main__":
    parameters_ = Parameters()
    parameters_.read_from_params_file()
    QueryLanguageModifier(parameters_).run()
