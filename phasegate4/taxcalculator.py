print("""
    0: Single
    1: Married filing jointly
    2: Married filing separately
    3: Head of house
    """)
filing_status = int(input("Select an option: "))
income = float(input("The income: "))
tax = 0

def calculate_tax():
    match filing_status:
        case 0:
            print("Single")
            
            if income > 0 and income <= 8350:
                tax = income * 0.1
                return tax

            if income > 8350 and income <= 33950:
                balance = income - 8350
                tax = balance * 0.15
                return tax
             
            if income > 33950 and income <= 82250:
                balance = balance - 33950
                tax = balance * 0.25
                return tax

            if income > 82250 and income <= 171550:
                balance = balance- 82250 
                tax = balance * 0.28
                return tax

            if income > 171550 and income <= 372750:
                balance = balance - 171550
                tax = balance * 0.33
                return tax

            else:
                balance = balance - 372750
                tax = balance * 0.35
                return tax

print(tax)





