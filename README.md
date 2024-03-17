# Vector Embeddings using Hugging Face and Mongo DB

A mini vector embedding project using Hugging Face's [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) transformer model and MongoDB Atlas.

MongoDB Atlas's M0 Sandbox (Shared RAM, 512 MB Storage) free tier plan is used for the project.

MongoDB Atlas' search index functionality is used to 

Personal MongoDB Atlas details:
```
Org: Rishi's Org - 2024-03-15
Project: Project 0
Database: VectorEmbeddingCluster (sample_mflix dataset)
Collection: movies
```

## Environmental Variables

Below environment variables need to be saved in a .env file
```
1. MongoDB Connection String
2. Hugging Face Inference Token
3. Hugging Face Inference API
```

## MongoDB Atlas Setup
```
1. Create a MongoDB Atlas account
2. Create a project, select M0 free tier plan, and host it in AWS / Frankfurt (eu-central-1) region
3. Create a database for vector embeddings and populate it with sample_mflix dataset
4. Security > Database Access > copy username and password
5. Go to the database: Connect database > Drivers > copy connection string
6. Paste the username and password into connection string and store it in .env file
```

## Hugging Face Setup
```
1. Login to Hugging Face account
2. Go to settings > Access Token > Create new token
3. Copy and paste the token in .env file
```

## MongoDB Atlas Search Index Setup
```
1. Go to Database > VectorEmbeddingCluster > Atlas Search > Create Search Index
2. Select JSON editor > next > select movies collection inside sample_mflix dataset
3. Name the index as SemanticSearchMoviePlot
4. Enter the below JSON code > create search index
5. Once the search index is active run the deploy command in terminal
```

```json
{
  "mappings": {
    "dynamic": true,
    "fields": {
      "plot_embedding_hf": {
        "dimensions": 384,
        "similarity": "dotProduct",
        "type": "knnVector"
      }
    }
  }
}
```

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the packages.
Run the setup file [setup.sh](https://github.com/rishi-srinivasan/text-to-sql-llm/blob/main/setup.sh) to create .env file.

The setup file also installs the requirements from [requirements.txt](https://github.com/rishi-srinivasan/vector-embeddings-mongo-hf/blob/main/requirements.txt) file.

```bash
sh setup.sh
```
## Deploy

```python
python3 movie_recs.py
```

## Thanks
[Free Code Camp](https://www.freecodecamp.org/)

[Hugging Face](https://huggingface.co/)