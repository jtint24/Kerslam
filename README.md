<img src="https://user-images.githubusercontent.com/89891042/155621540-1b1e7c33-72d5-408e-9652-d87b5b13592b.png" width="200" height="120" align="right" />

# Kerslam
KERSLAM stands for Keyword and Entity Recognition with Sentence-Level Association Maps. KERSLAM is a simple, fast, and novel way to perform keyword extraction on texts by simulating translational entropy calculation. KERSLAM's getKeywords() function returns an array of keywords in the text, sorted by how relevant they are to the text's meaning. KERSLAM is able to intelligently pull keywords that are single tokens or n-grams, and sort them to users.

[![Current Release Version](https://img.shields.io/github/release/jtint24/Kerslam.svg?style=flat-square&logo=github)](https://github.com/jtint24/Kerslam/releases)

## How to Use it?

KERSLAM is extremely simple to use. Once the relevant files are in the correct directory, KERSLAM can be imported like so:

`import getKeywords`

Then, keywords and entities can be obtained from a text by using the following function:

`getKeywords.getKeywords(text)`

which takes the text as a string and returns an array of keywords and entities sorted in descending order by significance.

## How Does it Work?

### Simulating Translational Entropy

KERSLAM simulates the calculation of translational entropy, a way of calculating how many bits of information a word contains in context. This works by comparing words in a bitext, a corpus which has a translation into a different language. Words that have many possible translations tend to carry a lot of meaning. Words that have few common translations tend to have less meaning. To find the word's meaning in bits, the following formula is applied to the distribution of possible translations, <img src="https://render.githubusercontent.com/render/math?math=T">:

<img src="https://render.githubusercontent.com/render/math?math=H(T) = -\sum_{t \in T}P\left(t\right)\log_{2}\left(P\left(t\right)\right)">

Translational entropy is one of the most effective ways of calculating the semantic content of words [^1], but finding it computationally is extremely difficult, even with a bitext, which is itself quite arduous to create. KERSLAM sidesteps this issue by substituting the distribution of *translations* for a word with the distribution of *related* words, two closely-related distributions. This distribution of related words is created by measuring token co-occurance. This is computationally very cheap, and allows for parsing of large documents relatively quickly. AssociationMaps, which are map structures designed to represent associations within texts, are created at this stage, and statistics from them are used to find entropies for individual words. However, the translational entropy calculation is just the first step in keyword extraction.

### Refining Keywords

Once translational entropy has been calculated for each unique word in a text, individual words are clustered into n-grams. This is done by applying a Markovian model over the text. Words that commonly form n-grams of each other are recorded, and the translational entropy of the n-gram is found from the entropies of the constituent words. N-grams up to size 4 are recorded as keywords; larger n-grams are rarely used as keywords and are likely just artifacts. After this, function words are filtered from the list of keywords, though not from inside n-grams. This is a quality assurance measure that also greatly refines the final set of keywords returned. This creates the final list of keywords sorted by entropy, which is then given to the user.

[^1]: ["Measuring Semantic Entropy," I. Dan Melamed](https://aclanthology.org/W97-0207.pdf)
