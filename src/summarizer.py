import os
from dotenv import load_dotenv

load_dotenv()  # reads .env and loads its values into the environment
from groq import Groq

client = Groq()  # automatically reads GROQ_API_KEY from your environment
MODEL = os.environ["GROQ_MODEL"]


def build_prompt(stories):
    lines = []
    for i, story in enumerate(stories, start=1):
        lines.append(f"{i}. {story['title']} ({story['score']} points, {story['comments']} comments) - {story['url']}")
    return (
        "Summarize today's top Hacker News stories below into a short, friendly digest.\n"
        "For each story, write ONE punchy sentence about why it matters - no fluff. "
        "Keep every link exactly as given. Format as a numbered list.\n\n"
        + "\n".join(lines)
    )


def summarize_stories(stories):
    prompt = build_prompt(stories)
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You write concise, engaging tech-news digests."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
        max_completion_tokens=600,
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    from hn_client import get_top_stories
    stories = get_top_stories()
    print(summarize_stories(stories))