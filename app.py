from flask import *
import openai
import os
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    if request.method == "POST":
        print(request.form["subject"])
        print(request.form["background"])
        print(request.form["mood"])
        print(request.form["vibe"])
        print(request.form["camera_proximity"])
        print(request.form["camera_angle"])
        print(request.form["camera_settings"])
        print(request.form["lighting"])
        print(request.form["camera_effects"])
        print(request.form["film_types"])

        openai.api_key = os.getenv("OPENAI_API_KEY")

        
        PROMPT = request.form["subject"] + " " + request.form["background"] + " " + request.form["mood"] + " " + request.form["vibe"] + " " + request.form["theme"] + "" + request.form["camera_proximity"] + " " + request.form["camera_angle"] + " " + request.form["camera_settings"] + " " + request.form["lighting"] + " " + request.form["ambience"] + " " + request.form["camera_effects"] + " " + request.form["camera_settings"] + " " + request.form["film_types"]

        response = openai.Image.create(
            prompt=PROMPT,
            n=1,
            size="1024x1024"
        )

        print(response["data"][0]["url"])
        return render_template("home.html",image_url=response["data"][0]["url"])

    return render_template("home.html")

if __name__ == "__main__":
    app.run()