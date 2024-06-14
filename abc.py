import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

def read_cookies(file_path):
    with open(file_path, 'r') as file:
        cookies = file.readlines()
    cookies = [cookie.split(': ')[1].strip() for cookie in cookies]
    return cookies

def send_friend_request(cookie, user_id):
    friend_request_url = f"https://friends.roblox.com/v1/users/{user_id}/request-friendship"
    headers = {
        'Cookie': f'.ROBLOSECURITY={cookie}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Content-Type': 'application/json',
        'X-CSRF-TOKEN': ''
    }

    try:
        initial_response = requests.post(friend_request_url, headers=headers)
        
        if initial_response.status_code == 403:
            csrf_token = initial_response.headers.get('x-csrf-token')
            if csrf_token:
                headers['X-CSRF-TOKEN'] = csrf_token

                friend_request_response = requests.post(friend_request_url, headers=headers)

                if friend_request_response.status_code == 200:
                    return True
                else:
                    print(f"Thất bại - ID: {user_id} - Lỗi: {friend_request_response.text}")
                    return False
        return False
    except requests.exceptions.RequestException as e:
        print(f"Yêu cầu thất bại: {e}")
        return False

def send_friend_requests(cookie, user_id, success_count):
    if send_friend_request(cookie, user_id):
        success_count.append(user_id)

def main():
    cookies = read_cookies('cookie.txt')
    print(f"Đã tải: {len(cookies)} cookie.")
    user_id_to_friend = input("Nhập id tài khoản: ")
    num_requests = int(input("Nhập số lượt cần kết bạn: "))

    success_count = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        for _ in range(num_requests):
            cookie = random.choice(cookies)
            executor.submit(send_friend_requests, cookie, user_id_to_friend, success_count)

    print(f"Đã gửi {len(success_count)} yêu cầu kết bạn thành công.")

if __name__ == "__main__":
    main()
