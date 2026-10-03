# Function that simulates the login system logic
def login(username, password):
    if username == "admin" and password == "123456":
        return "Dashboard"
    return "Invalid credentials"

# Test case 1: Successful login
def test_successful_login():
    result = login("admin","123456")
    assert result == "Dashboard"
    print("\n[SUCCESS] Test Passed: User redirected to dashboard.")

# Test Case 2: Failed login with wrong password
def test_failed_login():
    result = login("admin", "wrong_password")
    assert result == "Invalid credentials"
    print("[SUCCESS] Test Passed: Error message displayed correctly.")

# Execute tests
if __name__ == "__main__":
    test_successful_login()
    test_failed_login()