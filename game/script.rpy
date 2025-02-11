# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define leib = Character("Micaleib")
define wilhelmina = Character("Wilhelmina", who_color="#ff7f50")
define ronnie = Character("Ronnie", who_color="#FFFF00")
define katinka = Character("Katinka", who_color="53624A")


# The game starts here.
init:
    transform flip:
        xzoom - 1.0

    transform flip_right:
        flip
        xalign 1.0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    leib "uuuggg..."
    leib "uuuggg..."
    leib "my head hurts... "

    scene bg sand-crash with dissolve
    show bg sand-crash at truecenter

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.


    leib "I remember now, the car, the portal.."
    leib "my name is leib, and I am the time traveler"
    show micaleib rags  # at right <--- used to display left, right or center

    leib "but where am I...."

    show micaleib rags at left

    leib "A dessert maybe?"

    "Look around you"

    leib "huh?"

    "AROUND YOU" with vpunch
    show wilhelmina_yas_queen_2 at flip_right

    leib "who are you??"
    wilhelmina "I am shocked you don't recognize me.. haha"
    wilhelmina "I am wilhelmina"
    wilhelmina "Princess of orange"
    wilhelmina "and you have traveled into my world now. Tell me, what is the last thing you remember?"

    leib "I... I don't know.. maybe.. ah yes"
    leib "I was fighting the king of ... "
    leib "oh my god.."

    wilhelmina "don't worry my love, I hate him as much as you."

    show bg mountains at truecenter with dissolve

    wilhelmina "Here in this world we call him the __dark__ prince of orange, he is no king here.."

    leib "Where are we?"

    wilhelmina "we are safe here"
    wilhelmina "you are free now, but know that in due time I will need your help"
    wilhelmina "go, find ronnie, and kill the dark prince of orange"

    hide wilhelmina_yas_queen_2 at flip_right

    leib "it's gorgeous out here"
    leib "wait.. whats that"
    leib "..." with vpunch

    show bg twice-the-fun with dissolve

    leib "it can't be.. there were destroyed in the long lost year 2001"
    leib "also... there are 4 of them here?!" with vpunch

    leib "I have a bad feeling about this"
    leib "But first, I need to start searching for a guy call ronnie.. whoever that might be"

    show bg forest
    hide micaleib rags
    "and so the journey embarked.."
    "it would be long journey"
    "it would not take long before our hero encountered a mysterious figure in the woods"

    show micaleib rags at left
    show rietman_boss at right

    ronnie "hold it there champ, who are you"
    leib "I am leib, who are you?"
    ronnie "it's not important, I can get things fixed for you, just tell me what you need"
    leib "I need to find the closest arab around, I have a feeling something bad will happen"
    ronnie "a blackie ay?"
    leib "no, an ARAB" with vpunch
    ronnie "if that is what you want ..."
    leib "WAIT"
    ronnie "what's that?"
    leib "I will also need a menora..  I can't do my godly duties witout one"
    ronnie "you got it champ"

    hide rietman_boss
    show bg airplane

    leib "hmmm.. nothing seems out of the ordinary..."
    "ALLAH-U-AKBAHR" with vpunch
    show terrorists at right

    leib "hold it there you middle-eastern assholes"
    "leib picks up his menora and throws it at them"
    hide terrorists

    leib "I can't believe that just worked.."

    "and so leib defeated 2 dumb arabs and prevented a double 911"
    "only time will tell what the future has in store for this world.. now that micaleib has started to return..."

    show bg whitehouse
    show katinka_uitnodigend at right

    katinka "oh hero, my brave warrior..."
    katinka "thank you for saving America <3<3"
    katinka "take me as your wife, please please please"

    leib ".."
    leib ".."
    leib "no"
    leib "I will take you as my sex doll" with vpunch

    katinka ".." with vpunch
    "and they lived happily after after"


    # This ends the game.
    return
