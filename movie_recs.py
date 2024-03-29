from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import dotenv_values
import requests

# load environment file
config = dotenv_values(".env")

# get MongoDB connection string
uri = config["MONGO_URI"]

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client.sample_mflix
collection = db.movies

# count the documents in the collection
print("No. of documents: ", collection.count_documents({}))

# get hugging face inference token and space inference api
hf_token = config["HF_INFERENCE_TOKEN"]
embedding_url = config["HF_EMBEDDING_URL"]


# generate the embeddings using hf embedding url and token
def generate_embedding(text: str) -> list[float]:

    response = requests.post(
        embedding_url,
        headers={"Authorization": f"Bearer {hf_token}"},
        json={"inputs": text}
    )

    if response.status_code != 200:
        raise ValueError(f"Request failed with status code {response.status_code}: {response.text}")

    return response.json()


# generate embeddings for first 50 items
# ********************** uncomment below code if running for first time **********************
# for document in collection.find(({'plot': {"$exists": True}})).limit(50):
#     # add a column in collection
#     document['plot_embedding_hf'] = generate_embedding(document['plot'])
#     # replace the document in MongoDB with new collection
#     collection.replace_one({'_id': document['_id']}, document)


query = "Cartoon characters doing funny things"

# runs aggregation pipeline in MongoDB
results = collection.aggregate([
    {"$vectorSearch": {
        "queryVector": generate_embedding(query),
        "path": "plot_embedding_hf",
        "numCandidates": 100,
        "limit": 4,
        "index": "SemanticSearchMoviePlot",
    }}
])

for result in results:
    print(f'Movie Name: {result["title"]}, \nMovie Plot: {result["plot"]}\n')
