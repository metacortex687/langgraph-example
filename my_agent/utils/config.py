import os
from pathlib import Path

# Get the project root directory (where .env is located)
ROOT_DIR = Path(__file__).parent.parent.parent

# Read .env file directly
env_path = ROOT_DIR / ".env"
if env_path.exists():
    with open(env_path) as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                os.environ[key] = value

# Get API keys
XAI_API_KEY = os.getenv("XAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

print("Current working directory:", os.getcwd())
print("Project root directory:", ROOT_DIR)
print("XAI_API_KEY loaded:", "Yes" if XAI_API_KEY else "No")
print("TAVILY_API_KEY loaded:", "Yes" if TAVILY_API_KEY else "No")

# Validate required environment variables
if not XAI_API_KEY:
    raise ValueError("XAI_API_KEY environment variable is not set. Please set it in your .env file.")
if not TAVILY_API_KEY:
    raise ValueError("TAVILY_API_KEY environment variable is not set. Please set it in your .env file.") 