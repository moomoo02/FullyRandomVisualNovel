# Kirito and Bocchi's Visual Novel
# Written by OpenAI Assistant

# Declare the characters
define s = Character('Kevin', color="#8888FF")
define t = Character('JoJo', color="#FF8888")

# Set the background image
image bg school = "bg classroom.png"

# Declare the emotion images
image t_happy = "zeil happy.png"
image t_neutral = "zeil normal.png"
image t_sad = "zeil sad.png"
image t_smug = "zeil smug.png"
image t_laugh = "zeil laugh.png"

# Start the novel
label start:
    show bg school
    show t_neutral
    s "Hey, Jojo. What's up?"
    show t_neutral
    t "Nothing much, Kevin. Just trying to avoid people as usual."
    s "Why do you always try to avoid people? You're such a tsundere."
    show t_sad
    t "I-I'm not a tsundere! I just don't like being around people, okay?"
    s "Sure, sure. So, do you want to hang out after school today?"
    show t_neutral
    t "I don't know... I have a lot of homework to do."
    s "Come on, JoJo. It'll be fun. We can go to the arcade or something."
    show t_neutral
    t "F-Fine. But just for a little while, okay?"
    s "Great! I'll meet you at the entrance after school."
    show t_neutral
    t "O-Okay..."
    return