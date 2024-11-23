import azure.functions as func
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    test_resp = {
        "id": "some_plan_id",
        "lastUpdated": "today",
    }
    return func.HttpResponse(
        json.dumps(test_resp),
        mimetype="application/json",
        status_code=200,
    )
