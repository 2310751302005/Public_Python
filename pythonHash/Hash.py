import hashlib

def hash_string(input_string):
    """
    Generate a SHA-256 hash for the given input string.
    """
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return sha256_hash.hexdigest()

def verify_hash(input_string, expected_hash):
    """
    Verify that the SHA-256 hash of the input string matches the expected hash.
    """
    return hash_string(input_string) == expected_hash

def compare_hashes(input_string1, input_string2):
    """
    Compare the SHA-256 hashes of two input strings.
    """
    hash1 = hash_string(input_string1)
    hash2 = hash_string(input_string2)
    return hash1 == hash2

# Test the hash algorithm
if __name__ == "__main__":
    test_string = "Hello, world!"
    test_string2 = "Hello, world!"
    different_string = "Hello, Universe!"

    # Generate hash
    hash1 = hash_string(test_string)
    hash2 = hash_string(test_string2)
    different_hash = hash_string(different_string)

    print(f"Hash for '{test_string}': {hash1}")
    print(f"Hash for '{test_string2}': {hash2}")
    print(f"Hash for '{different_string}': {different_hash}")

    # Verify hash
    is_verified = verify_hash(test_string, hash1)
    print(f"Hash verification for '{test_string}': {is_verified}")

    # Compare hashes
    are_hashes_equal = compare_hashes(test_string, test_string2)
    print(f"Are hashes equal for '{test_string}' and '{test_string2}': {are_hashes_equal}")

    are_hashes_equal_different = compare_hashes(test_string, different_string)
    print(f"Are hashes equal for '{test_string}' and '{different_string}': {are_hashes_equal_different}")
