from pathlib import Path
from dotenv import load_dotenv
import os

# Load .env from project root (vector-db/.env)
env_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path=env_path)

# Ollama settings
OLLAMA_URL = os.getenv('OLLAMA_URL', 'http://localhost:11434/api/embeddings')
OLLAMA_MODEL = os.getenv('OLLAMA_MODEL', 'nomic-embed-text')
OLLAMA_API_KEY = os.getenv('OLLAMA_API_KEY')

# MongoDB
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017')
