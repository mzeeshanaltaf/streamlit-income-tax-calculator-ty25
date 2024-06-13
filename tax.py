def format_number(num):
    if num == int(num):
        return int(f"{int(num):}")
    else:
        return float(f"{num:.2f}")


def tax_calculation_ty24(annual_salary):
    it_ty_24 = 0

    if annual_salary <= 600000:
        it_ty_24 = 0

    elif 600000 < annual_salary <= 1200000:
        it_ty_24 = 0.025 * (annual_salary - 600000)

    elif 1200000 < annual_salary <= 2400000:
        it_ty_24 = 15000 + 0.125 * (annual_salary - 1200000)

    elif 2400000 < annual_salary <= 3600000:
        it_ty_24 = 165000 + 0.225 * (annual_salary - 2400000)

    elif 3600000 < annual_salary <= 6000000:
        it_ty_24 = 435000 + 0.275 * (annual_salary - 3600000)

    elif annual_salary > 6000000:
        it_ty_24 = 1095000 + 0.35 * (annual_salary - 6000000)

    return format_number(it_ty_24)


def tax_calculation_ty25(annual_salary):
    it_ty_25 = 0

    if annual_salary <= 600000:
        it_ty_25 = 0

    elif 600000 < annual_salary <= 1200000:
        it_ty_25 = 0.05 * (annual_salary - 600000)

    elif 1200000 < annual_salary <= 2200000:
        it_ty_25 = 30000 + 0.15 * (annual_salary - 1200000)

    elif 2200000 < annual_salary <= 3200000:
        it_ty_25 = 180000 + 0.25 * (annual_salary - 2200000)

    elif 3200000 < annual_salary <= 4100000:
        it_ty_25 = 430000 + 0.30 * (annual_salary - 3200000)

    elif annual_salary > 4100000:
        it_ty_25 = 700000 + 0.35 * (annual_salary - 4100000)

    return format_number(it_ty_25)
