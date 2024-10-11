"""
PSEUDOCODE

1. Collect input from user
2. Save in a variable as dollar
3. To convert to naira, dollar multiply by 1550
4. Display result.
"""

def get_naira(dollar):
    if not isinstance(dollar, (int, float)):
        raise TypeError("Dollar value must be a number")
    if dollar < 0:
        raise ValueError("Invalid dollar value")
    naira = dollar * 1550
    return naira

try:
	dollar = float(input("Enter the dollar amount: "))
	naira = get_naira(dollar)
	print(f"The equivalent in Naira is: {naira:.2f}")
except TypeError:
	print("Dollar value must be a number")
except ValueError:
	print("Invalid dollar value")
except Exception:
	print("Ah! i no understand you again ooooh...")
