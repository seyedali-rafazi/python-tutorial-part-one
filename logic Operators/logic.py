high_income = True
high_credit = False
student = True

if not student and (high_credit or high_income):
    print("eligiblae")
else:
    print("not eligible")