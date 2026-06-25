class Planner:

    def create_plan(self, intent: str, file_types: list) -> list:

        plan = []

        # Input processing

        if "pdf" in file_types:
            plan.append("parse_pdf")
            plan.append("detect_urls")
            plan.append("process_urls")
            plan.append("get_youtube_transcript")

        if "image" in file_types:
            plan.append("extract_image_text")
            plan.append("detect_urls")
            plan.append("process_urls")
            plan.append("get_youtube_transcript")

        if "audio" in file_types:
            plan.append("transcribe_audio")

        # Task processing

        # if "youtube" in intent:
        #     plan.append("get_youtube_transcript")

        if intent == "summarization":
            plan.append("summarize")

        elif intent == "sentiment_analysis":
            plan.append("analyze_sentiment")

        elif intent == "code_explanation":
            plan.append("explain_code")

        elif intent == "comparison":
            plan.append("compare_content")

        elif intent == "qa":
            plan.append("answer_question")

        return plan
    
if __name__ == "__main__":

    planner = Planner()

    print(
        planner.create_plan(
            intent="summarization",
            file_types=["pdf"]
        )
    )