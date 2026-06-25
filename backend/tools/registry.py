from backend.tools.pdf_tool import parse_pdf
from backend.tools.summary_tool import summarize
from backend.tools.image_tool import extract_text_from_image
from backend.tools.audio_tool import transcribe_audio
# from backend.tools.comparison_tool import compare_content
from backend.tools.detect_urls import detect_urls   
from backend.tools.process_urls import process_urls
from backend.tools.youtube_tool import get_youtube_transcript

TOOLS = {
    "parse_pdf": parse_pdf,
    "summarize": summarize,
    "extract_image_text": extract_text_from_image,
    "transcribe_audio": transcribe_audio,
    "detect_urls": detect_urls,
    "process_urls": process_urls,   
    "get_youtube_transcript": get_youtube_transcript
}