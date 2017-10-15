from natasha import NamesExtractor
from textblob import TextBlob

with open('factRuEval.txt', 'r', encoding='utf-8') as text:
    lines = text.read().splitlines()
    natasha = NamesExtractor()
    matches = natasha(str(lines))
    for match in matches:
        print(match.fact)
    wiki = TextBlob(str(lines))
    for np in wiki.noun_phrases:
        print(np)

'Unfortunately, it is impossible to compare named entity recognition in Natasha and TextBlob, because there is no' \
'named entity recognition in TextBlob (only noun phrases) :('