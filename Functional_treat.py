print("Welcome to the Data Analyzer and Transformer Program.")
while True:
    
    def total_elements(data):
                '''
                total_elements():
                This function calculates the total number of elements in the given 1D array.
                
                Parameters:
                --------------------------
                data (list): A list of integers representing the 1D array.

                Return Value:
                --------------------------
                int: The total number of elements in the input list.
                '''
                count = 0
                for i in data:
                    count+=1
                return count
            
    def minimum(data):
        '''
        minimum():
        This function shows the minimum value in the given 1D array.
        
        Parameters:
        --------------------------
        data (list): A list of integers representing the 1D array
        Return Value:
        --------------------------
        int: The minimum value in the input list.
        '''
        min_value =data[0]
        for i in data:
            if i<min_value:
                min_value=i
        return min_value
            
    def maximum(data):
        '''
        maximum():
        This function shows the maximum value in the given 1D array.
        
        Parameters:
        --------------------------
        data (list): A list of integers representing the 1D array

        Return Value:
        --------------------------
        int: The maximum value in the input list.
        '''
        max_value=data[0]
        for i in data:
            if i>max_value:
                max_value=i
        return max_value
    
    def sum_of_elements(data):
        '''
        sum_of_elements():
        This function calculates the sum of all elements in the given 1D array.
        
        Parameters:
        --------------------------
        data (list): A list of integers representing the 1D array

        Return Value:
        --------------------------
        int: The sum of all elements in the input list.
        '''
        total_sum = 0
        for i in data:
            total_sum+=i
        return total_sum
    
    def average(data):
        '''
        average():
        This function calculates the average value of all elements in the given 1D array.
        
        Parameters:
        --------------------------
        data (list): A list of integers representing the 1D array

        Return Value:
        --------------------------
        float: The average value of all elements in the input list.
        '''
        if total_elements(int_data) == 0:
            return 0
        avg = sum_of_elements(int_data)/total_elements(int_data)
        return avg
    
    def factorial(n):
        '''
        factorial():
        This function calculates the factorial of a given number using recursion
        Parameters:
        --------------------------
        n (int): The number for which the factorial is to be calculated

        Return Value:
        --------------------------
        int: The factorial of the input number n.
        '''
        if n<=1:
            return 1
        else:
            return n*factorial(n-1)
    def dataset_statistics(data):
        '''
        dataset_statistics():
        This function calculates minimum, maximum, sum, as well as average for the given list
        Parameters:
        ---------------------------
        data (list): A list of integers representing 1D array

        Return Value:
        ---------------------------
        int: The minimum value in the input list.
        int: The maximum value in the input list.
        int: The sum of all elements in the input list.
        float: The average value of all elements in the input list.
        '''
        min_value = min(data)
        max_value = max(data)
        total_sum = sum(data)
        if len(data) == 0:
            avg = 0
        else:
            avg = total_sum/len(data)
        return min_value, max_value, total_sum, avg
    
    print(total_elements.__doc__)
    print(minimum.__doc__)
    print(maximum.__doc__)
    print(sum_of_elements.__doc__)
    print(average.__doc__)
    print(factorial.__doc__)
    print(dataset_statistics.__doc__)

    print("\nMain Menu:")
    print('''
    1. Input Data
    2. Display Data Summary (Built-in Functions)
    3. Calculate Factorial (Recursion)
    4. Filter Data by Threshold (Lambda Function)
    5. Sort Data
    6. Display Dataset Statistics (Return Multiple Values)
    7. Exit''')
    choice = int(input("Please enter your choice: "))
    match choice:
        case 1:
            data = input("Enter data for 1D array (seperated by spaces): ")
            int_data = [int(i) for i in data.split()]
            print("Data has been stored successfully.")

        case 2:
            
            
            print("Data Summary:")
            print(f"Total Elements: {total_elements(int_data)}")
            print(f"Minimum Value: {minimum(int_data)}")
            print(f"Maximum Value: {maximum(int_data)}")
            print(f"Sum of all Values: {sum_of_elements(int_data)}")
            print(f"Average Value: {average(int_data)}")

        case 3:
            
            num = int(input("Enter a number to calculate its factorial: "))
            print(f"Factorial of {num} is: {factorial(num)}")
        
        case 4:
            threshold = int(input("Enter a threshold value to filter out data above this value: "))
            Filtered_data = list(filter(lambda i: i>threshold, int_data))
            print(f"Filtered Data (values >= {threshold}): \n{Filtered_data}")

        case 5:
            print("Choose sorting option: ")
            print('''1. Ascending Order
2. Descending Order''')
            choice = int(input("Enter your choice: "))
            match choice:
                case 1:
                    int_data.sort()
                    print("Sorted Data in Ascending order: \n", int_data)
                case 2:
                    int_data.sort(reverse=True)
                    print("Sorted Data in Descending order: \n", int_data)
                case _:
                    print("Invalid Choice. Please enter 1 or 2..")
        case 6:
            
            min_val, max_val, total_sum, avg = dataset_statistics(int_data)
            print("Dataset Statistics: ")
            print(f"Minimum Value: {min_val}")
            print(f"Maximum Value: {max_val}")
            print(f"Sum of all Values: {total_sum}")
            print(f"Average Value: {avg}")
        case 7:
            print("Thank you for using the Data Analyzer and Transformer Program. Goodbye!")
            break
        case _:
            print("Invalid Choice. Please enter (1-7)")

print("Using 1D and 2D arrays")
print("\nChoose an option: ")
print('''1. Create a 1D array
2. Create a 2D array''')
choice = int(input("Enter your choice: "))
match choice:
    case 1:
        size = int(input("Enter the size of the 1D array: "))
        array_1D = []
        for i in range(size):
            element = int(input(f"Enter element {i+1}: "))
            array_1D.append(element)
        print("1D Array created successfully: ", array_1D)
        array_1D.sort()
        print("Sorted 1D Array in ascending order: ", array_1D)
        array_1D.sort(reverse=True)
        print("Sorted 1D Array in descending order: ", array_1D)
    
    case 2:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        array_2D = []
        for i in range(rows):
            array_1D = []
            array_2D.append(array_1D)
        for j in array_2D:
            for k in range(cols):
                element = int(input(f"Enter element for row {array_2D.index(j)+1}, column {k+1}: "))
                j.append(element)
        print("2D Array created successfully: ")
        for row in array_2D:
            for element in row:
                print(element, end=" ")
            print()
        asc_sort = sorted(array_2D, key = lambda x:x[0])
        print("Sorted 2D Array in ascending order based on first column: ")
        for row in asc_sort:
            for element in row:
                print(element, end=" ")
            print()
        desc_sort = sorted(array_2D, key = lambda x:x[0], reverse=True)
        print("Sorted 2D Array in descending order based on first column: ")
        for row in desc_sort:
            for element in row:
                print(element, end=" ")
            print()
    case _:
        print("Invalid Choice. Please enter 1 or 2..")  