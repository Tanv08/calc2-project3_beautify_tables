"""Testing Multiplication"""
from calc.calculations.multiplication import Multiplication

def test_calculation_multiplication():
    """testing that our calculator has a static method for multiplication"""
    #Arrange
    mynumbers = (2.0,1.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 2.0
    #Arrange
    mynumbers = (4.0,2.0)
    multiplication = Multiplication(mynumbers)
    #Act
    #Assert
    assert multiplication.get_result() == 8.0
