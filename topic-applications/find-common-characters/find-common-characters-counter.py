
#   Programmer:     Cheng, Jeff
#   Last Modified:  07-20-2024 06:26PM
#   Problem:        1002. Find Common Characters

#   Given a string array words, return an array of all characters that show up 
#   in all strings within the words (including duplicates). 

#   You may return the answer in any order.

#   Example 1:
#   Input: words = ["bella","label","roller"]
#   Output: ["e","l","l"]

#   Example 2:
#   Input: words = ["cool","lock","cook"]
#   Output: ["c","o"]

#   include Counter
from collections import Counter

class Solution:
    def commonChars(self, words):
#   check extreme cases
        if len(words) < 2:
            return words

#   init the first element to be counter
        model = Counter(words[0])

#   iterate through the list
        for word in words[1:]:
#   reduce to the lowest common counts
            model &= Counter(word)        

#   return the result
        return list(model.elements())