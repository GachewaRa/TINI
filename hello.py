from fastapi import FastAPI, Body, Header
app = FastAPI()

#using path variable
# @app.get("/hi/{who}")
# def greet(who):
#     return f"Hello {who}."

#using query params
# @app.get("/hi")
# def greet(who):
#     return f"Hello {who}."

#using the body
@app.post("/hi")
def greet(who:str = Body(embed=True)):
    return f"Hello {who}."

#using th header
# @app.post("/hi")
# def greet(who:str = Header()):
#     return f"Hello {who}."