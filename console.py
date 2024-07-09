import requests
def welcome_page():
    print("-----------welcome to messager---------")
    print("-----------1 for registaration---------")
    print("-----------2 for login-----------------")
    print("-----------3 for close------------------")

    number=input("Enter your choice: ")
    return number
def register():
    print("--------welcome to registration page..........")
    firstname=input("Enter your first name: ")
    lastname=input("Enter your lastname: ")
    username=input("Enter your username: ")
    password=input("Enter your password: ")
    email=input("Enter your email: ")
    print("----------------------------------------------")

    user_data={
        "username":username,
        "firstname":firstname,
        "lastname":lastname,
        "password":password,
        "email":email
    }
    api_url="http://localhost:8000/register"

    response=requests.post(url=api_url,json=user_data)
    if response.status_code==200:
        print("Succesful Registrations")
        return response.json().get("user_id")
    else:
        print(response.json().get("detail"))
        return None

def login():
    print("-------------------------------------------")
    print("-----------welcome again--------------------")
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    user_data={
        "username":username,
        "password":password
    }
    api_url="http://localhost:8000/login"

    response=requests.post(url=api_url,json=user_data)
    if response.status_code==200:
        print("Welcome come back: ",response.json().get("username"))
        return response.json().get("username"),response.json().get("user_id"),True
    else:
        print(response.json().get("detail"))
        return None,None,False
def loggedUser():
    print("----------1 for Profile View------------")
    print("----------2 for Create Post--------------")
    print("----------3 for search Users-------------")
    print("----------4 for Delete Account----------")
    print("----------else  sign out --------------- ")
    logged=input("Enter your Action: ")
    return logged

def profile_window():
    print("-----------Profile setting-------------")
    print("-----------1 for view profile-----------")
    print("-----------2 for update profile----------")
    print("-----------else to close the setting---------")
    setting=input("Enter your choice: ")
    return setting
def view_profile(user_id):
    api_url = f"http://localhost:8000/getprofile/{user_id}"
    response=requests.get(api_url)
    data=[]
    if response.status_code==200:
        data.append(("firstname",response.json().get("firstname")))
        data.append(("lastname", response.json().get("lastname")))
        data.append(("username", response.json().get("username")))
        data.append(("email", response.json().get("email")))
        data.append(("password", "##################"))

    print("-----------your profile----------------------------")
    for info,profile in data:
        print("{}: {}".format(info,profile))
    return None
