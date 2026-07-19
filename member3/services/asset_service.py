"""
Asset Service

Reads processed entities and prepares
Asset 360 data.
"""

import json
import os


ENTITY_FILE = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../member1/output/entities.json"
    )
)


def get_assets():

    if not os.path.exists(ENTITY_FILE):

        return []

    with open(ENTITY_FILE, "r") as f:

        entities = json.load(f)

    assets = []

    current = {}

    for item in entities:

        entity = item["Entity"]
        entity_type = item["Type"]

        if entity_type == "Equipment":

            if current:

                assets.append(current)

            current = {
                "Equipment": entity
            }

        else:

            current[entity_type] = entity

    if current:

        assets.append(current)

    return assets