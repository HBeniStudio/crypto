import block
import validation

blockchain = [block.genesis()]

last_block = blockchain[-1]

chain_size = 10

for i in range(0,chain_size):
    next_block = block.create_block(last_block,"null")
    blockchain.append(next_block)
    last_block = next_block

print(blockchain[0].data)
validation.validation(blockchain)