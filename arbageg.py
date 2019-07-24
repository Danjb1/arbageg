import random
import re
import sys

def applyOffset(word, offset):
    if word[0].isupper():
        # Preserve proper case
        word = word.lower()
        word = word[:offset] + word[offset].upper() + word[offset + 1:]
    return word[offset:] + word[:offset]

def calculateScore(word, newWord):
    # Start with a high score, and penalise bad letter patterns
    score = 1000

    # Word is unchanged
    if (word == newWord):
        score -= 10

    # 3 consecutive vowels
    match = re.search('[aeiou]{3}', newWord)
    if match:
        score -= 9

    # 3 consecutive consonants
    match = re.search('[bcdfghjklmnpqrstvwxyz]{3}', newWord)
    if match:
        score -= 8

    # Word ends in 2 hard consonants
    match = re.search('[bdghjkmpqtvxz]{2}$', newWord)
    if match:
        score -= 7

    # Word ends in an unlikely letter
    match = re.search('[chijquv]$', newWord)
    if match:
        score -= 6

    return score

def garbagize(word):

    # Preserve any trailing punctuation
    punctuation = ''
    if re.match('[!?,.]', word[len(word) - 1]):
        punctuation = word[-1:]
        word = word[:-1]

    # Try each possible offset, and choose the best one
    bestWord = word
    bestScore = -1
    for i in xrange(len(word)):
        newWord = applyOffset(word, i)
        score = calculateScore(word.lower(), newWord.lower())
        if score > bestScore:
            bestWord = newWord
            bestScore = score

    return bestWord + punctuation

def main():
    input = sys.argv[1].split()
    newWords = []
    for word in input:
        newWord = garbagize(word)
        newWords.append(newWord)
    print ' '.join(newWords)

if __name__ == '__main__':
    main()
