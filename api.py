from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, UploadFile, File
import tempfile
import shutil

from utils.document_loader import load_document
from pipeline.esg_pipeline import run_esg_analysis

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):

    try:

        suffix = "." + file.filename.split(".")[-1]

        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:

            shutil.copyfileobj(file.file, tmp)

            temp_path = tmp.name

        text = load_document(temp_path)

        report = run_esg_analysis(text)

        return report

    except Exception as e:

        return {"error": str(e)}