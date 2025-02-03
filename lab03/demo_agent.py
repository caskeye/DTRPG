from ollama import chat

model = 'llama3.2:3b'
messages = [
  {'role': 'system', 'content': 'You are an AI assistant.'},
]
options = {'temperature': 0.5, 'max_tokens': 100}

while True:
  message = {'role': 'user', 'content': input('You: ')}
  messages.append(message)
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'Agent: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  if message['content'] == '/exit':
    break