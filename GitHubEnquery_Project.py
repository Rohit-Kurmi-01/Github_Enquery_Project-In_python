import requests

def fetch_image(data):
    Image_url = data["avatar_url"]
    return Image_url

def fetch_name(data):
    Name = data["name"]
    return Name

def fetch_bio(data):
    bio = data["bio"]
    return bio

def fetch_public_repos(data):
    public_repos = data["public_repos"]
    return public_repos

def fetch_followers_following(data):
    Followers = data["followers"]
    Following = data["following"]
    return Followers, Following

def fetch_date_of_creation(data):
    Date_of_creation = data["created_at"]
    return Date_of_creation



def api_request(Enquery_No):
    username = input("Enter Your Github Username:- ")
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
         match Enquery_No :
            case '1' :
                Image_url = fetch_image(data)
                return Image_url

            case '2' :
                Name = fetch_name(data)
                return Name

            case '3' :
                Bio = fetch_bio(data)
                return Bio

            case '4' :
                public_repos = fetch_public_repos(data)
                return public_repos

            case '5' :
                Followers, Following = fetch_followers_following(data)
                return Followers, Following

            case '6' :
                Date_of_creation = fetch_date_of_creation(data)
                return Date_of_creation

            case _ :
                 print("invailid Enquery No. Please Try Again")
                 notic = "--> Please Read All Enquery Number  <--"
                 return notic 
def main():

    while True:
        print(50*"*")
        print("WELCOME TO GITHUB ENQUERY")
        print(50*"*")
        print("Choose the Enquery type :- ")
        print("1. Image URL of your Github")
        print("2. Name of your Github Account")
        print("3. bio of your Github")
        print("4. public_repos of your Github")
        print("5. Followers & Following of your Github")
        print("6. Date of creation of your Github Account")
        print("7. Nothing ! Please Exit")
        print(50*"*")
        Enquery_No = str(input("Enter Your Enquery No.:- "))

        if Enquery_No == '7':
            print("Thanks You For Using Github Enquery")
            exit()
        else:
            
            try:
                result = api_request(str(Enquery_No))
                print(result)
            except Exception as e:
                print(f"Error: {e}")
            print(50*"-" + "Exit" + 50*"-")
            



if __name__ == "__main__":
    main() 