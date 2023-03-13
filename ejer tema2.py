def test_crearpunto():
    # Arrange
    punto = Punto(1, 2, 3)
    # Act
    punto.crear()
    # Assert
    assert punto.id == 1
    assert punto.x == 2
    assert punto.y == 3
    assert punto.z == 4
    