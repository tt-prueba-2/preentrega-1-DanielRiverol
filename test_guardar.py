import app  # Asegúrate de que este sea el nombre del archivo que contiene tu código
from unittest.mock import patch

@patch('builtins.input', side_effect=["1", "Manzana", "10", "3"])  # Simulamos la secuencia de inputs
def test_agregar_producto(mock_input, capfd):
    app.productos = []  # Reseteamos la lista de productos
    app.main()  # Llamamos a la función principal
    captured = capfd.readouterr()  # Capturamos la salida del programa
    assert "Producto agregado con éxito." in captured.out  # Verificamos que el producto se agregó correctamente
    assert len(app.productos) == 1  # Verificamos que se haya agregado el producto
    assert app.productos[0] == ["Manzana", 10]  # Verificamos que los datos sean correctos
