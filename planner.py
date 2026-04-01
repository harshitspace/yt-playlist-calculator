import google.generativeai as genai
import json
from utils import format_time

def generate_study_plan(videos, total_seconds, speed, daily_weekday_mins, daily_weekend_mins, deadline_days, gemini_key, note):
    """
    Takes playlist metadata + user constraints.
    Returns AI-generated day-by-day study plan as structured text.
    """
    genai.configure(api_key=gemini_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    # Build video list string for the prompt
    adjusted_total = total_seconds / speed
    video_list = "\n".join([
        f"Video {i+1}: \"{v['title']}\" — {format_time(v['duration_seconds'] / speed)}"
        for i, v in enumerate(videos)
    ])

    prompt = f"""You are a study schedule planner. A student wants to complete a YouTube playlist.

PLAYLIST DATA (at {speed}x speed):
- Total videos: {len(videos)}
- Total duration at {speed}x: {format_time(adjusted_total)}
- Videos:
{video_list}

STUDENT CONSTRAINTS:
- Available time on weekdays: {daily_weekday_mins} minutes/day
- Available time on weekends: {daily_weekend_mins} minutes/day
- Deadline: {deadline_days} days from today
- Playback speed: {speed}x
- Additional note: {note if note else 'None'}

YOUR TASK:
Generate a realistic day-by-day schedule. Respect daily time limits strictly.
Add a rest day every 6 days. End with deadline analysis and one tip.

RESPOND STRICTLY IN THIS FORMAT — no extra prose before the tables:

## 📊 Playlist Overview

| Detail | Value |
|--------|-------|
| Total Videos | {len(videos)} |
| Total Duration ({speed}x) | {format_time(adjusted_total)} |
| Weekday Availability | {daily_weekday_mins} mins/day |
| Weekend Availability | {daily_weekend_mins} mins/day |
| Deadline | {deadline_days} days |

## 📅 Day-by-Day Schedule

| Day | Type | Videos | Duration |
|-----|------|--------|----------|
[Fill one row per day. For rest days, put "🛌 Rest Day" in Videos column and "-" in Duration.]

## ⚠️ Deadline Analysis

[2-3 sentences: Can they finish? If not, how many videos completed and how many remain?]

## 💡 Tip

[One specific, actionable tip based on the playlist length and user's pace.]

## 🎯 Motivation

[One punchy motivational line. Max 15 words.]
"""

    response = model.generate_content(prompt)
    return response.text