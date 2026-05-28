import spacy

nlp = spacy.load("en_core_web_sm")

def parse_jd(text):
    doc = nlp(text.lower())
    return set(token.text for token in doc if token.is_alpha and not token.is_stop)
