# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:
    scene bg classroom
    "Rin Tohsaka is standing in the classroom, leaning against a tree and looking at her phone. She appears to be deep in thought, oblivious to the commotion around her."
    show zeil angry
    "Rin Tohsaka" "Ugh, I can't believe I have to put up with those arrogant pre-med students again. They think they're so much better than everyone else just because they're going to be doctors someday."
    "The protagonist approaches, not noticing Rin at first.  He has a confident air about him, but there is a hint of sadness in his eyes."

label sprites:
    "Protagonist"  "Man, I can't wait to get out of this place. I was hoping to become a doctor, but it looks like I'm going to have to settle for something else. Still, I won't let that hold me back. I'll show everyone that I'm just as good as those pre-med snobs."
    show zeil annoyed
    "Rin notices the protagonist and scowls, crossing her arms over her chest."
    "Rin Tohsaka" "What do you want, (protagonist's name)?"
    "Protagonist" "Huh? Oh, it's you, Tohsaka. I didn't see you there."
    "Rin Tohsaka" "Gee, what a surprise. You're always so focused on yourself, you never notice anyone else."
    return
