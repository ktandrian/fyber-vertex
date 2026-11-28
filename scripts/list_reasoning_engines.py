"""Get all agent runtimes in a project."""

import agentplatform
from decouple import config

PROJECT_ID = config("PROJECT_ID", default="YOUR_PROJECT_ID")
LOCATION = "us-central1" # Only available in us-central1 as per 2024-06-17.

client = agentplatform.Client(project=PROJECT_ID, location=LOCATION)
reasoning_engine_list = list(client.runtimes.list())
print(reasoning_engine_list)
