import localizeconst

from fastapi import FastAPI
from clip_classifier import ClipClassifier, ClipUrlDataTemplate


app = FastAPI()
classifier = ClipClassifier()


@app.get("/")
def root():
    """Корневая страница API"""
    return {"message":
            localizeconst.WELCOME_API_LABEL_PART1 +
            localizeconst.WELCOME_API_LABEL_PART2 +
            localizeconst.WELCOME_API_LABEL_PART3}


@app.post("/predict/")
def predict(clip_data: ClipUrlDataTemplate):
    """Запрос для предсказания классификатором."""
    result = classifier.predict_by_url_data_template(clip_data)
    dict_result = {'label': result[0],
                   'confidence': result[1]}
    return dict_result
