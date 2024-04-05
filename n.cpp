#include <iostream>
#include <random>

int main() {
    // Seed the random number generator with a random device
    std::random_device rd;
    std::mt19937 gen(rd());

    // Define the distribution (uniform distribution in this case)
    std::uniform_int_distribution<int> dist(1, 100); // Generates random numbers between 1 and 100

    // Generate random numbers
    for (int i = 0; i < 10; ++i) {
        int randomNumber = dist(gen);
        std::cout << "Random Number " << i + 1 << ": " << randomNumber << std::endl;
    }

    return 0;
}
