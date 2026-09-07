# Name : Rudresh Kumbhare
# PRN : 125B1B213
# Batch : D1

import numpy as np

def inputMatrix(rows=3, cols=3, name="Matrix"):
    print(f"Enter elements of {name}")
    matrix = []

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(int(input(f"Enter element [{i+1}][{j+1}]: ")))
        matrix.append(row)

    return np.array(matrix)

def add(arr1, arr2):
  return arr1 + arr2

def subtract(arr1, arr2):
  return arr1 - arr2

def multiply(arr1, arr2):
  return arr1 @ arr2

def divide(arr1, arr2):
  if np.any(arr2) == 0:
    return "Cannot divide by zero."

  return np.divide(arr1, arr2)

def dotProduct(arr1, arr2):
  return np.dot(arr1, arr2)

def sqrt(arr):
  return np.sqrt(arr)

def matrixOperation(choice, arr1, arr2=None):
  switcher = {
      'add':add,
      'subtract':subtract,
      'multiply':multiply,
      'divide':divide,
      'dot':dotProduct,
      'sqrt':sqrt
  }

  func = switcher.get(choice)
  if choice == 'sqrt':
    return func(arr1)
  elif func and arr2 is not None:
    return func(arr1, arr2)
  else:
    return "Invalid input.\n"

M1 = inputMatrix(name="Matrix 1")
print("\nM1:\n", M1, "\n")

M2 = inputMatrix(name="Matrix 2")
print("\nM2:\n", M2, "\n")

print("Addition: \n", matrixOperation('add', M1, M2), "\n")
print("Subtraction: \n", matrixOperation('subtract', M1, M2), "\n")
print("Multiplication: \n", matrixOperation('multiply', M1, M2), "\n")
print("Division: \n", matrixOperation('divide', M1, M2), "\n")
print("Dot product: \n", matrixOperation('dot', M1, M2), "\n")
print("Square root of Matrix 1: \n", matrixOperation('sqrt', M1), "\n")
print("Square root of Matrix 2: \n", matrixOperation('sqrt', M2), "\n")
