import multipart
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import uvicorn


# Create the FastAPI instance
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
def get_root_html() -> HTMLResponse:
    with open("templates/index.html") as html:
        return HTMLResponse(content=html.read())


@app.get("/basics", response_class=HTMLResponse)
def get_basics_html() -> HTMLResponse:
    with open("templates/basics.html") as html:
        return HTMLResponse(content=html.read())


# add the remaining endpoints here
@app.get("/web_serving", response_class=HTMLResponse) #can be json, html, etc.
def get_web_serving_html() -> HTMLResponse: #function will return this HTML, -> means this will do this thing
    with open("templates/web_serving.html") as html:
        return HTMLResponse(content=html.read()) 
    
@app.get("/web_development", response_class=HTMLResponse) 
def get_web_development() -> HTMLResponse:
    with open("templates/web_development.html") as html:
        return HTMLResponse(content =html.read())

@app.get("/view_notes", response_class=HTMLResponse) #reads the notes and does the 
def get_view_notes() -> HTMLResponse:
    with open("templates/notes.html") as html:
        return HTMLResponse(content =html.read())

@app.get("/notes")
async def read_notes():
    """
    Read the notes from the file and return them.
    :return:
    """
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
    except FileNotFoundError:
        content = "No notes yet."
    return {"notes": content}

#something benefiting from being asynchronous, taking a long time like opening a file
@app.post("/notes")
async def write_notes(note: str = Form(...)):
    """
    Write the notes to the file. post your messages to the notes endpoint.
    :param note:
    :return:
    """
    with open("notes.txt", "w") as file:
        file.write(note)
    return {"message": "Note saved successfully."}


# an example of a path parameter
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
