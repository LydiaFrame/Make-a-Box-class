#!/usr/bin/env python3
"""Program to calculate the cost to wrap a present."""

__author__ = "Lydia Frame"
__date__ = "4/27/2025"

from box import Box

def main():
    """Main function to run the wrapping cost calculator."""
    # Prompt user for dimensions
    length = float(input('Length? '))
    print()
    width = float(input('Width? '))
    print()
    height = float(input('Height? '))
    print()

    # Create a Box object
    present = Box(length, width, height)

    # Calculate cost
    surface_area = present.calc_surface_area()
    cost = surface_area * 0.02

    # Print result
    print('Cost for', present, 'is ${0:.2f}'.format(cost))

if __name__ == '__main__':
    main()
