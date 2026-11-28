"""Delete an agent runtime in a project."""

import agentplatform
from decouple import config

PROJECT_ID = config("PROJECT_ID", default="YOUR_PROJECT_ID")
LOCATION = "us-central1"
client = agentplatform.Client(project=PROJECT_ID, location=LOCATION)

# Change the Agent Engine ID
REASONING_ENGINE_ID = "1234567890123456"
client.runtimes.delete(
    name=f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{REASONING_ENGINE_ID}"
)
