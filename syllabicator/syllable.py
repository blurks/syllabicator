import re

default_vowels = r'aeiouy'
default_consonants = r'bcdfghjklmnpqrstvwxz'

def analyse_syllable(syl: str, vowels = default_vowels,
                     consonants = default_consonants) -> dict:
    syllable_re = r'(?P<onset>[{c}]*)(?P<nucleus>[{v}]+)(?P<coda>[{c}]*)'.format(c=consonants, v=vowels)
    match = re.fullmatch(syllable_re, syl)
    if match:
        onset = match.group("onset")
        nucleus = match.group("nucleus")
        coda = match.group("coda")
        return {"onset": onset, "nucleus": nucleus, "coda": coda}
    else:
        return None

    
    