def update_profile(user_id):
    print("-------------update your profile------------------")
    print("-------------new value or enter-----------")
    firstname=input("update firstname: ")
    lastname=input("update lastname: ")
    username=input("update username: ")
    email=input("update email: ")
    password=input("update password: ")
    print("---------------updating----------------------")

    if firstname:
        api_url = f"http://localhost:8000/updatefirst/{user_id}"
        user_data={"firstname":firstname}
        response=requests.put(api_url,json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    if lastname:
        api_url = f"http://localhost:8000/updatelast/{user_id}"
        user_data = {"lastname": lastname}
        response = requests.put(api_url, json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    if email:
        api_url = f"http://localhost:8000/updateemail/{user_id}"
        user_data = {"email": email}
        response = requests.put(api_url, json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    if password:
        api_url = f"http://localhost:8000/updatepass/{user_id}"
        user_data = {"password": password}
        response = requests.put(api_url, json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    if username:
        api_url = f"http://localhost:8000/updateuser/{user_id}"
        user_data = {"username": username}
        response = requests.put(api_url, json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    print("-----------------Done--------------------------")

def post_window():
    print("---------------Post Here-----------------------")
    print("---------------1 for creating post--------------")
    print("---------------2 for updating post--------------")
    print("---------------3 for deleting post--------------")
    print("---------------4 for viewing post---------------")
    print("---------------else close the post---------------")
    post=input("Enter your choice: ")
    return post
def create_post(user_id):
    print("-------------------post area--------------------------")
    content=input("Enter your post here: ")

    if content:
        user_data={
            "content":content
        }
        api_url=f"http://localhost:8000/createpost/{user_id}"
        response=requests.post(url=api_url,json=user_data)
        if response.status_code==200:
            print(response.json().get("message"))
    else:
        print("-------------no post is created--------------------")
def update_post():
    print("-----------------update area---------------------------")
    post_id=input("Enter post id for updating: ")
    content=input("Enter updated post: ")

    if post_id and content:
        user_data={
            "content":content
        }
        api=f"http://localhost:8000/updatepost/{post_id}"
        response=requests.put(url=api,json=user_data)

        if response.status_code==200:
            print(response.json().get("message"))
        else:
            print(response.json().get("detail"))
    else:
        print("----------------Nothing is updated--------------------")
def delete_post():
    print("--------------------delete area---------------------------")
    post_id=input("Enter post id to delete: ")

    if post_id:
        api=f"http://localhost:8000/deletepost/{post_id}"
        response=requests.delete(api)
        if response.status_code==200:
            print(response.json().get("message"))
        else:
            print(response.json().get("detail"))
    else:
        print("----------------no post is deleted---------------------")
def view_post(user_id):
    print("--------------------------viewing area------------------------")
    api=f"http://localhost:8000/viewpost/{user_id}"
    response=requests.get(url=api)
    if response.status_code==200:
        for post in response.json():
            print("----------------------------------------")
            print("post id: ",post.get("post_id"))
            print("content: ",post.get("content"))
            print("created: ",post.get("created"))
            print("likes: ",post.get("likes"))
            print("dislike: ",post.get("dislike"))
            print("---------------END----------------------")
    else:
        print(response.json().get("detail"))
def search_window():
    print("---------------------Connect with Friends---------------------")
    username=input("search user by username: ")
    if username:
        api = f"http://localhost:8000/searchuser/{username}"
        response=requests.get(url=api)
        if response.status_code==200:
            return bool(response.json().get("message")),response.json().get("user_id"),username
    return False,None,None
def connect_window(username):
    print("-------------------Say hi to {}".format(username),"------------------------")
    print("-----------------1 for making your friend---------------")
    print("-----------------2 for viewing the posts----------------")
    print("-----------------3 for sending messages-----------------")
    print("-----------------4 for sending gift--------------------")
    print("-----------------else close the window------------------")
    ans=input("Enter your choice: ")
    return ans
def friend_post_window(user_id):
    print("----------------Read and Comment on Your Friends Post------------------------")
    view_post(user_id)
    comment=input("[1]for Comment,[2]for like,[3]for dislike,[else]: ")
    return comment
def verify_id(post_id):
    api=f"http://localhost:8000/verfiy/{post_id}"
    response=requests.get(url=api)
    if response.status_code==200:
        return True
    return False
def create_comment(user_id):
    print("-----------comment one post------------------------")
    post_id=input("Enter post id for comment: ")
    api = f"http://localhost:8000/createcomment/{post_id}"

    if post_id and verify_id(post_id):
        comment=input("Enter your comment here: ")
        data={
            "user_id":user_id,
            "comments":comment
        }
        response=requests.post(url=api,json=data)
        if response.status_code==200:
            print(response.json().get("message"))
    else:
        print("--------no comment yet...............")
def like_post():
    post_id=input("Enter post id to like: ")
    if post_id and verify_id(post_id):
        data={
            "user_id":user_id
        }
        api=f"http://localhost:8000/like/{post_id}"
        response=requests.put(url=api)
        if response.status_code==200:
            print(response.json().get("message"))
        else:
            print(response.json().get("detail"))
    else:
        print("--------------try again----------------")
def dislike_post():
    post_id=input("Enter post id to dislike: ")
    if post_id and verify_id(post_id):
        data={
            "user_id":user_id
        }
        api=f"http://localhost:8000/dislike/{post_id}"
        response=requests.put(url=api)
        if response.status_code==200:
            print(response.json().get("message"))
        else:
            print(response.json().get("detail"))
    else:
        print("--------------try again----------------")
def get_username(user_id):
    api = f"http://localhost:8000/username/{user_id}"
    response=requests.get(url=api)
    if response.status_code==200:
        return response.json().get("message")
    else:
        print(response.json().get("detail"))

def load_message(sender_id,recipent_id):
    api="http://localhost:8000/messages_data"
    data={
        "sender_id":sender_id,
        "recipent_id":recipent_id
    }
    response=requests.get(url=api,json=data)
    if response.status_code==200:
        for message in response.json():
            sender_name=get_username(message.sender_id)
            recipent_name=get_username(message.recipent_id)
            print("sender: ",sender_name)
            print("recipent: ",recipent_name)
            print("message: ",message.content)
            print("date: ",message.sent_date)
    else:
        print("-------------no message yet-----------------")
def message_window(sender,recipent):
    print("-------------------message window---------------------")
    load_message(sender,recipent)
    message=input("[1]for sending message [else]: ")
    return message
def send_message(sender_id,recipent_id):
    message=input("Write your message here: ")
    if message:
        api="http://localhost:8000/messages"
        data={
            "sender_id":sender_id,
            "recipent_id":recipent_id,
            "content":message
        }
        response=requests.post(url=api,json=data)
        if response.status_code==200:
            print(response.json().get("message"))
    else:
        print("-------------message not sent------------------------")











while True:
    choice=welcome_page()
    if choice=="1":
        register()
    elif choice=="2":
        username,user_id,correct=login()
        while True==True and correct:
            logged=loggedUser()
            if logged=="1":
                while True and True:
                    setting = profile_window()
                    if setting=="1":
                        view_profile(user_id)
                    elif setting=="2":
                        update_profile(user_id)
                    else:
                        break
            elif logged=="2":
                while True  and True:
                    post=post_window()
                    if post=="1":
                        create_post(user_id=user_id)
                    elif post=="2":
                        update_post()
                    elif post=="3":
                        delete_post()
                    elif post=="4":
                        view_post(user_id)
                    else:
                        break
            elif logged=="3":
                while True and True:
                    message,user,username=search_window()
                    if message:
                        while True and True:
                            ans=connect_window(username)
                            if ans=="1":
                                pass
                            elif ans=="2":
                                while True and True:
                                    comment=friend_post_window(user_id=user)
                                    if comment=="1":
                                        create_comment(user_id)
                                    elif comment=="2":
                                        like_post()
                                    elif comment=="3":
                                        dislike_post()
                                    else:break
                            elif ans=="3":
                                while True and True:
                                    message=message_window(user_id,user)
                                    if message=="1":
                                        send_message(user_id,user)
                                    else:
                                        break

                            elif ans=="4":
                                pass
                            else:
                                break






    else:
        break

