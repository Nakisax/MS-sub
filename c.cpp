#include <iostream>

// Function to calculate factorial recursively
int factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

int main() {
    int num;
    std::cout << "Enter a number to calculate its factorial: ";
    std::cin >> num;
    
    // Check if the number is negative
    if (num < 0) {
        std::cout << "Factorial is not defined for negative numbers." << std::endl;
        return 1; // Return non-zero value to indicate error
    }

    // Calculate factorial
    int result = factorial(num);
    std::cout << "Factorial of " << num << " is: " << result << std::endl;
    
    return 0; // Return zero to indicate successful completion
}
