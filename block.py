import hashlib as hasher
import datetime as date


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        print("creating a block")
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.hash_block()
        print(f"created block #{self.index} with hash: {self.hash} at {self.timestamp}")

    def hash_block(self):
        sha = hasher.sha256()
        block_content = (
                str(self.index) +
                str(self.timestamp) +
                str(self.data) +
                str(self.previous_hash)
        )
        sha.update(block_content.encode('utf-8'))
        return sha.hexdigest()

def genesis():
    return Block(0,date.datetime.now(),"Hello BlockChain", 0)

def create_block(last_block,data):
    index = last_block.index + 1
    timestamp = date.datetime.now()

    return Block(index,timestamp,data,last_block.hash)