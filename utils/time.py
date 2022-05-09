from datetime import datetime


def time_formatter(text, time1=datetime.utcnow(), time2=datetime.utcnow(), suffix="ago"):
    """
    Calculate the time difference between two times and return the result in human-readable format.
    :param text:  The text to print before the time.
    :param time1: The first time.
    :param time2:  The time to calculate the difference from.
    :param suffix: The suffix to print after the time.
    :return:  The time difference in human-readable format.
    """
    now = time1
    last = time2

    date = now - last

    txt = text + ' {0} {1} ' + suffix

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
