import requests 
from datetime import datetime

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
    date_str = data["created_at"]
    # Parsing the date string 
    date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ") 
    # Converting to desired 
    formatted_date = date_obj.strftime("%Y-%m-%d %H:%M:%S")

    return f"Formatted Date and Time: {formatted_date}"

def api_request(enquiry_no, username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    
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
            case _:
                return "--> Invalid Enquiry Number. Please Try Again <--"
    else:
        raise Exception("Failed to fetch user data")

def main():
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
        print("7. Nothing! Please Exit")
        print(50 * "*")
        
        enquiry_no = input("Enter Your Enquiry No.: ")
        
        if enquiry_no == '7':
            print("Thank you for using GitHub Enquiry")
            break
        else:
            username = input("Enter Your GitHub Username: ")
            try:
                result = api_request(enquiry_no, username)
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            print(50 * "-" + " Exit " + 50 * "-")

if __name__ == "__main__":
    main()
