import time
import os
import sys

def simulate_app():
    """Simulates an application that crashes deterministically."""

    # Simulate out-of-memory (OOM) kill (likely to be fixed with resource limits)
    print("Simulating OOM kill (allocating 600MB)...")
    big_list = [bytearray(1024 * 1024) for _ in range(600)]  # Roughly 600MB
    time.sleep(1)  # To show the message before crash.


    # Simulate a crash due to an environment variable being absent
    print("Simulating missing environment variable 'REQUIRED_ENV_VAR'...")
    if not os.environ.get("REQUIRED_ENV_VAR"):
        print("Environment variable REQUIRED_ENV_VAR not set. Exiting.")
        sys.exit(1)

    # Simulate a crash due to a file not existing.
    print("Simulating missing file 'missing_file.txt'...")
    try:
        with open("/data/missing_file.txt", "r") as f:
            pass
    except FileNotFoundError:
        print("missing_file.txt not found. Exiting")
        sys.exit(1)

    # Simulate normal operation (this will never be reached in this deterministic version)
    print("Application running normally...")
    time.sleep(5)

if __name__ == "__main__":
    simulate_app()