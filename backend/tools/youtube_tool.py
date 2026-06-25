from youtube_transcript_api import YouTubeTranscriptApi
import re


def get_youtube_transcript(state):

    youtube_urls = state.get("youtube_urls", [])

    if not youtube_urls:
        return state

    url = youtube_urls[0]

    match = re.search(r"v=([a-zA-Z0-9_-]+)", url)

    if not match:
        state["youtube_error"] = "Invalid URL"
        return state

    video_id = match.group(1)

    try:

        ytt_api = YouTubeTranscriptApi()

        try:
            transcript = ytt_api.fetch(
                video_id,
                languages=["en"]
        ).to_raw_data()

        except:
            transcript = ytt_api.fetch(
                video_id,
                languages=["hi"]
        ).to_raw_data()

        transcript_text = " ".join(
            item["text"]
            for item in transcript
        )

        state["contents"]["youtube"].append(
            {
                "video_id": video_id,
                "text": transcript_text
            }
        )

    except Exception as e:

        print("YOUTUBE ERROR:", e)
        state["youtube_error"] = str(e)

    return state