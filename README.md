# WINA Race Scraper (Render Ready)

## What it does:
Scrapes today's UK race meetings from Racing Post and serves them as an API.

## How to deploy on Render:
1. Upload this folder to GitHub
2. Go to https://render.com
3. Click "New Web Service"
4. Connect your repo and set:
   - Environment: Python
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn main:app`

## API Endpoint:
- `/recent-meetings` — Returns today’s race meetings in JSON

Use this endpoint in your Lovable app to power the race dropdown.