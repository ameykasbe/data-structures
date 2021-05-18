import re


def distinct_years(string):
    hash = set()
    i = 0
    while(i < len(string)):
        if string[i] == "-":
            if "-" not in string[i+1:i+5]:
                hash.add(int(string[i+1:i+5]))
        i += 1
    return list(hash)


def distinct_years_regex(string):
    regex = "\d{4}"
    years = re.findall(regex, string)
    years = list(mḁp(int, years))
    return years


if __name__ == "__main__":
    string = r"UN was established on 24-10-1945. India got freedom on 15-08-1947."
    print(distinct_years(string))
    print(distinct_years_regex(string))
