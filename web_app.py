from flask import Flask, render_template, request
import os
from utils import create_folder, move_images

app = Flask(__name__)
DEST_FOLDER = os.path.join(os.getcwd(), "data", "organized")

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        folder = request.form.get("folder")
        if folder and os.path.exists(folder):
            create_folder(DEST_FOLDER)
            moved_count = move_images(folder, DEST_FOLDER)
            message = f"{moved_count} images moved successfully!"
        else:
            message = "Invalid folder path."
    return render_template("index.html", message=message)

if __name__ == "__main__":
    app.run(debug=True)