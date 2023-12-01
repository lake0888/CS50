months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def get_Date():
    type = False
    str_date = ""
    m = ""
    d = ""
    y = ""
    date = {}
    while True:
        try:
            str_date = input("Enter a valid date \n")
            m, d, y = str_date.split("/")
            ok = True
            if (len(m.strip()) != 1 and len(m.strip()) != 2) or (len(d.strip()) != 1 and len(d.strip()) != 2) or (len(y.strip()) != 4):
                ok = False
            else:
                m = int(m)
                d = int(d)
                y = int(y)
                if m < 1 or m > 12 or d < 1 or d > 31:
                    ok = False
            if not ok:
                continue
        except EOFError:
            break
        except ValueError:
            try:
                m_d, y = str_date.split(",")
                if len(y.strip()) != 4:
                    continue
                else:
                    y = int(y)
            except ValueError:
                pass
            else:
                try:
                    m, d = m_d.split(" ")
                    if (len(d.strip()) != 1 and len(d.strip()) != 2):
                        continue
                    else:
                        d = int(d)
                        if d < 1 or d > 31:
                            continue
                except ValueError:
                    pass
                else:
                    if (m not in months):
                        pass
                    else:
                        break
        else:
            type = True
            break

    if not type and not m.isnumeric():
        m = months.index(m) + 1

    date["month"] = m
    date["day"] = d
    date["year"] = y

    return date


def main():
    date = get_Date()
    print(f"{ date['year'] }-{date['month']:02}-{date['day']:02}")


if __name__ == "__main__":
    main()