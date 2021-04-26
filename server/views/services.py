from app import app
from flask import jsonify
from models import Services

@app.route("/api/services")
def listServices():
    serviceList = [s.to_public_json() for s in Services.objects()]
    return jsonify(serviceList)

@app.route("/api/services/<string:servicename>")
def getService(servicename: str) -> str:
    service = Services.objects(name=servicename).first()
    print(service)
    if service:
        return service.to_public_json()
    else:
        return jsonify({"error": "Service not found"}), 404
