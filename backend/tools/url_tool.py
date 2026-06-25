import re

def detect_urls(state):

    text = state.get("text", "")

    urls = re.findall(
        r'https?://[^\s]+',
        text
    )

    state["urls"] = urls

    return state

if __name__ == "__main__":

    state = {
        "text": """
        Check this video:
        https://www.youtube.com/watch?v=dQw4w9WgXcQ
        """
    }

    print(detect_urls(state))