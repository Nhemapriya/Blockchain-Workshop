# sys.argv command line argument
import sys
import hashlib
from time import gmtime, strftime
import pickle
#Define the class for block creation
#Creation of Block to store details related to journals
class userBlock:
  def __init__(self, userId, prevBlockHash,userData):
    self.userId = userId
    self.prevBlockHash = prevBlockHash
    self.userData = userData
    self.blockHash = hashlib.sha256(self.prevBlockHash.encode()).hexdigest()
    self.time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

n = len(sys.argv)
#Basic blockchain
block = {}
myUserId = sys.argv[3]
block["firstName"] = sys.argv[1]
block["lastName"] = sys.argv[2]
block["userId"] = sys.argv[3]
block["userInstitution"] = sys.argv[4]
myData = pickle.dumps(block)

#create a block
myBlock = userBlock(block["userId"], hashlib.sha256(myUserId.encode()).hexdigest(),myData)
print("block created succesfully")
print("***Details***")
print(myBlock.blockHash)

