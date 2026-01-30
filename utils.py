import re
from googleapiclient.discovery import build
from isodate import parse_duration

def get_playlist_id(url):
    pattern = r'list=([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    if match:
        return match.group(1)
    return None

def get_playlist_duration(api_key, playlist_id):
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_ids = []
    total_seconds = 0
    next_page_token = None

    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )

        pl_response = pl_request.execute()

        for item in pl_response['items']:
            video_ids.append(item['contentDetails']['videoId'])
        
        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break

    for i in range(0, len(video_ids), 50):
        batch_ids = ','.join(video_ids[i:i+50])

        video_request = youtube.videos().list(
            part='contentDetails',
            id=batch_ids
        )

        video_response = video_request.execute()

        for item in video_response['items']:
            duration_iso = item['contentDetails']['duration']
            if duration_iso == 'P0D':
                continue
            seconds = parse_duration(duration_iso).total_seconds()
            total_seconds += seconds
        
    return total_seconds, len(video_ids)

def format_time(seconds):
    hours = (seconds // 3600)
    minutes = ((seconds % 3600) // 60)
    secs = (seconds % 60)

    result = []
    if hours > 0:
        result.append(f"{hours} h")
    if minutes > 0:
        result.append(f"{minutes} m")
    if secs > 0 or (hours == 0 and minutes == 0):
        result.append(f"{secs} s")
    
    return ', '.join(result)