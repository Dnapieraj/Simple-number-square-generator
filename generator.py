
def square_number_generator():
    number = 0
    while True:
        number += 1
        yield number * number

def main():
    try:
        count = int(input("How many squared numbers do you want to generate? "))
        if count <= 0:
            print("Please enter a positive number.")
            return
            
        generator = square_number_generator()
        squares = [next(generator) for _ in range(count)]
        
        print(f"First {count} squared numbers: {squares}")
        
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()