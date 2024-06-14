import pyrebase

firebaseconfig = {
                "apiKey": "AIzaSyBbEV8hUZ4sLELpHmp9HPWsrKS9qxs6MCQ",
                "authDomain": "login1-f85ff.firebaseapp.com",
                "databaseURL": "https://login1-f85ff.firebaseio.com",
                "projectId": "login1-f85ff",
                "storageBucket": "login1-f85ff.appspot.com",
                "messagingSenderId": "781518658658",
                "appId": "1:781518658658:web:88c6981e58fcbda5f5053b",
                "measurementId": "G-RK7XL5L8BR"
}
firebase=pyrebase.initialize_app(firebaseconfig)
auth=firebase.auth()

def login():
    print("log in...")
    email=input("enter email: ")
    password=input("enter password: ")
    try:
        auth.sign_in_with_email_and_password(email,password)
        print("logged in successfully")
    except:
        print("invalid credentials")
        return
def signup():
    print("sign up...")
    email = input("enter email: ")
    password = input("enter password: ")
    try:
        user = auth.create_user_with_email_and_password(email, password)
    except:
        print("user already exists")
        return
    
ans=input("are you a new user?[y/n]")

if ans == 'n':
    login()
elif ans == 'y':
    signup()