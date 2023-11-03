import emoji


def extract_emojis(text):
    return emoji.get_emoji_regexp().findall(text)


extract_emojis_udf = udf(emoji_utils.extract_emojis, ArrayType(StringType()))
