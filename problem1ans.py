import math

def calculate_circle_area(radius):
  """Calculates the area of a circle given its radius.

  Args:
      radius: The radius of the circle.

  Returns:
      The area of the circle with four decimal places of precision.
  """

  pi = math.pi  # Use the built-in constant pi for accuracy
  area = pi * radius * radius
  return f"A={area:.4f}"  # Format output with A= and 4 decimal places

def main():
  """Prompts user for radius and prints the area."""

  try:
    radius = float(input("Enter the radius of the circle: "))
    if radius <= 0:
      raise ValueError("Radius must be a positive number.")
    area_result = calculate_circle_area(radius)
    print(area_result)
  except ValueError as e:
    print(f"Error: {e}")

if __name__ == "__main__":
  main()
