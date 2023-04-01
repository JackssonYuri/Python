secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = int(input("number: "))

while number != secret_number:
    print("Tente de novo")
    number = int(input("number: "))
    
print("Você acertou")
