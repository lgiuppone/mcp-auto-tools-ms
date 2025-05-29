import yaml
import os

# Custom instructions for memory processing
# These aren't being used right now but Mem0 does support adding custom prompting
# for handling memory retrieval and processing.
CUSTOM_INSTRUCTIONS = """
Extract the Following User-Related Information:

- User Identity: Capture unique identifiers such as user ID or name.
- User Context: Understand the context in which the user is being queried or created (e.g., testing, onboarding, production).
- Actions: Identify what operation is being requested (fetch, create, list, random selection).
- Relationships: Note any links or associations between this user and other entities (e.g., related endpoints or services).
- Purpose: Clarify why this user information is relevant or useful for the current query or task.
- Source: Record which endpoint or external API is providing the user data.
"""

def load_tools_config(file_path="tools.yml") -> dict:
    """Loads the tools configuration from a YAML file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Tools config file '{file_path}' not found.")

    with open(file_path, "r") as f:
        return yaml.safe_load(f)
    
