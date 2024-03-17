#include <stdio.h>
#include <iostream>

int rental_car_cost(int d){
  if (d < 3) {
    return 40 * d;
  }
  else if (d >= 3 && d < 7) {
    return 40 * d - 20;
  } else {
    return 40 * d - 50;
  }
}

int main() {
	std::cout << rental_car_cost(1) << "\n";
	std::cout << rental_car_cost(2) << "\n";
	std::cout << rental_car_cost(3) << "\n";
	std::cout << rental_car_cost(4) << "\n";
	std::cout << rental_car_cost(5) << "\n";
	std::cout << rental_car_cost(6) << "\n";
	std::cout << rental_car_cost(7) << "\n";
	std::cout << rental_car_cost(8) << "\n";
	std::cout << rental_car_cost(9) << "\n";
	std::cout << rental_car_cost(10) << "\n";
	return 0;
}
