import hashlib

message = "Hello, world!"
hash_object = hashlib.sha256(message.encode())
hash_hex = hash_object.hexdigest()

print(f"SHA-256 hash of '{message}' is: {hash_hex}")

