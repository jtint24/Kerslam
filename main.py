#KERSLAM: Keyword Extraction and Recognition with Sentence Level Association Maps

import getKeywords #to use the getKeywords function

"""
main()

contains demos of the getKeywords function
"""
def main():
  print(getKeywords.getKeywords("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly procedural), object-oriented and functional programming. It is often described as a 'batteries included' language due to its comprehensive standard library. Guido van Rossum began working on Python in the late 1980s as a successor to the ABC programming language and first released it in 1991 as Python 0.9.0. Python 2.0 was released in 2000 and introduced new features such as list comprehensions, cycle-detecting garbage collection, reference counting, and Unicode support. Python 3.0, released in 2008, was a major revision that is not completely backward-compatible with earlier versions. Python 2 was discontinued with version 2.7.18 in 2020. Python consistently ranks as one of the most popular programming language. Python was conceived in the late 1980s[42] by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to the ABC programming language, which was inspired by SETL,[43] capable of exception handling and interfacing with the Amoeba operating system.[13] Its implementation began in December 1989.[44] Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his 'permanent vacation' from his responsibilities as Python's 'benevolent dictator for life', a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker.[45] In January 2019, active Python core developers elected a five-member Steering Council to lead the project.[46][47]. Python 2.0 was released on 16 October 2000, with many major new features.[48] Python 3.0, released on 3 December 2008, with many of its major features backported to Python 2.6.x[49] and 2.7.x. Releases of Python 3 include the 2to3 utility, which automates the translation of Python 2 code to Python 3.[50] Python 2.7's end-of-life was initially set for 2015, then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3.[51][52] No further security patches or other improvements will be released for it.[53][54] With Python 2's end-of-life, only Python 3.6.x[55] and later were supported. Later, support for 3.6 was also discontinued. In 2021, Python 3.9.2 and 3.8.8 were expedited[56] as all versions of Python (including 2.7[57]) had security issues leading to possible remote code execution[58] and web cache poisoning.[59] In 2022, Python 3.10.4 and 3.9.12 were expedited[60] and so were older releases including 3.8.13, and 3.7.13 because of many security issues.[61] When Python 3.9.13 was released in May 2022, it was announced that the 3.9 series (joining the older series 3.8 and 3.7) will only receive security fixes going forward.[62] On September 7, 2022, four new releases were made due to a potential denial-of-service attack: 3.10.7, 3.9.14, 3.8.14, and 3.7.14.[63][64]. Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including metaprogramming[65] and metaobjects [magic methods] ).[66] Many other paradigms are supported via extensions, including design by contract[67][68] and logic programming.[69] Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management.[70] It uses dynamic name resolution (late binding), which binds method and variable names during program execution. Its design offers some support for functional programming in the Lisp tradition. It has filter,map and reduce functions; list comprehensions, dictionaries, sets, and generator expressions.[71] The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.[72] Its core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:[73] Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Readability counts. Rather than building all of its functionality into its core, Python was designed to be highly extensible via modules. This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.[42] Python strives for a simpler, less-cluttered syntax and grammar while giving developers a choice in their coding methodology. In contrast to Perl's 'there is more than one way to do it' motto, Python embraces a 'there should be one—and preferably only one—obvious way to do it' philosophy.[73] Alex Martelli, a Fellow at the Python Software Foundation and Python book author, wrote: 'To describe something as 'clever' is not considered a compliment in the Python culture.'[74] Python's developers strive to avoid premature optimization and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity.[75] When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C; or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter. "))
  # print(getKeywords.getKeywords("A team of two ASU students won the Red Bull Basement 2021 global competition after becoming finalists in the program last December. Freshmen Brinlee Kidd and Sylvia Lopez won the competition with their note-taking platform, Jotted, which is expected to launch within the next six months. The competition concluded at the end of March and aimed to help students develop product ideas.Kidd, who is majoring in informatics and minoring in technology entrepreneurship and management, and Lopez, who is majoring in industrial engineering and minoring in secondary education, were supposed to go to Istanbul in December 2021 to begin a five-week development phase of their product eventually leading to the final round. But due to COVID-19, the program was pushed back to March 2022 and condensed to six days.Throughout the finals, the team worked with a number of experts and professionals in the technology and education field to help grow their product. The team used Q&A sessions held by the experts to help change and advance the original pitch for the final round of the competition. The Jotted team changed much of its original prototype after the consultations and workshops, including switching the product from an app to a browser-based platform. Lopez and Kidd said making the product browser-based would improve it for the audience they are trying to reach. “A lot of the shifting we made, whether it was small things or big things like switching to a browser, was something we realized would be better for students,” Lopez said. “A lot of it has been based on taking a step back and thinking about it on a student level.” While Kidd and Lopez originally went into the finals with a pitch they believed would be their final one, they said the competition helped them understand the product better and communicate their passion for education with Jotted. “We decided to incorporate our personalities as founders, partners, people and university students into (the pitch) more instead of more business or professional,” Lopez said. “As we saw the vibe of what it was going to look like, we adjusted accordingly.”"))
  # print(getKeywords.getKeywords("Graham’s number is a whole number, but it’s so ridiculously large that you can’t even comprehend its value. If you tried to write down Graham’s number, you could not, because the number of digits in it, say there are a of them, is so large that there’s not enough space in the observable universe to write down them all. Even if each digit took up a Planck-volume sized region of space (a Planck volume is orders of magnitude smaller than a proton, and that’s an understatement), there would still be too many digits to be contained in the observable universe. In fact, even a, which is the number of digits in Graham’s number, is itself so large that you could not write it down, because the number of its digits, say there are b of them, is so large that there aren’t enough Planck volumes in the observable universe to contain them all. In fact, even b is a number so large that you could not write out its digits (say there are c of them). This process continues for a number of times so large that even the number of times this process repeats exceeds the number of Planck volumes in the observable universe. This blew my mind when I learned it, so just sharing it any fellow math nerds out there. (If you’re having trouble imagining this, suppose some really large number N has a million digits (let a be 1,000,000). Then in a very small universe containing fewer than a million Planck volumes, you could not write down N because it has too many digits. But, you could write down a itself (which is 1,000,000), because it only has 7 digits (let b be 7, and since b has one digit, let c be 1). Well, Graham’s number is so large that this sequence of variables a, b, c, d, …, is too large to even fit in the universe"))
  # print(getKeywords.getKeywords("From Heian Japan to medieval France, the differences between men and women have dominated literary discourse. With a binary opposition being defined as a pair of related concepts with antipodal meanings, it is easy to see how classical discourse has centered around the idea that the two genders exist as opposites, each serving as the antithesis of its counterpart. After all, pitting the genders against each other undeniably allows for a more unambiguous division of societal groups and—historically—has facilitated an unmistakably unequal distribution of power. Sei Shōnagon, in her novel The Pillow Book, decides to embrace this binary perception of gender, highlighting the differing natures of men and women and using these to determine the behaviors appropriate for a member of each group. Viewing the issue from a different perspective, Christine de Pizan issues a harsh rebuke of all attempts to utilize gender as a discriminant when ascertaining social utility, and her efforts serve to blur established divisions of gender and redefine what it means to be masculine or feminine. In The Pillow Book, Sei Shōnagon assigns behavior codes to men and women in order to affirm the binary opposition of the two genders and advocate for a gender-specific method of conduct centered around male chivalry and female refinement; this is in stark contrast to The Book of the City of Ladies, in which Christine de Pizan challenges the binary nature of gender—through allusions to mythological and historical female figures—in an effort to contradict the notion that men and women occupy the predetermined social roles of scholarly husband and subservient wife."))
  print("got keywords!")


main()