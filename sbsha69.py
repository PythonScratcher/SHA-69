def sbsha69(input_string):
    # Initialize hash value
    hash_value = 0
    
    # Process each character in the input string
    for char in input_string:
        hash_value = (hash_value * 31 + ord(char)) & 0xFFFFFFFF  # Applying a simple hash function
    
    return hash_value
