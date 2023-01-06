import os
#import openai
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
print(OPENAI_API_KEY)
# openai.api_key = os.getenv(OPEN_AI_API_KEY);

# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="Give me a setting for an anime girl date\n\nThe two anime girls are meeting up at a small cafe near the beach. The sun is setting and they can hear the waves crashing against the shore in the distance. They sit down together, chatting about their favorite animes and sharing stories of their own lives. As they talk, they enjoy some snacks from the cafe like ice cream or pastries. After finishing their treats, they take a walk along the beach and watch as the sun sinks below the horizon.",
#   temperature=0.6,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=1,
#   presence_penalty=1
# )
