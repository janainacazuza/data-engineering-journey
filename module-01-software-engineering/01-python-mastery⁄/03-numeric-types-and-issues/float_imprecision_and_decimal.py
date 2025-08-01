## Float Imprecision and Decimal Module Example
# This code demonstrates the imprecision of floating-point arithmetic in Python
# and how to use the Decimal module to avoid such issues.

print(
    f"Float Imprecision and Decimal Module Example, 0.2 + 0,1 = 0,3 ? 0.2 + 0.1 =  {0.2 + 0.1}"
)  # Output: Float Imprecision and Decimal Module Example, 0.2 + 0,1 = 0,3 ? 0.2 + 0.1 = 0.30000000000000004
# float imprecision is because fractional numbers cannot be represented exactly in binary floating-point format.

from decimal import Decimal

Decimal("0.2") + Decimal("0.1") == Decimal("0.3")  # True
print(
    f"Decimal Imprecision Example, Decimal(0.2) + Decimal(0.1) == Decimal(0.3) ? {Decimal('0.2') + Decimal('0.1') == Decimal('0.3')}"
)  # Output: Decimal Imprecision Example, Decimal(0.2) + Decimal(0.1) == Decimal(0.3) ? True
# important to use Decimal for precise decimal arithmetic, especially in financial applications.
# IMPORTTANT: Generating Decimal objects from strings is crucial to avoid float imprecision. because if you use float to generate Decimal, it will still have the imprecision.
