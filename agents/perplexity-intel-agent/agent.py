import anthropic
import os
import sys
from datetime import datetime
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT
from tools import get_search_tool_definition, execute_search

sys.stdout.reconfigure(encoding="utf-8")
load_dotenv()


def run_agent():
    client = anthropic.Anthropic()

    messages = [
        {
            "role": "user",
            "content": f"Run a full competitor intelligence scan for today, {datetime.now().strftime('%B %d, %Y')}. Search for the latest signals on Google AI Overviews, OpenAI SearchGPT, Microsoft Copilot, and Anthropic. Produce the full structured report."
        }
    ]

    tools = [get_search_tool_definition()]

    print("🔍 Agent starting scan...\n")

    while True:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=4000,
            system=SYSTEM_PROMPT,
            tools=tools,
            messages=messages
        )

        # If agent wants to use a tool
        if response.stop_reason == "tool_use":
            # Add assistant response to messages
            messages.append({"role": "assistant", "content": response.content})

            # Process each tool call
            tool_results = []
            for block in response.content:
                if block.type == "tool_use":
                    print(f"🔎 Searching: {block.input['query']}")
                    result = execute_search(
                        block.input["query"],
                        block.input.get("days_back", 30)
                    )
                    tool_results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": result
                    })

            messages.append({"role": "user", "content": tool_results})

        # Agent is done
        elif response.stop_reason == "end_turn":
            final_report = ""
            for block in response.content:
                if hasattr(block, "text"):
                    final_report += block.text

            # Save report
            os.makedirs("output", exist_ok=True)
            filename = f"output/report_{datetime.now().strftime('%Y%m%d_%H%M')}.md"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(final_report)

            print("\n" + "=" * 60)
            print(final_report)
            print("=" * 60)
            print(f"\n✅ Report saved to {filename}")
            break

        else:
            print(f"Unexpected stop reason: {response.stop_reason}")
            break


if __name__ == "__main__":
    run_agent()
