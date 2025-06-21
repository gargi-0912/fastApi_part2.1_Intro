from fastapi import FastAPI

app=FastAPI()
# We can replace app with any other name also
@app.get("/",description="This is our first route.",deprecated=True)
async def base_get_route():
    return {"message":"Hello world"} 

@app.post("/")
async def post():
    return {"message":"hello from the post route"}

@app.put("/")
async def put():
    return {"message":"hello from the put route"}