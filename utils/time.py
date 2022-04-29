from datetime import datetime


def time(text, time):
    now = datetime.utcnow()
    last = time

    date = now - last

    txt = text + ' {0} {1} ago'

    if date.days <= 0:
        if date.seconds // 3600 <= 0:
            if (date.seconds // 60) % 60 <= 0:
                txt = txt.format(date.seconds, "seconds" if date.seconds != 1 else "second")
            else:
                txt = txt.format((date.seconds // 60) % 60, "minutes" if (date.seconds // 60) % 60 != 1 else "minute")
        else:
            txt = txt.format(date.seconds // 3600, "hours" if date.seconds // 3600 != 1 else "hour")
    else:
        txt = txt.format(date.days, "days" if date.days != 1 else "day")

    return txt
