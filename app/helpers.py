# File of helpers for app.py

# Dummy to test processing input data
def testHelper(input):
    diseases = ["heart attack", "flu", "cancer", "allergy"]
    pick = len(input) % len(diseases)
    return diseases[pick]