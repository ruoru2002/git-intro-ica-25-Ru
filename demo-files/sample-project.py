#!/usr/bin/env python3
"""
Sample Project for Git Practice

This is a simple Python script that students can use to practice
Git operations like committing, branching, and merging.
"""

import random
import time


class Calculator:
    """A simple calculator class for demonstration purposes."""
    
    def __init__(self):
        self.history = []
    
    def add(self, a, b):
        """Add two numbers."""
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def subtract(self, a, b):
        """Subtract two numbers."""
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result
    
    def multiply(self, a, b):
        """Multiply two numbers."""
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result
    
    def divide(self, a, b):
        """Divide two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """Get calculation history."""
        return self.history


def main():
    """Main function to demonstrate the calculator."""
    print("Welcome to the Git Practice Calculator!")
    print("=" * 40)
    
    calc = Calculator()
    
    # Demonstrate some calculations
    print("Performing some calculations...")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"15 / 3 = {calc.divide(15, 3)}")
    
    print("\nCalculation History:")
    for entry in calc.get_history():
        print(f"  {entry}")
    
    print("\nGit Practice Tips:")
    print("- Try modifying this file and committing changes")
    print("- Create a new branch and add a new method")
    print("- Merge your changes back to main")
    print("- Practice resolving conflicts with classmates")


if __name__ == "__main__":
    main() 