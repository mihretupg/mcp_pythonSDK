from mcp.server.fastmcp import FastMCP  # pyright: ignore[reportMissingImports]
from quotes import get_sad_quote, get_happy_quote

mcp = FastMCP("AXBV-qoutes-server")  # MCP server name
@mcp.tool(
    name="Get-AXBV-happy-quote",
    description="Return a random happy quote from the AXBV quotes collection."
)
def get_axbv_happy_quote() -> str:
    return get_happy_quote()

if __name__ == "__main__":
    mcp.run()
