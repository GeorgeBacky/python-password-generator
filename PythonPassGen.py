import os, random, string
 
def get_random_string(min_chars=10, max_chars=15):
    all_chars = string.ascii_letters + string.digits + string.punctuation
    random.seed = (os.urandom(1024))  # this line can be removed
    random_str = "".join(random.choice(all_chars)
    for _ in range(random.randint(min_chars, max_chars)))
    return random_str
 
 
print(get_random_string())
