from world import world
import uvicorn

print("HERE MAIN")
if __name__ == "__main__":
    print("main")
    uvicorn.run("main:world.fastapi_app", host="127.0.0.1", port=5000, reload=False)
