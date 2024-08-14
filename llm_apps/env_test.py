from dotenv import load_dotenv
import os

env_path = '/Users/christophergusty/code/packt/.env'
load_dotenv(dotenv_path=env_path)

# Print the loaded environment variable
print(f"SERPAPI_API_KEY: {os.getenv('SERPAPI_API_KEY')}")
