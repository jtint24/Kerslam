"""
getAssociationMap



"""

def getAssociationMap(text: str) -> {str : {str : int}}:
  text = text.lower()
  returnMap: {str: {str: int}} = {"__" : {"__" : 0}}
  print("text:")
  print(text)
  vocabulary: [str] = list(set(removePunctuation(text).split(" ")))
  vocabulary = removeFunctionWords(vocabulary)
  print("vocabulary:")
  print(vocabulary)
  sentences: [str] = periodReplace(text).split(".")
  print("sentences:")
  print(sentences)

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
      
def removeFunctionWords(vocabulary: [str]) -> str:
  functionWords: [str] = ["it", "and", "a", "because", "digits", "if", "even", "too", "be", "is", "there", "in", "of", "you", "to", "I", "me","could", "so", "then", "that", "this", "the", "than","by","for","only","an","therefore","will","from","has","with","but","are","also","at","yet","was","on","our","my","me","can","as","around","its"]
  for functionWord in functionWords:
    if functionWord in vocabulary:
      vocabulary.remove(functionWord)  
  return vocabulary

def removePunctuation(text: str) -> str:
  retString: str = str(text)
  disallowedCharacters: str = ".?!,_'()“”"
  for character in disallowedCharacters:
    retString = retString.replace(character,"")
  return retString

def periodReplace(text: str) -> str:
  charsToPeriods: str = "?!"
  for character in charsToPeriods:
    text = str(text).replace(character, ".")
  return text