import uvicorn  


if __name__ == "__main__":
    uvicorn.run("api:app", 
                host="127.0.0.1",
                port=3300,
                reload=True)
                