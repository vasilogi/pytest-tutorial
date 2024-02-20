import pytest
import src.shapes as shapes
import math

class TestCircle:

    def setup_method(self, method):
        print(f"setting up {method}")
        self.circle = shapes.Circle(radius=10)

    def teardown_method(self, method):
        print(f"tearing down {method}")
    
    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius


    def test_not_same_area_rectangle(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()