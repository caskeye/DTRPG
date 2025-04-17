from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from dndnetwork import DungeonMasterServer, PlayerClient
from llm_utils import TemplateChat
from proj.ragu import ChromaDBClient as rag


class DungeonMaster:
    def __init__(self):
        self.game_log = ['START']
        self.server = DungeonMasterServer(self.game_log, self.dm_turn_hook)
        self.chat = TemplateChat.from_file('util/templates/dm_chat.json', sign='hello')
        self.start = True
        self.chroma = rag.ChromaDBClient(
            collection_name='session_info',
            embedding_function=rag.OllamaEmbeddingFunction(model_name='nomic-embed-text')
        )

    def start_server(self):
        self.server.start_server()

    def dm_turn_hook(self):
        dm_message = ''
        # Do DM things here. You can use self.game_log to access the game log
        if self.start:
            dm_message = self.chat.start_chat()
            self.start = False
        else: 
            dm_message = self.chat.send('\n'.join(self.game_log))

        # Process the DM's message and update the game log
        self.chroma.add_documents([
            {
                'id': 'dm_message_' + str(len(self.game_log)),
                'text': dm_message,
                'metadata': {'role': 'dm'}
            }
        ])

        # Return a message to send to the players for this turn
        return dm_message 


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
