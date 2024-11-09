from flask import Flask, request, render_template, redirect, url_for, abort
import whisper
import os
import warnings
import logging

# Suppress FP16 warning
warnings.filterwarnings(
    "ignore", message="FP16 is not supported on CPU; using FP32 instead"
)

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Configure logging
logging.basicConfig(level=logging.DEBUG)


# Function to transcribe video
def transcribe_video(video_path):
    logging.debug(f"Transcribing video: {video_path}")
    model = whisper.load_model("base")
    result = model.transcribe(video_path)
    logging.debug(f"Transcription result: {result['text']}")
    return result["text"]


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            logging.debug("No file part in the request")
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            logging.debug("No selected file")
            return redirect(request.url)
        if file:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            logging.debug(f"Saving file to: {file_path}")
            file.save(file_path)
            transcription = transcribe_video(file_path)
            return render_template("result.html", transcription=transcription)
    return render_template("upload.html")


@app.errorhandler(404)
def page_not_found(e):
    logging.debug("Page not found: 404")
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)
