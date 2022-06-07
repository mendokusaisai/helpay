from flask import Flask, render_template

from api.card_api import card_api_bp
from api.member_api import member_api_bp

app = Flask(
    __name__,
    static_folder="../frontend/dist/static",
    template_folder="../frontend/dist",
)
app.register_blueprint(card_api_bp)
app.register_blueprint(member_api_bp)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def index(path: str) -> str:
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
