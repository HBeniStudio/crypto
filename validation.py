

def validation(blockchain):

    for i in range(len(blockchain)):
        if blockchain[i].hash != blockchain[i].hash_block():
            print(f"Block {blockchain[i].index} has been modified!")
            return False

        if i > 0:
            if blockchain[i].previous_hash != blockchain[i -1].hash:
                print(f"Block {blockchain[i].index} has an incorrect previous hash!")
                return False

    print("Blockchain is valid!")
    return True