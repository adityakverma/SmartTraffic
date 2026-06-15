def generate_recommendation(risk):

    if risk == "High":
        return {
            "police_units": 5,
            "barricades": 12,
            "message": "Deploy maximum traffic control resources."
        }

    elif risk == "Medium":
        return {
            "police_units": 3,
            "barricades": 6,
            "message": "Monitor traffic and prepare diversions."
        }

    else:
        return {
            "police_units": 1,
            "barricades": 2,
            "message": "Normal traffic conditions."
        }


if __name__ == "__main__":

    risk = "High"

    recommendation = generate_recommendation(risk)

    print(recommendation)