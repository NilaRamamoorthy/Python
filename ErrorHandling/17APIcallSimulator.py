import random
import time
import logging

# Setup logger
logging.basicConfig(filename="api_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Custom exception
class InvalidResponseError(Exception):
    pass

# Simulated API call
def fake_api_call():
    outcomes = ['success', 'timeout', 'connection_error', 'invalid_response']
    result = random.choice(outcomes)

    if result == 'timeout':
        raise TimeoutError("The request timed out.")
    elif result == 'connection_error':
        raise ConnectionError("Failed to connect to server.")
    elif result == 'invalid_response':
        raise InvalidResponseError("API returned an invalid response.")
    else:
        return {"status": 200, "data": "Hello from API"}

# Retry logic
def call_api_with_retries(retries=3):
    attempt = 0
    while attempt < retries:
        try:
            print(f"🔄 Attempt {attempt + 1}...")
            response = fake_api_call()
            print("✅ API Call Successful:", response)
            return
        except (TimeoutError, ConnectionError, InvalidResponseError) as e:
            print(f"⚠️ Error: {e}")
            logging.info(f"Attempt {attempt + 1} failed: {e}")
        finally:
            logging.info(f"Completed attempt {attempt + 1}")
            attempt += 1
            time.sleep(1)

    print("❌ All attempts failed. Please try again later.")

# Run simulation
call_api_with_retries()
