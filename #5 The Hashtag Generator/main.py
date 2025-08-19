def generate_hashtag(s):
    if not s or s.strip() == "":
        return False

    words = s.strip().split()
    capitalized_words = [word.upper() for word in words]

    result = "#" + "".join(capitalized_words)
    return result if len(result) <= 140 else False
