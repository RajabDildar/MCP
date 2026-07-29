import json
import random

from fastmcp import FastMCP

mcp = FastMCP(name="New demo server")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b


@mcp.tool
def dice_roll(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6 sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


@mcp.resource("info://server")
def server_info() -> str:
    """Get info about this server"""
    info = {
        "name": "Simple calculator server",
        "author": "Rajab Ali",
        "description": "A basic mcp server with maths tools",
        "tools": ["add", "dice_roll"],
        "version": "",
    }
    return json.dumps(info, indent=2)


if __name__ == "__main__":
    # mcp.run() # for local stdio, use this
    mcp.run(transport="http", host="0.0.0.0", port=8000)
