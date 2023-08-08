class ReverseNumber:
    def reverse_num(self, number):
        reversed_num = 0
    
        while int(number) != 0:
            digit = int(number % 10)
            print('digit:', digit)
            reversed_num = reversed_num * 10 + digit
            print('reversed_num:', reversed_num)
            number /= 10
            print('number:', int(number))
            
        return reversed_num
            
            
def main():
    num = 10025
    rn = ReverseNumber()
    
    reversed_num = rn.reverse_num(num)
    print(f"Input - {num} Output: {reversed_num}")
    
    
if __name__ == '__main__':
    main()
        
        
     