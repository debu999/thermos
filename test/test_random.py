"""Random Testing"""


def regextesting(pattern, text, iscasesensitive):
    import re
    boundedpattern = r"\s*".join(map(re.escape, pattern.split()))

    print boundedpattern


    regex = re.compile(r"\b{}\b".format(boundedpattern), re.IGNORECASE) if iscasesensitive else re.compile(
        r"\b{}\b".format(boundedpattern))

    for match in regex.finditer(text):
        print "%s:%s:%s" % (match.start(), " ".join(match.group(0).split()), match.end())



if __name__ =="__main__":
    pattern="Director's cut"
    text = "word famous director's \n cut in the city"
    iscasesensitive = True

    regextesting(pattern, text, iscasesensitive)