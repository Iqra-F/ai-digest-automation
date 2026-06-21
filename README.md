## Prerequisites

- Python 3.12 or later
- A free [Groq](https://console.groq.com) account and API key
- A Discord server with a webhook URL ([how to create one](https://support.discord.com/hc/en-us/articles/228383668-Intro-to-Webhooks))

## Local Setup

```bash
# Clone the repo
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME

# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# then fill in your real keys in .env
```

## Environment Variables

| Variable | Description |
|----------|--------------|
| `GROQ_API_KEY` | Your Groq API key from console.groq.com |
| `GROQ_MODEL` | The model to use (e.g. `llama-3.1-8b-instant`) |
| `DISCORD_WEBHOOK_URL` | Webhook URL for the Discord channel to post into |

## Running Locally

```bash
python src/main.py
```

This fetches the top 5 HN stories, summarizes them, and posts the digest to your Discord channel — printing progress to the console along the way.

## Automation (GitHub Actions)

The bot runs automatically every day via `.github/workflows/daily_digest.yml`.

**Setup:**
1. Go to your repo's **Settings → Secrets and variables → Actions**
2. Add repository secrets matching the environment variables above: `GROQ_API_KEY`, `GROQ_MODEL`, `DISCORD_WEBHOOK_URL`
3. Push your code — the workflow activates automatically
4. Trigger it manually anytime from the **Actions** tab using the "Run workflow" button

**Default schedule:** 08:00 UTC daily. To change it, edit the `cron` expression in `daily_digest.yml`.

## Customization

- **Number of stories:** change `story_limit` in `src/main.py`'s `run()` call
- **Tone/style of the digest:** edit the prompt in `build_prompt()` inside `src/summarizer.py`
- **Publishing target:** swap Discord for Telegram by adapting `publisher.py` (Telegram Bot API uses a similar webhook-style POST request)

## Engineering Notes

This project originally targeted NVIDIA NIM for inference, but hit a real, documented regional limitation: NVIDIA's phone-verification signup flow doesn't yet support Pakistani phone numbers, blocking API key generation. Rather than wait on an unresolved platform bug, the project pragmatically switched to Groq — which offers an equally capable free tier with no phone verification required. Both providers expose an OpenAI-compatible API shape, which kept the swap to a two-line change.

## License

MIT

## Author

Built by Iqra Fatima — [Portfolio](https://iqra-portfolio.pages.dev/) · [GitHub](https://github.com/Iqra-F) · [LinkedIn](https://www.linkedin.com/in/iqra-fatima-290903286/)
