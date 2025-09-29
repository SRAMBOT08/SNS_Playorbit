from fastapi import FastAPI

app = FastAPI(title="SNS_Playorbit - Backend")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"msg": "SNS_Playorbit backend up. Visit /docs for API docs."}

