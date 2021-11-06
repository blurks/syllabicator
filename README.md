# Syllabicator

A simple program for breaking down words into syllables using the
maximal onset principle (citation needed).  Training data of
syllabicated words is used to build up a trie of maximal onsets, which
is then used to break down words into syllables.  A syllable is
divided into an onset, a nucleus and a coda.

The program is designed to work on phonetic transcriptions, but you
also should get decent results for orthographic data from languages
where orthography is closely to pronunciation.
[wordlist2](./wordlist2) is an example of German orthographic training
data (Source: https://de.wikipedia.org/wiki/Trie).


## Usage examples

Sample analyses using the training data from [wordlist2](./wordlist2):
```sh
python -m syllabicator.syllable
```

Running tests:
```sh
python -m unittest
```


## TODO

* proper cli
* tests for syllable.py
* get proper training data
