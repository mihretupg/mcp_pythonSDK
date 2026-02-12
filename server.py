from mcp.server.fastmcp import FastMCP  # pyright: ignore[reportMissingImports]
from quotes import get_sad_quote, get_happy_quote, get_neutral_quote  # pyright: ignore[reportMissingImports]

mcp = FastMCP("AXBV-qoutes-server")  # MCP server name
@mcp.tool(
    name="Get-AXBV-quote",
    description="Return a random  quote from the AXBV quotes collection."
)
def get_axbv_happy_quote() -> str:
    return get_happy_quote()

def get_axbv_sad_quote() -> str:
    return get_sad_quote()

def get_axbv_neutral_quote() -> str:
    return get_neutral_quote()



if __name__ == "__main__":
    mcp.run()
