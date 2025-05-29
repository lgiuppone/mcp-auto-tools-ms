import httpx
from mcp.server.fastmcp import FastMCP, Context
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
from dataclasses import dataclass
from dotenv import load_dotenv
#from mem0 import Memory
import asyncio
import json
import os
from utils import load_tools_config

#from utils import get_mem0_client

load_dotenv()

tools_config = load_tools_config()

# Default user ID for memory operations
DEFAULT_USER_ID = "user"

# Create a dataclass for our application context
@dataclass
class Mem0Context:
    """Context for the Mem0 MCP server."""

# Initialize FastMCP server with the Mem0 client as context
mcp = FastMCP(
    "mcp-mem0",
    description="MCP server for long term memory storage and retrieval with Mem0",
   # lifespan=mem0_lifespan,
    host=os.getenv("HOST", "0.0.0.0"),
    port=os.getenv("PORT", "8050")
)        

# Factory para registrar herramientas dinámicamente
def create_tool(tool_name: str, endpoint: str, description: str):
    @mcp.tool(name=tool_name, description=description)
    async def _tool(ctx: Context):
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(endpoint)
                response.raise_for_status()
                return response.text
        except Exception as e:
            return f"{tool_name} error: {str(e)}"

# Registrar herramientas del YAML
for tool_name, tool_info in tools_config.get("tools", {}).items():
    endpoint = tool_info["endpoint"]
    description = tool_info.get("description", f"{tool_name} tool")
    create_tool(tool_name, endpoint, description)
        
##@mcp.tool()
##async def fetch_users2(ctx: Context) -> str:
##    """Fetch users from the external REST API."""
##    try:
##        async with httpx.AsyncClient() as client:
##            response = await client.get("https://api-fast-docker.dev.api-users/users/1")
##            response.raise_for_status()
##            return response.text
##    except Exception as e:
##        return f"Error fetching users: {str(e)}"
##


async def main():
    transport = os.getenv("TRANSPORT", "sse")
    if transport == 'sse':
        # Run the MCP server with sse transport
        await mcp.run_sse_async()
    else:
        # Run the MCP server with stdio transport
        await mcp.run_stdio_async()

if __name__ == "__main__":
    asyncio.run(main())
