#########################################################################################################################

from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d)



# This the benifit for using the defaultdict, if we use a normal dict,
#  we have to check if the key is in the dict or not, and then append the value to the list.
#  But with defaultdict, we can just append the value to the list without checking if the key is in the dict or not.

# Here normal dict will raise a KeyError if the key is not in the dict.
print(d['pink'])
print('\n')

#########################################################################################################################

from collections import Counter

paragraph = "This is a sample paragraph. This paragraph is for testing the Counter functionality."

words = paragraph.lower().split()
word_count = Counter(words)
word_count_dict = dict(word_count)
print(type(word_count_dict),"\nValues: ",word_count_dict)  # Counter is a subclass of dict, so it has all the methods of dict.

#########################################################################################################################
 