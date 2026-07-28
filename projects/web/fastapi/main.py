from fastapi import FastAPI

# Creating your fastapi application instance 
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



@app.get("/users/{user_id}")
def users(user_id: str):
    return {
        "Hi":user_id,
    
    }



@app.get("/userss/{user_id}")
def get_user(user_id: int, active: bool):
    return {
        "user_id": user_id,
        "active": active
    }


@app.get("/product/{product_id}")
def product(product_id: int, price: int):
    return {
        "product_id": product_id,
        "price": price
    } 




#  post request

@app.post("/createuser")
def create_user():
    return{
        "message":"User Created"
    }