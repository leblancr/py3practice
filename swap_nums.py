class SwapNos:
    def swap(self, x, y):
        print(f"values before swap: {x} and {y}")
        x = x + y;
        y = x - y;
        x = x - y;
        print(f"values after swap: {x} and {y}")
      

def main():
    swap_nums = SwapNos()
    print("Calling swap function with inputs 2 and 3")
    swap_nums.swap(2, 3)
    print("Calling swap function with inputs -3 and 5")
    swap_nums.swap(-3, 5)
    
    
if __name__ == '__main__':
    main()
