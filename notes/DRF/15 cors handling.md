## CORS Handling (django-cors-headers)
    CORS Kya Hota Hai?

## CORS ka full form hai:

    Cross-Origin Resource Sharing

# Ye browser ka security feature hota hai.

    Agar frontend aur backend alag origins par chalein, to browser request ko block kar deta hai.
    
# Example:

    Frontend	Backend
    http://localhost:3000	http://127.0.0.1:8000

    Yaha ports alag hain, isliye ye different origins hain.


## how to handle

Django Me CORS Handle Karne Ka Standard Package

Package:

django-cors-headers

Ye automatically proper headers add karta hai.

Installation
        pip install django-cors-headers


        INSTALLED_APPS
        INSTALLED_APPS = [
            ...
            "corsheaders",
]




# Middleware Add Karna
        IMPORTANT

        Ye middleware top me hona chahiye.

        MIDDLEWARE = [
            "corsheaders.middleware.CorsMiddleware",

            "django.middleware.common.CommonMiddleware",
        ]




Sab Origins Allow Karna (Development)
CORS_ALLOW_ALL_ORIGINS = True

Ab koi bhi frontend request bhej sakta hai.

Example

React app:

http://localhost:3000

Django:

http://127.0.0.1:8000

Request:

fetch("http://127.0.0.1:8000/api/")

Ab request allow ho jayegi.

# Production Me Ye Dangerous Hai

    Production me:

    CORS_ALLOW_ALL_ORIGINS = True

    use nahi karna chahiye.

    Kyun?

    Kyuki koi bhi website tumhari API access kar sakti hai.



## Production Safe Way

        Specific origins allow karo.

        CORS_ALLOWED_ORIGINS = [
            "http://localhost:3000",
            "https://myfrontend.com",
        ]

        Sirf ye origins access kar payenge.