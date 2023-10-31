#include <stdio.h>
#include <iostream>
#include <vector>

int sum(std::vector<int> numbers) {
    int min, max;
    min = max = numbers[0];
    int sum = 0;
    for (int i = 0; i < numbers.size(); i++) {
      if (numbers[i] < min) {
        min = numbers[i];
      } else if (numbers[i] > max) {
        max = numbers[i];
      }
      sum += numbers[i];
    }
    return sum-min-max;
}

int main() {
	std::cout << sum({ 6, 2, 1, 8, 10 }) << "\n";
	std::cout << sum({ 1, 1, 11, 2, 3 }) << "\n";
	return 0;
}
