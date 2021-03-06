# File of helpers for app.py

# Dummy to test processing input data
def testHelper(input):
    diseases = ["heart attack", "flu", "cancer", "allergy"]
    pick = len(input) % len(diseases)

    if "chest_pain" in input:
        return "acute coronary syndrome"
    elif "fever" in input:
        return "flu"
    return diseases[pick]
