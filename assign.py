from english_words import english_words_set as words
import random

words = list(words)


def ran_word():
    word = random.choice(words)
    return word


def guess(word):
    print("Guess the word: ")
    length = len(word)
    print("_ "*length)


def difficulty(word):
    print("Levels of difficulty :-\n1.Easy\n2.Medium\n3.Hard")
    dif = int(input("Choose your option : \n").lower())
    if dif == 1:
        while len(word) > 3:
            word = ranWord()
    elif dif == 2:
        while 3 >= len(word) > 5:
            word = ranWord()
    elif dif == 3:
        while len(word) < 5:
            word = ranWord()
    else:
        print("No option available !!!\nOption are:\n1.Easy,2.Medium,3.Hard")
        quit()
    return word


if __name__ == "__main__":
    wrd = ran_word().lower()
    wrd = difficulty(wrd)
    guess(wrd)
    ans = "_"*len(wrd)
    ans = list(ans)
    ctr = 0
    nm = len(wrd)+3
    print("You have only", nm, "guesses")

    while True:
        if list(wrd) == ans:
            print("You Won !!!")
            break
        elif ctr == nm:
            print("You Lose ;((")
            print("The word was :", wrd)
            break
        gsWrd = input("Guess your letter from the word: \n").lower()
        if wrd.count(gsWrd) == 0:
            print("Wrong Guess !!!")
            print(" ".join(ans))
        else:
            print("Correct Guess :D")
            for x in range(len(wrd)):
                if gsWrd == wrd[x]:
                    ans[x] = gsWrd
            print(" ".join(ans))
        ctr += 1
        print(nm-ctr, "guesses remaining")
