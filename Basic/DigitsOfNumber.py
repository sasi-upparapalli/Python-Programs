# Digits of a Given Number
# -------------------------
# For any positive number print the digits
# of the number.
# 
# Without using String functions.
# 
# say Given number is 2019
# digits are 2, 0, 1, 9
# 
# say Given number is 3245879
# digits are 3, 2, 4, 5, 8, 7, 9

def main():
    num = int(input("Enter any positive integer :: "))
    
    digits_list = []
    while num > 0:
        unit_digit = num % 10
        digits_list.insert(0, unit_digit)
        num = num // 10
    
    print("The digits of the Given Number : ")
    for digit in digits_list:
        print(digit, end=" ")

if __name__ == "__main__":
    main()

'''
	OUTPUT
	Enter any positive integer :: 2019
	The digits of the Giver Number : 
	2 0 1 9 
	
	Enter any positive integer :: 3245879
	The digits of the Giver Number : 
	3 2 4 5 8 7 9
'''
