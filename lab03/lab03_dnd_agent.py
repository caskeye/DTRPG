from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Bryan Caskey'
model = 'llama3.2:3b'
options = {'temperature': 1.2,
           'top_p': 0.5}
messages = [{'role': 'system', 'content': 'You are a Dungeon Master of a D&D campaign. Your job \
                          is to provide the player with a detailed description of the current \
                          scenario they are in, and provide them with options for how they want\
                          to interact with the world.'},
            {'role': 'assistant', 'content': 'You are a D&D player who is playing a character \
                          named "Thonk the Large" in the "Hoard of the Dragon Queen" campaign.'}]


# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  print(f'Dungeon Master: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})

  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)

  # But before here.
  if messages[-1]['content'] == '/exit':
    break

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

