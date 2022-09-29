from fuzzywuzzy import process 
from fuzzywuzzy import fuzz

  
s1 = "This is an apple."
s2 = "I love apples."
print "FuzzyWuzzy Ratio: ", fuzz.ratio(s1, s2)
print "FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2)
print "FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2)
print "FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2)
print "FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2),'\n\n'
  
# for process library,
query = 'My name is Ron'
choices = ['my name is Ron', 'my name Ron.', 'R for Ron'] 
print "List of ratios: "
print process.extract(query, choices), '\n'
print "Best among the above list: ",process.extractOne(query, choices)
