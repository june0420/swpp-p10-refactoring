# TODO: 1. Use one-liners
#def count_asterisk_exceed_five(text):
#    return text.count("*") > 5

def censor_alert(text, word, replaced_char, alert_num):
    while word in text:
        text = text[:text.find(word)] + replaced_char * len(word) + text[text.find(word) + len(word):]
    if text.count(replaced_char) > alert_num:
        print("More than " + str(alert_num) + " " + replaced_char)
    return text

if __name__ == "__main__":
    text = """Because he's the hero Gotham deserves but not the one it needs right now.
So we will hunt him, because he can take it. Because he's not out hero.
He is a silent guardian, a watchful protector... a dark knight."""

    word1 = "hero"
    word2 = "silent"

    # TODO: 4. Consider general usage
    # TODO: 3. Substitute algorithm

    # TODO: 2. Extract method, remove duplicated code
    # Censor `word1` from `text`
    text = censor_alert(text, word1, '*', 5)

    # TODO: 2. Extract method, remove duplicated code
    # Censor `word2` from `text`
    text = censor_alert(text, word2, '*', 5)

    # Print result `text`
    print(text)