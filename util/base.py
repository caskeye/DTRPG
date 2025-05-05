from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from dndnetwork import DungeonMasterServer, PlayerClient
from llm_utils import TemplateChat, tool_tracker
from proj.ragu import ChromaDBClient as chroma, OllamaEmbeddingFunction


class DungeonMaster:
    def __init__(self):
        self.game_log = ['START']
        self.server = DungeonMasterServer(self.game_log, self.dm_turn_hook)
        self.chat = TemplateChat.from_file('proj/templates/dm_chat.json', 
                                           sign='hello',
                                           process_response=TemplateChat.process_response,
                                           dungeon_master=self)
        self.start = True
        self.rag = chroma(
            collection_name='session_info',
            embedding_function=OllamaEmbeddingFunction(model_name='nomic-embed-text')
        )

    def start_server(self):
        self.server.start_server()

    def dm_turn_hook(self):
        dm_message = ''
        
        # Do DM things here. You can use self.game_log to access the game log
        print(f"[DEBUG] DM Starting Turn")
        if self.start:
            dm_message = self.chat.start_chat()
            self.start = False
        else: 
            dm_message = self.chat.send('\n'.join(self.game_log))
        
        # Process the DM's message and update the game log
        self.rag.add_documents([
            {
                'id': 'dm_message_' + str(len(self.game_log)),
                'text': dm_message,
                'metadata': {'role': 'dm'}
            }
        ])

        print(f"[DEBUG] session_info: {self.rag.peek()}")

        # Return a message to send to the players for this turn
        return dm_message 
    
    

    @tool_tracker
    def process_function_call(self, function_call):
        name = function_call.name
        args = function_call.arguments

        if hasattr(self, name):
            method = getattr(self, name)  # Get the method by name
            return method(**args)  # Call the method with the provided arguments
        else:
            raise AttributeError(f"Method '{name}' not found in DungeonMaster.")
    
    #Tool
    def retrieve_session_info(self, query: str = "search") -> str:
        print(f'[DEBUG] retrieve_session_info called with query: {query}')
        documents = self.rag.query(query, 1)
        print(f'[DEBUG] Retrieved documents: {documents}')
        return "\n".join(documents[0])
        pass



class Player:
    def __init__(self, name):
        self.name = name
        self.client = PlayerClient(self.name)

    def connect(self):
        self.client.connect()

    def unjoin(self):
        self.client.unjoin()

    def take_turn(self, message):
        self.client.send_message(message)



