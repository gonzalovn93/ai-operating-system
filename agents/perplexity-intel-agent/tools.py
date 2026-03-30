from tavily import TavilyClient
import os


def get_search_tool_definition():
    return {
        "name": "web_search",
        "description": "Search the web for recent news, product updates, job postings, and announcements about AI search competitors. Use targeted queries. Returns top results with titles, URLs, and snippets.",
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "The search query. Be specific. Include company name and topic."
                },
                "days_back": {
                    "type": "integer",
                    "description": "How many days back to search. Default 30.",
                    "default": 30
                }
            },
            "required": ["query"]
        }
    }


def execute_search(query: str, days_back: int = 30) -> str:
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    results = client.search(
        query=query,
        search_depth="advanced",
        max_results=5,
        days=days_back
    )

    formatted = []
    for r in results.get("results", []):
        formatted.append(f"**{r['title']}**\nURL: {r['url']}\n{r['content']}\n")

    return "\n---\n".join(formatted) if formatted else "No results found."
