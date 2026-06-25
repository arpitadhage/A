from collections import Counter
import re


def clean_text(text: str):

    # remove bullet points and weird chars
    text = text.replace("\uf0b7", "")
    text = text.replace("\n", " ")

    return text


def summarize(state: dict):

    text = state.get("text", "")

    if not text:
        state["summary"] = "No text found"
        return state

    # CLEAN
    text = clean_text(text)

    # SPLIT SENTENCES PROPERLY
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if len(s.strip()) > 20]

    # WORD FREQUENCY
    words = re.findall(r'\w+', text.lower())
    freq = Counter(words)

    # SCORE SENTENCES
    scores = {}

    for sent in sentences:
        score = 0
        for word in re.findall(r'\w+', sent.lower()):
            score += freq[word]
        scores[sent] = score

    ranked = sorted(scores, key=scores.get, reverse=True)

    top = ranked[:5]

    # FIXED OUTPUT FORMAT
    state["summary"] = {
        "1_line": top[0] if top else "",
        "3_bullets": top[:3],
        "5_sentence": " ".join(top[:5])
    }

    return state