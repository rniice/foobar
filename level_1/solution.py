#i_love_lance_janice
def answer(s):
    decoder     = dict()
    key_encoded = "abcdefghijklmnopqrstuvwxyz"
    key_decoded = key_encoded[::-1]

    for i, char in enumerate(key_encoded):
        decoder[char] = key_decoded[i]

    d_list = [decoder[char] if char in list(key_encoded) else char for char in list(s)]
    return "".join(d_list)
