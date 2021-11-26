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

def functionWords() -> [str]:
  return ["it", "and", "a", "because", "digits", "if", "even", "too", "be", "is", "there", "in", "of", "you", "to", "I", "me","could", "so", "then", "that", "this", "the", "than","by","for","only","an","therefore","will","from","has","with","but","are","also","at","yet","was","on","our","my","me","can","as","around","its"]