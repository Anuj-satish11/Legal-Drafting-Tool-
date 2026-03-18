from app.routes import main

@main.route("/status", methods=["GET"])
def status():
    return {"status": "ok", "service": "legal-drafting-tool"}