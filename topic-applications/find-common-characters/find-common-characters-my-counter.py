
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

class Solution:
    def commonChars(self, words):
#   create own counter
#   create the dictionary
#   iterate through the parameter & update the dictionary as necessary
#   result the iterated result
        def counter(self, w):
            frequencies = {}

            for c in w:
                frequencies[c] = frequencies.get(c, 0) + 1
            return frequencies
        
#   handle extreme cases
        if len(words) < 2:
            return words
        
#   init the first element as a counter
        model = counter(self, words[0])

#   iterate through the remaining elements
        for word in words[1:]:
#   creating each as a new counter
            new_model = counter(self, word)
#   for each subsequence elements, run them against the first counter
#   and reduce to the lowest common count
            for c, count in list(model.items()):
                try:
                    model[c] = min(count, new_model[c])
                except KeyError:
#   update (delete) key as needed
                    del model[c]

#   create result list
        commonToAll = []
#   extend element * respective count int the list
        for c, count in model.items():
            commonToAll.extend( [c] * count)

#   return the result
        return commonToAll