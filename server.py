from fastapi import fastapi

app = fastapi()

@app.get("/")
def read_root():
    return {"message": "Hello from Render!"}