import re
from googleapiclient.discovery import build
from isodate import parse_duration

def get_playlist_id(url):
    pattern = r'list=([a-zA-Z0-9_-]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else None

def get_playlist_details(api_key, playlist_id):
    """
    Returns a list of dicts: [{title, duration_seconds, video_id}]
    and total_seconds.
    """
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_ids = []
    title_map = {}  # video_id -> title
    next_page_token = None

    # Step 1: Get all video IDs + titles from playlist
    while True:
        pl_request = youtube.playlistItems().list(
            part='contentDetails,snippet',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        pl_response = pl_request.execute()

        for item in pl_response['items']:
            vid_id = item['contentDetails']['videoId']
            title = item['snippet']['title']
            video_ids.append(vid_id)
            title_map[vid_id] = title

        next_page_token = pl_response.get('nextPageToken')
        if not next_page_token:
            break

    # Step 2: Get durations in batches
    videos = []
    total_seconds = 0

    for i in range(0, len(video_ids), 50):
        batch_ids = ','.join(video_ids[i:i+50])
        video_request = youtube.videos().list(
            part='contentDetails',
            id=batch_ids
        )
        video_response = video_request.execute()

        for item in video_response['items']:
            vid_id = item['id']
            duration_iso = item['contentDetails']['duration']
            if duration_iso == 'P0D':
                continue
            secs = parse_duration(duration_iso).total_seconds()
            total_seconds += secs
            videos.append({
                'title': title_map.get(vid_id, 'Unknown'),
                'duration_seconds': secs,
                'video_id': vid_id
            })

    return videos, total_seconds

def format_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    result = []
    if hours > 0: result.append(f"{hours}h")
    if minutes > 0: result.append(f"{minutes}m")
    if secs > 0 or (hours == 0 and minutes == 0): result.append(f"{secs}s")
    return ', '.join(result)