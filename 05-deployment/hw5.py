import pickle


from pathlib import Path
MODEL_PATH = Path(__file__).with_name("pipeline.bin")
with MODEL_PATH.open("rb") as model_file:
    pipeline = pickle.load(model_file)



REMOTE_CALL = {
    "lead_source": "organic_search",
    "industry": "technology",
    "employment_status": "employed",
    "location": "europe",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0,
    "interaction_count": 7,
    "lead_score": 0.74,
}

from model import normalize_record
record = normalize_record(REMOTE_CALL)
prob_conversion = float(pipeline.predict_proba([record])[0, 1])

print(f"Probability of conversion: {round(prob_conversion, 3)}")