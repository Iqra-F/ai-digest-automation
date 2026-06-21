import requests

HN_BASE_URL = "https://hacker-news.firebaseio.com/v0"


def get_top_story_ids(limit=5):
    response = requests.get(f"{HN_BASE_URL}/topstories.json", timeout=10)
    response.raise_for_status()
    return response.json()[:limit]


def get_story(story_id):
    response = requests.get(f"{HN_BASE_URL}/item/{story_id}.json", timeout=10)
    response.raise_for_status()
    return response.json()


def get_top_stories(limit=5):
    story_ids = get_top_story_ids(limit)
    stories = []
    for story_id in story_ids:
        story = get_story(story_id)
        stories.append({
            "title": story.get("title", "Untitled"),
            "url": story.get("url", f"https://news.ycombinator.com/item?id={story_id}"),
            "score": story.get("score", 0),
            "comments": story.get("descendants", 0),
        })
    return stories

if __name__ == "__main__":
    for story in get_top_stories():
        print(f"- {story['title']} ({story['score']} pts) -> {story['url']}")