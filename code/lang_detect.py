import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from flask import Flask, request, g, abort
from flask import jsonify
import json
import ast
import configparser
import logging.config
import spacy
from spacy.language import Language
from spacy_language_detection import LanguageDetector


logging.config.fileConfig("../config/logging.conf")


app = Flask(__name__)

def get_lang_detector(nlp, name):
    return LanguageDetector(seed=42) 

def load_model():
    global nlp_model
    nlp_model = spacy.load("en_core_web_sm")
    Language.factory("language_detector", func=get_lang_detector)
    nlp_model.add_pipe('language_detector', last=True)
    return nlp_model


@app.route('/language_detection/healthCheck', methods=['GET', 'POST'], strict_slashes = False)
def checkHealth():

    """HEALTHCHECKER
    
    This API would be polled to check the response of the server(bot) that is running..
    """
    return(jsonify({'status' : 'Language Detection Server is running...'}), 200)

@app.route('/language_detection', methods=['GET', 'POST'], strict_slashes = False)
def detect():
    """
    detect method returns the top language for the given input
    Parameters
    ----------
    text : String.
    Returns
    -------
    JSON: Returns the top language in the input.
    """
    try:
        text = request.json['text']
        logging.info("The input received for language detection is : {}".format(text))
        doc = nlp_model(text)
        languages = []
        for i, sent in enumerate(doc.sents):
            languages.append(sent._.language['language'])
        top_language = max(set(languages), key=languages.count)
        logging.info("The detected language is : {}".format(top_language))
        return json.dumps(top_language)
    except Exception as error:
        logging.error(str(error))


if __name__ == '__main__':
    load_model()
    app.run(host="0.0.0.0",
            port= 8000,
            debug=False)

    

