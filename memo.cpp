#include <iostream>
#include <unordered_map>
#include <vector>

// recursive solution with O(2^n)
int fib(int n){
    if (n < 1) throw 2;

    if (n == 1 || n == 2) return 1;

    return fib(n - 1) + fib(n - 2);

}

// memoization
long long fib_m(int n, std::unordered_map<int, long long>& memo = {}){
    if (n <= 2) return 1;

    if (memo.find(n) != memo.end()) return memo[n];

    memo[n] = fib_m(n - 1, memo) + fib_m(n - 2, memo);
    return memo[n];
}

int main(){
    int number;
    std::cout << "Enter number: ";
    std::cin >> number;

    std::unordered_map<int, long long> memo;
    std::cout << "Fibonacci of " << number << " = " << fib_m(number, memo) << std::endl;
}