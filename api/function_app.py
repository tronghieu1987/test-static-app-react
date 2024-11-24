import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)


@app.route(route="getPlan")
def getPlan(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        logging.info("Responding with personalized msg")
        return func.HttpResponse(
            json.dumps(
                {
                    "result": f"Hello, {name}. This HTTP triggered function executed successfully."
                }
            ),
            mimetype="application/json",
            status_code=200,
        )

    logging.info("Responding with no personalized msg")
    return func.HttpResponse(
        json.dumps(
            {
                "result": "Executed successfully. Pass a name in the query string or in the request body for a personalized response."
            }
        ),
        mimetype="application/json",
        status_code=200,
    )
