from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound


def youtube_subtitle(data):
    # Extract the video ID from the YouTube URL
    video_id = data.split('v=')[-1]

    try:
        subtitle = ""
        # Try to get manually added English subtitles first
        srt = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    except NoTranscriptFound:
        try:
            # If manually added English subtitles are not found, try auto-generated subtitles
            srt = YouTubeTranscriptApi.get_transcript(video_id)
        except (TranscriptsDisabled, NoTranscriptFound):
            # If no subtitles are available, return 0
            return 0
    except TranscriptsDisabled:
        # If transcripts are disabled for the video, return 0
        return 0

    # Concatenate the subtitles into a single string
    for sub in srt:
        subtitle += sub["text"] + " "

    return subtitle

# Example usage
# video_url = "https://www.youtube.com/watch?v=example_video_id"
# print(youtube_subtitle(video_url))
