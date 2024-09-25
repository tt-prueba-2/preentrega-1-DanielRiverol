import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

# Test para mostrar productos cuando no hay productos
@patch('builtins.input', side_effect=["2", "3"])  # Simulamos la opción de mostrar productos y luego salir
def test_mostrar_productos_sin_productos(mock_input, capfd):
    app.productos = []  # Aseguramos que la lista esté vacía
    app.main()  # Ejecutamos el programa
    captured = capfd.readouterr()  # Capturamos la salida del programa
    assert "No hay productos registrados." in captured.out  # Verificamos que se muestre el mensaje correcto

