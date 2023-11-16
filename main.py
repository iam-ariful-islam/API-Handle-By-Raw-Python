import requests


# Check the internet connect
def check_internet_connection():
    try:
        response = requests.get('http://www.google.com', timeout=5)
        if response.status_code == 200: return True
        else: return False
    except requests.RequestException: return False


# get user id from api login provide username and password
def api_login(data):
    response = requests.post('http://localhost:8000/api/user/login/', data=data)
    if response.status_code == 200:
        user_id = response.json().get('user_id')
        return user_id
    else: return response.json().get('errors')[0]


# retrieve user information
def get_user_info(user_id):
    response = requests.get('http://localhost:8000/api/user/user_id={}'.format(user_id))
    if response.status_code == 200: return response.json()
    else: return response.json().get('errors')[0]


# post user information
def post_user_info(data):
    response = requests.post('http://localhost:8000/api/user/add/', data=data)
    if response.status_code == 201: return True
    else: return response.json().get('user_id')[0]


# root function
def main():
    auth_data = {
        'username': 'user22',
        'password': 'user22'
    }
    user_data = {
        'name': 'admin',
        'age': '28',
        'mobile': '01x'
    }

    if check_internet_connection():
        user_id = api_login(auth_data)
        if user_id:
            get_user_info(user_id)
        post_user_info(user_data)

    else: print('Please first chheck your internet connection')


# root
if __name__ == '__main__':
    main()