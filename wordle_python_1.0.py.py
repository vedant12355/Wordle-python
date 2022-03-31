guess_word = "night"
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
yellow = []
blanks = ['_', '_', '_', '_', '_', ]
i = 0
ii = 0
red = []
correct = 'GGGGGG'
print("WORDLE")
print("The aim of this game is to a guess the five letter word in less than six tries.")
print("Enter a five letter word and press enter")
print("Beneath each letter will appear the letters R, Y or G")
print('"R" Means that the letter does not exist in the word')
print('"Y" Means that the letter is there in the word but in a different place')
print('"G" means that the letter is in the word and in the right place')
print('Note- I do not have the ability to ensure that you enter a word, or even to ensure that you have entered a five letter word,')
print('so the program will even view the most colorful words - for example $*@/$% - as a word')
outcomes = ['Dumb Luck!', 'Dumb Luck!', 'Eureka!', 'Brilliant!', 'Gottem', 'Ooph', 'Phew']
while ii<=5:
    word = input()
    score = []
    while i <= 4:
        guess_letter = guess_word[i]
        word_letter = word[i]
        remove_letter = word_letter.upper() + ', '
        if guess_letter == word_letter:
            score.append("G")
            blanks[i] = word_letter.upper()
            rl = word_letter.upper() + ', '
            if rl in yellow:
                yellow.remove(word_letter.upper() + ', ')
        elif guess_letter != word_letter and word_letter in guess_word:
            score.append("Y")
            remove_letter = word_letter.upper() + ', '
            if remove_letter in yellow:
                yellow[yellow.index(remove_letter)] = remove_letter
            else:
                yellow.append(remove_letter)
            if word_letter.upper() in blanks and remove_letter in yellow:
                yellow.remove(remove_letter)
        else:
            score.append("R")
            if remove_letter in red:
                red[red.index(remove_letter)] = remove_letter
            else:
                red.append(remove_letter)
        if i == 4:
            i = 0
            break
        else:
            i += 1
    score_joined = ''.join(score)
    yellow_joined = ''.join(yellow)
    red_joined = ''.join(red)
    print(score_joined)
    print('Guesses: '+ ''.join(blanks))
    print("'Y' letters: " + yellow_joined)
    print("'R' Letters:" + red_joined)
    ii += 1
    if score_joined == 'GGGGG':
        break
if score_joined != 'GGGGG':
    print("You didn't get it! The word was " + guess_word)
else:
    print(outcomes[ii])