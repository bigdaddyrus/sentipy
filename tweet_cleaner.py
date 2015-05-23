def tweet_cleaner(text):
    import re
    text1 = ''.join(text)
    #text1 = str(text)
    text1 = re.sub(r'^https?:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'^http?:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'^http:\/\/.*[\r\n]*', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'RT', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r't.co', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r'@', '', text1, flags=re.MULTILINE);
    text1 = re.sub(r"(?:\@|https?\://)\S+", "", text1)
    return text1;
