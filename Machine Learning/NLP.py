# For install : 
# pip install spacy
# python -m spacy download en_core_web_sm
import spacy

# language model
nlp = spacy.load('en_core_web_sm')

sample = "The quick brown fox, jumps over the lazy dog."
# print(sample.split()) # Primitive

doc = nlp(sample)

""" how spacey sees the sentence
 token refers to unit of text
 .orth_ method """ 
# print([token.orth_ for token in doc])

# leaving out the underscore gives the integer code of the word
# print([(token, token.orth_, token.orth) for token in doc])

# words that spacey thinks are stop words
# for word in doc:
#     if word.is_stop == True:
#         print("Spacy thinks this is a stop word: ", word)

# Lemmatisation gives the origin word
sample = "sing sang singing"
doc = nlp(sample)

# print([token.lemma_ for token in doc])

# Entity Recognition
wiki_priyanka = """known by her married name Priyanka Chopra Jonas, is an Indian actress,
singer, film producer, philanthropist, and the winner of the Miss World 2000 pageant.
One of India's highest-paid and most popular celebrities, Chopra has received numerous
awards, including a National Film Award and five Filmfare Awards. In 2016, the Government
of India honoured her with the Padma Shri, and Time named her one of the 100 most influential people in the world."""

nlp_priyanka = nlp(wiki_priyanka)
# .label_ method gives what category spacy gives e.g. 'DATE', 'NORP', 'CARDINAL'... 
# .label method gives the integer value associated 
# .ents method for entity recognition 
print([(i, i.label_, i.label) for i in nlp_priyanka.ents])

print("\n---------------------------------------\n")
# .explain method allows spacy to explain categories
entity_norp = spacy.explain("NORP")
print(f"NORP :{entity_norp}")

# for i in nlp_priyanka.ents:
#     if i.label_ == 'NORP':
#         print(i)

# .explain method allows spacy to explain categories
entity_org = spacy.explain("ORG")
print(f"ORG :{entity_org}")

# .explain method allows spacy to explain categories
entity_cardinal = spacy.explain("CARDINAL")
print(f"CARDINAL :{entity_cardinal}")

# .explain method allows spacy to explain categories
entity_fac = spacy.explain("FAC")
print(f"FAC :{entity_fac}")

# .explain method allows spacy to explain categories
entity_product = spacy.explain("PRODUCT")
print(f"PRODUCT :{entity_product}")