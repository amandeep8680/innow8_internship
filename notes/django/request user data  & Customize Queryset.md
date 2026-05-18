pracice folder - projects/web/__drf__/customizeapi

# API is not responsive it depends on - 
who are asking
who are granted
what is asking

# this is called dynamic queryset



# 🔹 🔑 Request Object Deep Understanding

request = API ka brain

request.user          # logged-in user
request.data          # POST/PUT body
request.query_params  # URL params (?course=python)
request.method        # GET, POST etc.



#  get_queryset() – Most Important Method

Ye decide karta hai:
👉 Database se exact kaunsa data aayega

def get_queryset(self):
    return Model.objects.all()

# But real power:

def get_queryset(self):
    user = self.request.user
    return Model.objects.filter(user=user)

👉 Per-user data isolation ✔️
















