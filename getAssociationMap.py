"""
getAssociationMap

creates a map of how many times each notable token in a sentence cooccurs with each other notable token within the same sentence.

:param text: the text to create the map from
:type text: string
:returns: the map of cooccurance counts for each token pair
:rtype: {str: {str : int}}
"""
def getAssociationMap(text: str) -> {str : {str : int}}:
  text = text.lower()
  returnMap: {str: {str: int}} = {"__" : {"__" : 0}}
  vocabulary: [str] = list(set(removePunctuation(text).split(" ")))
  vocabulary = removeFunctionWords(vocabulary)
  sentences: [str] = periodReplace(text).split(".")

  for word1 in vocabulary:
    returnMap[word1] = {"__" : 0}
    for word2 in vocabulary:
      returnMap[word1][word2] = 0

  for sentence in sentences:
    cleanSentence: str = removePunctuation(sentence)
    sentenceWord: [str] = cleanSentence.split(" ")
    for word1 in sentenceWord:
      for word2 in sentenceWord:
        try:
          returnMap[word1][word2]+=1
        except:
          pass

  return returnMap


"""
removeFunctionWords

removes function words from a list of strings

:param vocabulary: list of strings to remove function words from
:type vocabulary: [str]
:returns: list of strings with function words removed
:rtype: [str]
"""
def removeFunctionWords(vocabulary: [str]) -> [str]:
  functionWords: [str] = ["it", "and", "a", "because", "digits", "if", "even", "too", "be", "is", "there", "in", "of", "you", "to", "I", "me","could", "so", "then", "that", "this", "the", "than","by","for","only","an","therefore","will","from","has","with","but","are","also","at","yet","was","on","our","my","me","can","as","around","its"]
  for functionWord in functionWords:
    if functionWord in vocabulary:
      vocabulary.remove(functionWord)  
  return vocabulary

"""
removePunctuation

removes puntuation from a text

:param text: the text to remove punctuation from
:type text: string
:returns: the cleaned text
:rtype: string
"""
def removePunctuation(text: str) -> str:
  retString: str = str(text)
  disallowedCharacters: str = ".?!,_'()“”"
  for character in disallowedCharacters:
    retString = retString.replace(character,"")
  return retString


"""
periodReplace

replaces all end stops ("?","!") with periods

:param text: the text to change end stops in
:type text: string
:returns: the cleaned text
:rtype: string
"""
def periodReplace(text: str) -> str:
  charsToPeriods: str = "?!"
  for character in charsToPeriods:
    text = str(text).replace(character, ".")
  return text