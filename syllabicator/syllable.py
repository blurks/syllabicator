import sys
import re

from syllabicator.trie import SuffixTree


default_vowels = r'aeiouyäöü'
default_consonants = r'bcdfghjklmnpqrstvwxzß'


def analyse(syl: str,
            vowels: str = default_vowels,
            consonants: str = default_consonants) -> dict:
    
    syllable_re = r'(?P<onset>[{c}]*)(?P<nucleus>[{v}]+)(?P<coda>[{c}]*)'.format(c=consonants, v=vowels)
    
    match = re.fullmatch(syllable_re, syl)
    
    if match:
        onset = match.group("onset")
        nucleus = match.group("nucleus")
        coda = match.group("coda")
        return {"onset": onset, "nucleus": nucleus, "coda": coda}
    else:
        return None


def parseFile(f: str) -> list[str]:
    l = []
    with open(f, "r") as fd:
        line = fd.readline()
        while line != "":
            syllables = re.split(r"[,.;\|]|[,.;\|]*\s", line)
            for s in syllables:
                syl = analyse(s.lower())
                if syl:
                    l += [syl]
            line = fd.readline()
    return l


def buildTreeFromList(syllables: list[dict]) -> SuffixTree:
    t = SuffixTree()
    for syl in syllables:
        t.insert(syl["onset"])
    return t


def analyseWord(word: str, onsets: SuffixTree) -> list:
    w = word.lower()
    m = re.findall(r'([{c}]*)([{v}]*)'.format(c=default_consonants, v=default_vowels), w)
    syllables = [{"onset": m[0][0], "nucleus": m[0][1], "coda": None}]
    for i in range(len(m)-1):
        syl1 = syllables[i]
        syl2 = {"onset": "", "nucleus": m[i+1][1], "coda": None}
        consonantstr = m[i+1][0]
        if syl2["nucleus"]:
            syl2["onset"] = onsets.longestMatch(consonantstr)
            syllables += [syl2]
            codalen = len(consonantstr) - len(syl2["onset"])
            syl1["coda"] = consonantstr[0:codalen]
        else:
            syl1["coda"] = consonantstr
            break


    return syllables


if __name__ == "__main__":
    wl = parseFile("wordlist2")
    t = buildTreeFromList(wl)

    for s in analyseWord("unterscheidung", t):
        print(s)
    print("----------")
    for s in analyseWord("überreaktion", t):
        print(s)
    print("----------")
    for s in analyseWord("verantwortung", t):
        print(s)
    print("----------")
    for s in analyseWord("mathematik", t):
        print(s)
    print("----------")
    for s in analyseWord("elektrische", t):
        print(s)
