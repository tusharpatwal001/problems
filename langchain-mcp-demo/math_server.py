from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers

    Args:
        a (int): first number
        b (int): second number 

    Returns:
        int: sum of two numbers
    """
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """multiply two numbers

    Args:
        a (int): first number
        b (int): second number 

    Returns:
        int: product of two numbers
    """
    return a * b

# The transport="stdio" argunment tells the server to:

# Use standard input/output (stdin and stdout) to receive to tool function calls


if __name__ == "__main__":
    mcp.run(transport="stdio")
