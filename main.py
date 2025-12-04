from fastapi import FastAPI, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.mount("/", StaticFiles(directory="static", html=True), name="static")

PROMPT_FRUIT_NET = """
Add a tight, transparent fruit foam protective mesh net that completely wraps the entire body from head to toe, including the face. 
The net must fully cover head, face, torso, arms, and legs forming a continuous layer with realistic texture, visible holes, natural shadows and highlights. 
The mesh tightly follows every body contour. No skin is exposed. 
Keep the original person, facial features, expression, pose, clothing, hair, and background 100% unchanged — only add the net layer on top.
Ultra detailed, photorealistic, 8k.
""".strip()

@app.post("/api/generate")
async def wrap_with_net(image: UploadFile = File(...)):
    try:
        contents = await image.read()

        response = client.images.edit(
            model="dall-e-3",
            image=contents,
            prompt=PROMPT_FRUIT_NET,
            n=1,
            size="1024x1024",
            response_format="b64_json"
        )

        return JSONResponse({
            "success": True,
            "image_url": f"data:image/png;base64,{response.data[0].b64_json}"
        })

    except Exception as e:
        error_msg = "OpenAI quota habis! Cek billing di platform.openai.com" if "billing" in str(e).lower() else str(e)
        return JSONResponse({"success": False, "message": error_msg}, status_code=500)
        
if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port)