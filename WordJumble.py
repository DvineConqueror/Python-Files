import random
def choose():
    getWord = ['ankle', 'uncle','pray','hero','turn','important','dash','jumble','zero']
    pick = random.choice(getWord)
    return pick

def jumble(word):
    random_word = random.sample(word, len(word))
    jumble_word = ''.join(random_word)
    return jumble_word

print("Jumbled Word Guess")
picked_word = choose()
while True:
    qn = jumble(picked_word)
    print(f"Jumbled Word is: {qn}")
    word = input("Guess the word: ")
    if word == picked_word:
        print(f"Congrats! You guessed the word: {picked_word}")    
    choice = input("Do you want to continue(Yes or No): ")
    if choice.lower() != "yes":
        print("Thank you for buying our drinks!")
        break
    else:
        continue
    
