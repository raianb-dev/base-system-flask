from flask import Response
import datetime, json


def serial(status=400, content=None, alert=None):
    data = {}
    data["message"] = "procedure performed successfully"
    data["time_request"] = str(datetime.datetime.now())
    data["status"] = status
    data["content"] = [content]
    
    if (alert):
        data["alert"] = alert
        
    return Response(
        json.dumps(data),
        status=status,
        mimetype="aplication/json"
    )