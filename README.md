# docker_language_detection


This repository creates a flask api for language detection using spacy

create a docker image from this repository using the Dockerfile present

spacy_encore_web_sm was used for this task.
Reference : https://pypi.org/project/spacy-language-detection/

The api takes text string as input and returns the top language of the sentence.

Input json example : {"text" : "Pourriez-vous m’aider?"}

Output : "fr" -- because french is the top langugae detcted for the input above
