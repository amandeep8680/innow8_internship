## What is Session Authentication?
Session Authentication means:

-User logs in with username + password
-Django creates a session
-Browser stores a sessionid cookie
-Every next request automatically sends that cookie
-Server checks the session and identifies the user-

# It is mostly used for:
Web applications
Django Admin
Websites using browser login

# Not commonly used for:
Mobile apps
Public APIs

##  Working directory
projects/web/__drf__/sessionauth



# Configure DRF Authentication
settings.py     
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
    ],
}



 it create sesion automaticlly when we use login  inbuilt or 
 manualy by 
    # login(request,usr)