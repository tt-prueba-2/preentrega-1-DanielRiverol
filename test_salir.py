import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

@patch('builtins.input', side_effect=["3"])  # Simulamos la opción de salida
def test_salir(mock_input, capfd):
    app.main()  # Ejecutamos el programa
    captured = capfd.readouterr()  # Capturamos la salida del programa
    assert "Saliendo del sistema de inventario..." in captured.out  # Verificamos que se imprime el mensaje de salida


