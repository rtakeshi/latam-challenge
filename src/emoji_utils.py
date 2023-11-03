import emoji


def extract_emojis(text):
    return emoji.get_emoji_regexp().findall(text)