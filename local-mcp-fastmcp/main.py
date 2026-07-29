import random

from fastmcp import FastMCP

mcp = FastMCP(name="Maths server")


@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together"""
    return a + b


@mcp.tool
def dice_roll(n_dice: int = 1) -> list[int]:
    """Roll n_dice 6 sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]


if __name__ == "__main__":
    mcp.run()
