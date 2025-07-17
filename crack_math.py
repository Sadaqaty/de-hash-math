#!/usr/bin/env python3
from itertools import product
import hashlib
import logging
import string
import argparse

# Setting up logging
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

# Function to generate mathematical expressions
def generate_expressions(chars, length, operators):
    # Correctly concatenate the list of operators as a string to chars
    combined = chars + ''.join(operators)
    for expr in product(combined, repeat=length):
        yield ''.join(expr)

# Function to crack the hash
def crack_hash(target_hash, hash_types, maxlen, operators):
    chars = string.digits + string.ascii_lowercase
    for htype in hash_types:
        logging.info(f"[*] Trying hash type: {htype}")
        for length in range(1, maxlen + 1):
            logging.info(f"[*] Trying expressions with length: {length}")
            for expr in generate_expressions(chars, length, operators):
                # Try hashing the expression and compare it to the target hash
                hashed = hashlib.new(htype, expr.encode()).hexdigest()
                if hashed == target_hash:
                    logging.info(f"[+] Match found: {expr}")
                    return expr, htype
    return None, None

# Main function for processing arguments and starting the cracking
def main():
    parser = argparse.ArgumentParser(description="Universal Hash Cracker for math-like expressions")
    parser.add_argument('--hash', required=True, help="Target hash to crack")
    parser.add_argument('--ops', required=True, help="Operators to use (e.g. '+-*/')")
    parser.add_argument('--maxlen', type=int, default=5, help="Maximum expression length")
    args = parser.parse_args()

    logging.info(f"[*] Auto-detecting hash type for: {args.hash}")
    hash_types = ['sha256', 'sha3_256', 'blake2s', 'ripemd256']

    # Try to crack the hash
    result, htype = crack_hash(args.hash.lower(), hash_types, args.maxlen, list(args.ops))
    if result:
        logging.info(f"[+] Cracked: {result} using hash type: {htype}")
    else:
        logging.error("[-] No match found.")

if __name__ == '__main__':
    main()
