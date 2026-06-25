import cv2
import pytesseract
from pytesseract import Output

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

def extract_text_from_image(state):

    image_path = state["file_path"]

    img = cv2.imread(image_path)

    if img is None:
        state["error"] = "Image not found"
        return state

    text = pytesseract.image_to_string(img)

    data = pytesseract.image_to_data(
        img,
        output_type=Output.DICT
    )

    confidences = []

    for conf in data["conf"]:
        try:
            conf = float(conf)

            if conf > 0:
                confidences.append(conf)

        except:
            pass

    avg_conf = (
        round(sum(confidences)/len(confidences), 2)
        if confidences else 0
    )

    state["contents"]["image"].append(
    {
        "text": text,
        "ocr_confidence": avg_conf
    }
    )

    return state

if __name__ == "__main__":

    state = {
        "file_path": "sample_data/sample1.jpeg"
    }

    result = extract_text_from_image(state)

    print(result)