import getAssociationMap #to convert Strings into Association map dictionaries
import stringUtils

"""
AssociationMap

holds information about associations between words in texts
"""

class AssociationMap:
  def __init__(self, text: str):
    self.aMap: {str : {str : int}} = getAssociationMap.getAssociationMap(text)
    self.vocabulary: [str] = list(set(stringUtils.removePunctuation(text.lower()).split(" ")))
    self.vocabulary = getAssociationMap.removeFunctionWords(self.vocabulary)

  """
  cooccuranceProportion

  gets the percent of times that two words cooccur in a sentence out of all the times one word occurs in the sentence

  :param word1: the first word to check
  :type word1: string
  :param word2: the second word to check
  :type word2: string
  :returns: the proportion of the times that the two words occur together in a sentence
  :rtype: float
  """
  def cooccuranceProportion(self, word1: str, word2: str) -> float:
    submentions: int = self.submentionsForWord(word1)
    coocuranceCount: int = self.aMap[word1][word2]
    if submentions == 0:
      return 0
    return float(coocuranceCount)/float(submentions)

  """
  sumbmentionsForWord

  gets the number of time any word cooccurs with a given word 
  
  :param word1: the word to check the number of submentions for
  :type word1: string
  :returns: the number of times a word occurs with word1 in a sentence
  :rtype: int
  """
  def submentionsForWord(self, word1: str) -> int:
    wordArray: {str : int} = self.aMap[word1]
    sum: int = 0
    for word in wordArray:
      sum+=wordArray[word]
    return sum

