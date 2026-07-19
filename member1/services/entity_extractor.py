from gliner import GLiNER

model = GLiNER.from_pretrained("urchade/gliner_medium-v2.1")


def extract_entities(text):

    labels = [
        "Equipment",
        "Equipment Tag",
        "Component",
        "Person",
        "Inspection Date",
        "Measurement",
        "Temperature",
        "Failure",
        "Maintenance Action",
        "Plant",
        "Location"
    ]

    predictions = model.predict_entities(
        text,
        labels,
        threshold=0.4
    )

    results = []

    for item in predictions:
        results.append({
            "Entity": item["text"],
            "Type": item["label"],
            "Confidence": round(item["score"], 3)
        })

    return results