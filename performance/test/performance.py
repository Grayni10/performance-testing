import requests  # Allows us to make HTTP requests.
import time  # Used to measure the time it takes for a request.
import concurrent.futures  # Lets us run multiple tasks at the same time (simulate multiple users).
import pytest  # Testing framework to run our test.


def perform_login():
    """
    This function simulates one login attempt.
    It sends a login request to a demo endpoint and measures how long it takes.
    """
    # Start the timer before sending the request.
    start = time.time()

    # URL of the login endpoint.
    login_url = "https://reqres.in/api/login"

    # The login data (credentials) we are using.
    # These are the same for every request in this example.
    login_data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    # HTTP headers tell the server that we are sending JSON data.
    headers = {"Content-Type": "application/json"}

    # Send a POST request to the login URL with the login data (as JSON).
    response = requests.post(login_url, json=login_data, headers=headers)

    # Calculate how long the request took in milliseconds.
    elapsed = (time.time() - start) * 1000
    return response, elapsed


# This decorator tells pytest to run this test with num_users set to 10.
@pytest.mark.parametrize("num_users", [10])
def test_concurrent_login(num_users):
    """
    This test simulates 10 users trying to log in at the same time.
    It checks:
      - That every login request returns a 200 OK response.
      - That each login request finishes in less than 500 milliseconds.
    """
    # This list will store the time each login request takes.
    times = []

    # Create a pool of threads to simulate multiple users logging in concurrently.
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_users) as executor:
        # Create a list of tasks. Each task is a call to perform_login().
        future_list = [executor.submit(perform_login) for _ in range(num_users)]

        # As each task completes, process its result.
        for future in concurrent.futures.as_completed(future_list):
            # Get the response and time taken for this login.
            result_response, result_time = future.result()
            times.append(result_time)

            # Check that the response code is 200 (meaning OK).
            assert result_response.status_code == 200, (
                    "Login did not succeed, status code: " + str(result_response.status_code)
            )

            # Print the time this login took.
            print(f"Login took {result_time:.2f} ms")

    # After all requests have finished, check that none took 500 ms or more.
    for t in times:
        assert t < 1500, f"One of the requests took too long: {t:.2f} ms"
