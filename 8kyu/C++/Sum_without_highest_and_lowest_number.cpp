#include <stdio.h>
#include <iostream>
#include <vector>

int sum(std::vector<int> numbers){
    if (numbers.size() > 1) {
      int min, max;
      min = max = numbers[0];
      int sum = 0;
      for (int i: numbers) {
        if (i < min) {
          min = i;
        } else if (i > max) {
          max = i;
        }
        sum += i;
      }
      return sum-min-max;
    } else {
      return 0;
    }
}

int main() {
	std::cout << sum({ 6, 2, 1, 8, 10 }) << "\n";
	std::cout << sum({ 1, 1, 11, 2, 3 }) << "\n";
	return 0;
}
