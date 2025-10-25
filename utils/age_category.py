def age_mother_cat(age):
    """Returns the age category for a mother."""

    if age < 20:
        return 'Less than 20 years'
    elif age < 25:
        return '20-24 years'
    elif age < 30:
        return '25-29 years'
    elif age < 35:
        return '30-34 years'
    elif age < 40:
        return '35-39 years'
    elif age < 45:
        return '40-44 years'
    elif age < 50:
        return '45-49 years'
    else:
        return '50 years or older'


def age_category(a, age_th=[15, 18, 24, 44, 65]):
    """Returns the age category for a person."""

    if a < age_th[0]:
        return 1
    for i in range(1, len(age_th)):
        if (a >= age_th[i-1]) & (a < age_th[i]):
            return i+1
    return len(age_th)+1
