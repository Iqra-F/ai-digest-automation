from dotenv import load_dotenv

load_dotenv()

from hn_client import get_top_stories
from summarizer import summarize_stories
from publisher import publish_to_discord


def run(story_limit=5):
    print(f"Fetching top {story_limit} HN stories...")
    stories = get_top_stories(story_limit)

    print("Summarizing with AI...")
    digest = summarize_stories(stories)

    header = "Hacker News Daily Digest\n\n"
    full_message = header + digest

    print("Publishing...")
    publish_to_discord(full_message)
    print("Done.")


if __name__ == "__main__":
    run()