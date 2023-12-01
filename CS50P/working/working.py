import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(
        r"^((\d{1,2})(:(\d{2}))? (AM) to (\d{1,2})(:(\d{2}))? PM)|((\d{1,2})(:(\d{2}))? (PM) to (\d){1,2}(:(\d{2}))? AM)$",
        s,
    )
    if matches:
        groups = matches.groups()
        groups = get_group(groups)

        is_am = True if groups[4] == "AM" else False

        h_1 = int(groups[1])
        h_2 = int(groups[5])
        if not valid_hour(h_1) or not valid_hour(h_2):
            raise ValueError

        m_1 = groups[2]
        if m_1 != None:
            m_1 = int(groups[3])
            if not valid_minute(m_1):
                raise ValueError
        else:
            m_1 = 0

        m_2 = groups[6]
        if m_2 != None:
            m_2 = int(groups[7])
            if not valid_minute(m_2):
                raise ValueError
        else:
            m_2 = 0

        if is_am:
            if h_2 != 12:
                h_2 = update_hour(h_2)
            if h_1 == 12:
                h_1 = update_hour(h_1)
        else:
            h_1 = update_hour(h_1)
        return f"{h_1:02}:{m_1:02} to {h_2:02}:{m_2:02}"
    else:
        raise ValueError


def get_group(groups):
    left = []
    right = []
    i = 0
    while i < 8:
        left.append(groups[i])
        right.append(groups[i + 8])
        i += 1

    if left[0] != None:
        groups = left
    else:
        groups = right
    return groups


def valid_hour(h):
    return h >= 1 and h <= 12


def valid_minute(m):
    return m >= 0 and m < 60


def update_hour(h):
    h += 12
    if h == 24:
        h = 0
    return h


if __name__ == "__main__":
    main()
