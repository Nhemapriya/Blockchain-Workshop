#Required Import statements
import sys
import hashlib
from time import gmtime, strftime
import pickle
import json

#class for block creation
class userBlock:
  def __init__(self, userId, prevBlockHash,userData):
    self.userId = userId
    self.prevBlockHash = prevBlockHash
    self.userData = userData
    self.blockHash = hashlib.sha256(self.prevBlockHash.encode()).hexdigest()
    self.time = strftime("%Y-%m-%d %H:%M:%S", gmtime())

#Get and parse user input from command line
journalDict = {}
for arg in sys.argv[1:]:
    if '=' in arg:
        sep = arg.find('=')
        key, value = arg[:sep], arg[sep + 1:]
        journalDict[key] = value

#Block creation
#obtain journalID to hash
journalId = journalDict["journalId"]
#parse the entire journalData
userData = pickle.dumps(journalDict)
#create a block
myBlock = userBlock(journalDict["journalId"], hashlib.sha256(journalId.encode()).hexdigest(),userData)
#display details
print("***Block created succesfully***")
print("-------------Details----------------")
print("Block Hash => ", myBlock.blockHash)
print("Timestamp of creation => ", myBlock.time)
print("*Block Id => ", myBlock.userId)

print(journalDict)

#sample dictionary (keys and values)
    # "journalId" : "Tech241",
    # "journalName" : "Elseiver",
    # "journalDomain" : "Nanotech",
    # "journalTitle" : "Brain image segmentation",
    # "journalScope" : "Science and technology",
    # "publishedBy" : "Academy of honours",
    # "publicationFrequency" : "Bi-annual",
    # "publicationStatus" : "Available",
    # "publicationProceedings" : "AnnexureOne",
    #  "majorPublications" : ["ABC", "XYZ", "PQR"],

    # "authorDetails" :{
    #     "authorId" : "AUTH01",
    #     "authorName": "hema",
    #     "authorDesignation" : "Professor",
    #     "authorInstitutionalEmail": "hema@stjosephs.in",
    #     "authorPersonalEmail" : "hemuhema2000@gmail.com",
    #     "authorInstitution" : "St joseph's college of engineering",
    #     "authorQualification" : "PhD in science",
    #     "isbnNumber" : "23415",
    #     "orchidId" : "Hema151220",
    #     "numberOfPublications" : "12",
    # }

#Multiple userInput
mainBlockDirectory = []
def getMultipleArgs():
    journalList = []
    n = len(sys.argv)
    for loop in range(1,n):
        journalList.append(sys.argv[loop])

    for data in journalList:
        parseData = json.dumps(data)
        mainBlockDirectory.append(parseData)
    