<<<<<<< HEAD
# -----------------------------------------Imports--------------------------------------------------------------------------------
import requests

# -----------------------------------------Functions------------------------------------------------------------------------------
=======
import requests

>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
def fetch_image(data):
    image_url = data["avatar_url"]
    return f"Avatar URL: {image_url}"

def fetch_name(data):
    name = data["name"]
    return f"Name: {name}"

def fetch_bio(data):
    bio = data["bio"]
    return f"Bio: {bio}"

def fetch_public_repos(data):
    public_repos = data["public_repos"]
    return f"Public Repositories: {public_repos}"

def fetch_followers_following(data):
    followers = data["followers"]
    following = data["following"]
    return f"Followers: {followers}, Following: {following}"

def fetch_date_of_creation(data):
    date_of_creation = data["created_at"]
    return f"Date of Creation: {date_of_creation}"

<<<<<<< HEAD
# -----------------------------------------API Request for Repositories----------------------------------------------------------------------------

=======
>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
def fetch_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repos_data = response.json()
    
    if response.status_code == 200:
        repo_names = [repo['name'] for repo in repos_data]
        return "\n".join(f"{index + 1}. {name}" for index, name in enumerate(repo_names))
    else:
        raise Exception("Failed to fetch repositories")

<<<<<<< HEAD
# -----------------------------------------API Request for user Details----------------------------------------------------------------------------
=======
>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
def api_request(enquiry_no, username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
<<<<<<< HEAD
    # -------------------------------------------------Handling Enquiry Number-------------------------------------------------------------
=======
    
>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
    if response.status_code == 200:
        match enquiry_no:
            case '1':
                return fetch_image(data)
            case '2':
                return fetch_name(data)
            case '3':
                return fetch_bio(data)
            case '4':
                return fetch_public_repos(data)
            case '5':
                return fetch_followers_following(data)
            case '6':
                return fetch_date_of_creation(data)
            case '7':
                return fetch_repositories(username)
            case _:
                return "--> Invalid Enquiry Number. Please Try Again <--"
    else:
        raise Exception("Failed to fetch user data")

<<<<<<< HEAD
# -----------------------------------------Main Function----------------------------------------------------------------------------

def main():

    # ------------------------------First Iteration of user -----------------------------------
=======
def main():
>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
    while True:
        print(50 * "*")
        print("WELCOME TO GITHUB ENQUIRY")
        print(50 * "*")
        print("Choose the Enquiry type :-")
        print("1. Avatar URL of your GitHub")
        print("2. Name of your GitHub Account")
        print("3. Bio of your GitHub")
        print("4. Public Repositories of your GitHub")
        print("5. Followers & Following of your GitHub")
        print("6. Date of Creation of your GitHub Account")
        print("7. List All Repositories of your GitHub")
        print("8. Nothing! Please Exit")
        print(50 * "*")
        
        enquiry_no = input("Enter Your Enquiry No.: ")
<<<<<<< HEAD
        # -------------------------------------------------Handling Exit--------------------------------------------------------------
=======
        
>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
        if enquiry_no == '8':
            print("Thank you for using GitHub Enquiry")
            break
        else:
<<<<<<< HEAD
        # -------------------------------------------------Handling User Input--------------------------------------------------------------
            username = input("Enter Your GitHub Username: ")
            try:
            # -------------------------------------------------Handling API Request--------------------------------------------------------------
                result = api_request(enquiry_no, username)
                print(f"Enquiry Result:\n{result}")
            except Exception as e:
                # -------------------------------------------------Handling Exception--------------------------------------------------------------
                print(f"Error: {e}")
            print(50 * "-" + " Exit " + 50 * "-")

# -----------------------------------------Main Function Call----------------------------------------------------------------------------

=======
            username = input("Enter Your GitHub Username: ")
            try:
                result = api_request(enquiry_no, username)
                print(f"Enquiry Result:\n{result}")
            except Exception as e:
                print(f"Error: {e}")
            print(50 * "-" + " Exit " + 50 * "-")

>>>>>>> fb259a028dc82760a1b4e3ec0ad84c7fbd261ad6
if __name__ == "__main__":
    main()
