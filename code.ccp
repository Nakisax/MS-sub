#include <iostream>
#include <cstdlib>

int main() {
    // Generate a random number between 1 and 100
    int randomNumber = rand() % 100 + 1;

    std::cout << "Welcome to the Random Number Game!" << std::endl;
    std::cout << "I have selected a random number between 1 and 100. Try to guess it!" << std::endl;

    int guess;
    int attempts = 0;

    do {
        std::cout << "Enter your guess: ";
        std::cin >> guess;
        attempts++;

        if (guess < randomNumber) {
            std::cout << "Too low! Try again." << std::endl;
        } else if (guess > randomNumber) {
            std::cout << "Too high! Try again." << std::endl;
        } else {
            std::cout << "Congratulations! You guessed the number " << randomNumber << " in " << attempts << " attempts." << std::endl;
        }
    } while (guess != randomNumber);

    return 0;
}
