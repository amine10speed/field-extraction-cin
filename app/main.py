from fastapi import FastAPI, File, UploadFile
import shutil
from app.field_extraction import extract_fields
import os

app = FastAPI()

@app.post("/extract-fields/")
async def extract_fields_endpoint(file: UploadFile = File(...), debug: bool = False):
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        fields = extract_fields(file_location, debug=debug)
        os.remove(file_location)  # Clean up the temporary file

        return {"message": "Fields extracted successfully", "fields": list(fields.keys())}
    except Exception as e:
        os.remove(file_location)
        return {"message": "Error extracting fields", "error": str(e)}
