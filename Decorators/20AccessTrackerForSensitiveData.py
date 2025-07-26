import datetime

class SecureData:
    def __init__(self, secret):
        self._secret = secret
        self._access_log = []

    @property
    def secret(self):
        access_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self._access_log.append(access_time)
        print(f"[ACCESS] Secret data accessed at {access_time}")
        return self._secret

    @secret.setter
    def secret(self, value):
        raise AttributeError("Modification of secret data is not allowed.")

    def show_access_log(self):
        return self._access_log

# Example usage
data = SecureData("TopSecret123")
print(data.secret)  # Access log created
print(data.secret)  # Access log created again

# Attempt to modify the secret
try:
    data.secret = "NewSecret456"
except AttributeError as e:
    print("Error:", e)

# View access log
print("Access History:", data.show_access_log())
