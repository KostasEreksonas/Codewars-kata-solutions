#include <stdio.h>
#include <iostream>

int past(int h, int m, int s) {
  int result = 1000*(3600*h+60*m+s);
  return result;
}

int main() {
	std::cout << past(0, 0, 1) << " ms\n";
	std::cout << past(0, 1, 1) << " ms\n";
	std::cout << past(1, 1, 1) << " ms\n";
	return 0;
}
