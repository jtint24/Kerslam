import math
import AssociationMap
import getAssociationMap

def getKeywords(text: str) -> [str]:
  bitLogCoefficient: float = 1.0/math.log(2)
  textMap: AssociationMap = AssociationMap.AssociationMap(text);

  functionWords: [str] = ["it", "and", "a", "because", "digits", "if", "even", "too", "be", "is", "there", "in", "of", "you", "to", "I", "me","could", "so", "then", "that", "this", "the", "than","by","for","only","an","therefore","will","from","has","with","but","are","also","at","yet","was","on","our","my","me","can","as","around","its"]

  unrefinedWordEntropies: {str : float} = {"__" : 0}

  for word1 in textMap.vocabulary:
    sumProb: float = 0;
    if not word1 in functionWords:
      for word2 in textMap.vocabulary:
        if not word2 in functionWords:
          cooccuranceProportion = textMap.cooccuranceProportion(word1, word2)
          if cooccuranceProportion!=0:
            sumProb-=cooccuranceProportion*math.log(cooccuranceProportion)*bitLogCoefficient;
    unrefinedWordEntropies[word1] = sumProb
    #print(word1+" "+str(sumProb)+" "+str(getAssociationMap.removePunctuation(text).lower().count(" "+word1+" ")))
  

  refinedWordEntropies: {str : float} = clusterTokens(text, unrefinedWordEntropies)
  refinedWordEntropies = clusterTokens(text, refinedWordEntropies)
  refinedWordEntropies = clusterTokens(text, refinedWordEntropies)

  sortedWordsByEntropy: [str] = []
  entropyThreshhold = 1000
  idxThreshhold = 0

  print(refinedWordEntropies)
  while len(sortedWordsByEntropy)<len(refinedWordEntropies)-1:
    maxEntropy: float = 0
    maxEntropyToken: str = ""
    maxEntropyIdx: int = 0
    placementIdx: int = 0
    idxForgiveness: bool = True
    for word in refinedWordEntropies:
      if (refinedWordEntropies[word]>maxEntropy and (refinedWordEntropies[word]<entropyThreshhold) or (refinedWordEntropies[word]==entropyThreshhold and placementIdx>idxThreshhold and idxForgiveness)):
        maxEntropy = refinedWordEntropies[word]
        maxEntropyToken = word
        maxEntropyIdx = placementIdx
        if (refinedWordEntropies[word]==entropyThreshhold and placementIdx>idxThreshhold):
          idxForgiveness = False
      placementIdx+=1
    entropyThreshhold = maxEntropy
    idxThreshhold = maxEntropyIdx
    sortedWordsByEntropy.append(maxEntropyToken)
  return sortedWordsByEntropy

def clusterTokens(text: str, unrefinedWordEntropies: {str : int}) -> {str : int}:
  refinedWordEntropies: {str: int} = {"__" : 0}
  cleanText: [str] = getAssociationMap.removePunctuation(text.lower()).split(" ")
  for word in unrefinedWordEntropies:
    refinedWordEntropies[word] = unrefinedWordEntropies[word]
  for targetWord in unrefinedWordEntropies:
    followingWords: {str: int} = {"__" : 0}
    for followingWordIdx in range(0, len(cleanText)-1):
      wordBeforeFollowingWord: str = ""
      followingWord: str = cleanText[followingWordIdx]
      if (followingWordIdx>0):
        wordBeforeFollowingWord = cleanText[followingWordIdx-1]
      wordAfterFollowingWord: str = cleanText[followingWordIdx+1]
      if (followingWord == targetWord) or (wordBeforeFollowingWord + " " + followingWord == targetWord):
        try:
          followingWords[wordAfterFollowingWord]+=1
        except:
          followingWords[wordAfterFollowingWord] = 1
    sumFollowing: int = 0
    for followingWord in followingWords:
      sumFollowing+=followingWords[followingWord]
    if sumFollowing>1:
      for followingWord in followingWords:
        if followingWords[followingWord] > .5*float(sumFollowing):
          try:
            refinedWordEntropies[targetWord+" "+followingWord] = unrefinedWordEntropies[followingWord]+unrefinedWordEntropies[targetWord]
          except:
            refinedWordEntropies[targetWord+" "+followingWord] = unrefinedWordEntropies[targetWord]
          try:
            if followingWords[followingWord] > .75*float(sumFollowing):
              refinedWordEntropies.pop(targetWord)
          except:
            pass
  return refinedWordEntropies