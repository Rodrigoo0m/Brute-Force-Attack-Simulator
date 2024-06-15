# Brute Force Attack Simulator

This project demonstrates a brute force attack on a login system. The script is intended for educational purposes only and should be used in a controlled environment where you have explicit permission to test the security of the system.

## Disclaimer

**WARNING:** Performing brute force attacks on systems without authorization is illegal and unethical. Use this script only in controlled environments and on systems where you have explicit permission to test. The author is not responsible for any misuse of this script.

## Features

- Allows the user to input the login system URL.
- Reads usernames from `usernames.txt` and passwords from `passwords.txt`.
- Attempts to log in using every combination of usernames and passwords.
- Logs the result of each login attempt.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/brute-force-attack-simulator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd brute-force-attack-simulator
    ```
3. Install the required libraries:
    ```bash
    pip install requests
    ```

## Usage

1. Create `usernames.txt` and `passwords.txt` in the project directory.

    **Example of `usernames.txt`:**
    ```
    admin
    user1
    user2
    ```

    **Example of `passwords.txt`:**
    ```
    123456
    password
    12345678
    qwerty
    abc123
    admin
    ```

2. Run the script:
    ```bash
    python brute_force_attack.py
    ```
3. Enter the login system URL when prompted:
    ```
    Enter the login system URL: http://example.com/login
    ```

## Example Output

```
Enter the login system URL: http://example.com/login
[-] Login failed. Username: admin | Password: 123456
[-] Login failed. Username: admin | Password: password
[-] Login failed. Username: admin | Password: 12345678
[-] Login failed. Username: admin | Password: qwerty
[-] Login failed. Username: admin | Password: abc123
[-] Login failed. Username: admin | Password: admin
[-] Login failed. Username: user1 | Password: 123456
[-] Login failed. Username: user1 | Password: password
[+] Successful login! Username: user1 | Password: 12345678
```

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-feature-branch`
5. Create a pull request.

```

### Summary of the README.md

- **Disclaimer**: Warns users about the legal and ethical considerations.
- **Features**: Describes what the script does.
- **Requirements**: Lists the requirements to run the script.
- **Installation**: Provides step-by-step instructions to set up the project.
- **Usage**: Guides the user on how to use the script.
- **Example Output**: Shows an example of what the output might look like.
- **Contributing**: Explains how others can contribute to the project.
