from fastapi import FastAPI

# Creating your fastapi application
app = FastAPI()

#Simple fastapi code
# this is  a endpoint
@app.get("/")
def home():
    return{"Message":"Hi, Aman"}

@app.get("/me")
def aboutme():
    return{
        "Name":"Amandeep",
        "Role":"SDE"
    }



