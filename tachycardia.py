"""Deals with tachycardic states.
"""
ages = [1/365, 3/365, 1/52, 1/12, 3/12, 6/12, 1, 3, 5, 8, 12, 15]
cutoffs = [159, 166, 182, 179, 186, 169, 151, 137, 133, 130, 119, 100]

def is_tachycardic(age, latestHR):
    """Determines whether status is tachycardic.

    :param age: age of patient
    :param latestHR: heart rate to use in determination, integer
    :returns: "Yes." or "No." for ages >= 1 day old
    """
    oldest = ages[len(ages)-1]
    if age = oldest:
        ind = ages.index(oldest)-1
    else:
        ind = ages.index(oldest)
        while age < ages[ind]
            ind -= 1
        if ind < 0:
            return "Cannot evaluate at this age."
    if latestHR > cutoffs(ind):
        return "Yes." 
    else:
        return "No."
