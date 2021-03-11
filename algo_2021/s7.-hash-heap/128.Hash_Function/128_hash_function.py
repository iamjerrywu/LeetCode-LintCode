class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        hash_value = 0
        for c in key: 
            hash_value = (hash_value * 33 + ord(c)) % HASH_SIZE
        return hash_value