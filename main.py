import logging
import json

from flask import request, Response
from database.models import CoffeeMachine, CoffeePod
from baseapp import app

logger = logging.getLogger(__name__)


def get_filters(query_params, cls):
    return {x: y.upper() for x, y in query_params.items() if hasattr(cls, x)}


@app.route('/coffee-machines')
def get_coffee_machines():

    try:
        filters = get_filters(request.args, CoffeeMachine)
        if filters.get("water_line"):
            filters['water_line'] = True if filters['water_line'].upper() == "TRUE" else False

        coffee_machines = CoffeeMachine.objects(**filters).to_json()
        return Response(coffee_machines, mimetype="application/json", status=200)
    except Exception as e:
        logger.exception(f"Error {e} while getting machines")

        return Response(
            json.dumps({"error": "Something bad happend please try later"}),
            mimetype="application/json",
            status=500,
        )


@app.route('/coffee-pods')
def get_coffee_pods():
    try:
        filters = get_filters(request.args, CoffeePod)
        coffee_pods = CoffeePod.objects(**filters).to_json()
        return Response(coffee_pods, mimetype="application/json", status=200)
    except Exception as e:
        logger.exception(f"Error {e} while getting pods")

        return Response(
            json.dumps({"error": "Something bad happend please try later"}),
            mimetype="application/json",
            status=500,
        )
