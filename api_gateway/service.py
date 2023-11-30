import requests

AUTH_URL = "http://localhost:8000/"


def register_user(request):
    registration_data = request.data
    response = requests.post(f'{AUTH_URL}/auth/user/register/', json=registration_data)
    return response


def update_user(request):
    login_data = request.data
    headers = generate_authentication(request)
    response = requests.put(f'{AUTH_URL}/auth/users/update/', json=login_data, headers=headers)
    return response


def user_record(request, user_id):
    headers = generate_authentication(request)
    response = requests.get(f'{AUTH_URL}auth/users/record/?user_id={user_id}', json="None", headers=headers)
    return response


def user_delete(request, user_id):
    headers = generate_authentication(request)
    response = requests.delete(f'{AUTH_URL}auth/users/delete/?user_id={user_id}', json="None", headers=headers)
    print(response)
    return response


def generate_token(request):
    login_data = request.data
    response = requests.post(f'{AUTH_URL}/auth/token', json=login_data)
    return response


def generate_authentication(request):
    authorization_header = request.headers.get('Authorization')
    headers = {'Authorization': authorization_header, 'Content-Type': 'application/json'}
    return headers
