from fastapi import APIRouter, Request
router = APIRouter()
@router.post("/webhook/github")
async def github_webhook(request: Request):
    payload = await request.json()

    action = payload.get("action")
    pr = payload.get("pull_request", {})

    title = pr.get("title")
    url = pr.get("html_url")
    author = pr.get("user", {}).get("login")

    print(f"PR Action: {action}")
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"URL: {url}")

    return {"status": "processed"}

