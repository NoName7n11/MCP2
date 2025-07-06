from mcp.server.fastmcp import FastMCP

#Create a MCP server for calculator
mcp = FastMCP(
    name = "Calulator MCP Server",
    port = 3000,
    version = "1.0.0"
)

# Define tools for basic arithmetic operations
@mcp.tool()
def add(a: float, b: float) -> float:
    """Adds two numbers."""
    return a + b
@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtracts two numbers."""
    return a - b
@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers."""
    return a * b
@mcp.tool()
def divide(a: float, b: float) -> float:   
    """Divides two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
@mcp.tool()
def power(base: float, exponent: float) -> float:
    """Raises a number to the power of another."""
    return base ** exponent
@mcp.tool()
def square_root(number: float) -> float:
    """Calculates the square root of a number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return number ** 0.5
@mcp.tool()
def factorial(n: int) -> int:
    """Calculates the factorial of a number."""
    if n < 0:
        raise ValueError("Cannot calculate factorial of negative number")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
@mcp.tool()
def modulus(a: float, b: float) -> float:
    """Calculates the modulus of two numbers."""
    if b == 0:
        raise ValueError("Cannot calculate modulus by zero")
    return a % b
@mcp.tool()
def average(numbers: list[float]) -> float:
    """Calculates the average of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    return sum(numbers) / len(numbers)
@mcp.tool()
def percentage(part: float, whole: float) -> float:
    """Calculates the percentage of a part of a whole."""
    if whole == 0:
        raise ValueError("Cannot calculate percentage of zero")
    return (part / whole) * 100

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()