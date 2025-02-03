# Prompt Engineering Process, by Bryan Caskey
## Creating and Fine tuning the Dungeon Master AI

### Step 1: Editing the system prompt and Initial setup.
#### Intention
>The first step for me was to tell the model that it is a Dungeon Master, and that the user is a player in it's campaign. Without this, I wouldn't be accomplishing much in the way of creating an AI Dungeon Master. I also chose a temperature value of 1.2 as I felt that the DM should be slightly more creative than normal.

#### Action/Change
>As this is the foundational change to the model, there isn't a previous version of the model to compare against.

#### Result
>The result was actually much more solid than I would have originally thought. The model immediately picked up on what it needed to do and begane creating stories. 

#### Reflection/Analysis of the result. 
>The change worked because it gave the AI the context it needed to act as a Dungeon Master

---

### Step 2: Having the DM speak first
#### Intention
>This change was simple. I want the DM to initiate the conversation, as this allows them to provide the scene description and current scenario to the player, and the player can decide what to do based off of it.

#### Action/Change
>The change allows for the player to know what is happening before they chose to act.

#### Result
>As expected.

#### Reflection/Analysis of the result.
>Works as expected. The process of communicating with the AI is smoother.

---

### Step 3: Trying other models
#### Intention
>I tried out the Deepseek-r1 model, as I thought that I might be able to get either better performance or better responses from it compared to llama3.2:3b.

#### Action/Change
>As the Deepseek-r1 model has more parameter count options, and my computer at home has the hardware capability to run larger models, I figure that I could try a higher parameter model to get better results.

#### Result
>The Deepseek-r1:1.5b model ended up having strangely formatted output compared to the llama3.2 model, and did not generate as coherent of a story as llama3.2, but was more performant. The Deepseek-r1:32b model was very descriptive in its output, but strangely ended up confused about its role, and was very slow to run.

#### Reflection/Analysis of the result. 
>I expected the 32 billion parameter model to be slow, so that makes sense. I don't know why it decided to switch role to be the player, but that did end up keeping me from sticking with it, as well as the serveral minute procesing time for responses. The 1.5 billion parameter model was very fast, as it should be with half the parameters, but I did not like it's output quality, so I ended up sticking with the llama3.2 model.

---

### Step 4: Altering the "top_p" model parameter
#### Intention
>I wanted to change the top_p model to make the model more coherent and stable in its output.

#### Action/Change
>While having the model be creative is important, if it can't keep track of the story, then it has failed at its job. According to [Ollama Documentation](https://github.com/ollama/ollama/blob/main/docs/modelfile.md), lowering the `top_p` parameter should have it generate more focused text, so I tried that.

#### Result
>The model seems much better at keeping track of the story now.

#### Reflection/Analysis of the result. 
>From my understanding, the `top_p` parameter affects the probability that various tokens will be considered, so this raises that bar so that less tokens are considered.

---

### Step 5: Altering the system prompt
#### Intention
>The last change I made was both fixing the formatting of my system prompt, and adding a clarifying statement to specify the capabilities that it should have as a Dungeon Master.

#### Action/Change
>Previous runs of the AI had left me feeling that the AI didn't understand the scope of what it should be doing as a DM, so I felt that clarifying its duties would improve the chat session.

#### Result
>I am pretty sure that it is better understanding its role as a DM. To check, I asked it at one point if I could review my character sheet, and it correctly paused the campaign and pulled up a very accurate character sheet from my perspective as a D&D player.

#### Reflection/Analysis of the result. 
>The change worked because the system prompt gave better context to how the AI should perform its role.