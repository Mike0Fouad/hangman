#words for hangman game depending on levels
import random
# lists of words for each difficulty
easy_words = ["apple", "banana", "cat", "dog", "elephant", "flower", "guitar", "house", "igloo", "jacket",
              "kite", "lemon", "mouse", "notebook", "orange", "pencil", "quilt", "rabbit", "sun", "turtle",
              "umbrella", "violin", "watermelon", "xylophone", "zebra", "bicycle", "candle", "duck", "eagle",
              "fish", "grape", "hat", "ice cream", "jellybean", "kangaroo", "leopard", "moon", "nest", "ocean",
              "panda", "queen", "rainbow", "snake", "tiger", "umbrella", "volcano", "whale", "xylophone"]

medium_words = ["butterfly", "chocolate", "dolphin", "elephant", "football", "hamburger", "kangaroo", "landscape", "mountain", "parrot",
                "basketball", "cheetah", "dandelion", "eclipse", "fireworks", "giraffe", "helicopter", "island", "jackal", "kangaroo",
                "lighthouse", "mountain", "nightingale", "octopus", "penguin", "quokka", "rhinoceros", "skyscraper", "toucan", "umbrella",
                "volleyball", "whale", "xenophobe", "yacht", "zeppelin", "albatross", "bison", "camel", "dachshund", "elephant",
                "flamingo", "gazelle", "hedgehog", "iguana", "jaguar", "koala", "lemur", "meerkat", "narwhal", "opossum"]

hard_words = ["acquaintance", "bewilderment", "cryptocurrency", "discombobulate", "exacerbate", "gobbledygook", "labyrinthine", "mnemonic", "quizzaciously", "sesquipedalian",
              "antidisestablishmentarianism", "circumlocution", "deoxyribonucleic", "epistemology", "floccinaucinihilipilification", "gubernatorial", "hippopotomonstrosesquipedaliophobia", "incomprehensibility", "jurisprudence", "kaleidoscope",
              "logorrhea", "magnanimous", "nihilism", "onomatopoeia", "pneumonoultramicroscopicsilicovolcanoconiosis", "quintessential", "recalcitrant", "serendipity", "tyrannosaurus", "ubiquitous",
              "verisimilitude", "wunderkind", "xerophthalmia", "yoctosecond", "zeitgeist", "abracadabra", "ballyhoo", "cacophony", "dodecahedron", "ephemeral",
              "facetious", "gobbledygook", "hodgepodge", "jejune", "kaleidoscope", "labyrinthine", "mnemonic", "onomatopoeia", "peregrinate", "quizzaciously"]
# function to choose a random word from the list of words depending on the difficulty
def rand_word(difficulty):
    choosen=""
    if difficulty== "easy":
        choosen=easy_words[random.randint(0,len(easy_words)-1)]
    elif difficulty== "medium":
        choosen=medium_words[random.randint(0,len(medium_words)-1)]
    elif difficulty == "hard":
        choosen=hard_words[random.randint(0,len(hard_words)-1)]
    else:
        print("pls select a proper difficulty from the choices")
    return choosen
# function to convert a list into a string
def stringfy(list):
    string=""
    for i in range (len(list)):
        string+=list[i]
    return string
def spaced(string):
    spaced=""
    for i in range(len(string)):
        spaced+= string[i]+" "
    return spaced
        
        
# function to hide the word
def hide_word(word):
    hidden=""
    for i in range(len(word)):
        hidden+="_"
    return hidden

        
