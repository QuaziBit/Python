# -----------------------------------------+
# Olexandr Matveyev                        |
# CSCI 107, Assignment 4                   |
# Last Updated: October 2, 2019            |
# -----------------------------------------|
# This program should print Lyrics from    |
# lyrics array and it have to avoid        | 
# printing similar lyric phrases.          | 
# All lyric phrases were provided          |
# as print statements.                     |
#                                          | 
# EXTRA:                                   |
#   I moved lyric phrases to the           | 
#   array because I was confused on how to | 
#   accomplish (Assignment 4) task without |  
#   using an array.                        | 
# -----------------------------------------+
# Taken from LyricFind.com                 |
# Lyrics by andrew taggart, chris martin,  |
# guy berryman, johnny buckland, will      |
# champion Sung by Coldplay                | 
# and Chainsmokers.                        | 
# -----------------------------------------+

# Array of lyric phrases
lyrics = [
    "I've been reading books of old", 
    "The legends and the myths", 
    "Achilles and his gold",
    "Hercules and his gifts",
    "Spiderman's control",
    "And Batman with his fists",
    "And clearly I don't see myself upon that list",
    "But she said, 'where'd you wanna go?'",
    "How much you wanna risk?",
    "I'm not looking for somebody",
    "I'm not looking for somebody",
    "I'm not looking for somebody",
    "With some superhuman gifts",
    "Some superhero",
    "Some fairytale bliss",
    "Just something I can turn to",
    "Somebody I can kiss",
    "I want something just like this",
    "Oh, I want something just like this",
    "Oh, I want something just like this",
    "Oh, I want something just like this",
    "Oh, I've been reading books of old",
    "The legends and the myths",
    "The testaments they told",
    "The moon and its eclipse",
    "And Superman unrolls",
    "A suit before he lifts",
    "But I'm not the kind of person that it fits",
    "She said, 'Where'd you wanna go?'",
    "How much you wanna risk?",
    "I'm not looking for somebody",
    "With some superhuman gifts",
    "Some superhero",
    "Some fairytale bliss",
    "Some fairytale bliss",
    "Just something I can turn to",
    "Somebody I can miss",
    "I want something just like this",
    "I want something just like this",
    "Oh, I want something just like this",
    "Oh, I want something just like this",
    "Where'd you wanna go?",
    "How much you wanna risk?",
    "I'm not looking for somebody",
    "With some superhuman gifts",
    "Some superhero",
    "Some fairytale bliss",
    "Just something I can turn to",
    "Somebody I can kiss",
    "I want something just like this",
    "Oh, I want something just like this",
    "Oh, I want something just like this",
    "Oh, I want something just like this"
    ]

# This function will print the lyric phrases
def printLyric():
    
    # i is loop counter
    i = 0

    # tmp is used to store previously printed lyric phrase
    tmp = ""

    # the while loop will loop via array of lyric phrases
    while i < len(lyrics):

        # here we testing if previously printed frye repeated
        # if it is repeated we will not print it
        # otherwise we will print it
        if tmp != lyrics[i]:
                print("%s" % (lyrics[i]) )

        # holding currently printed phrase      
        tmp = lyrics[i]

        # incrementing loop counter
        i = i + 1

    # END-WHILE

# END-FUNCTION 

# run this program
printLyric()
    


