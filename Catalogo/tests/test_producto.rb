
require_relative  '../src/producto'
require  'test/unit'
#require  "json"

class TestMyProducto <  Test::Unit::TestCase

#	def setup 
#		file = File.read('src/Catalogo/ejemploProducto.json')
#		data_hash = JSON.parse(file)
#		
#		@producto = Producto.new(data_hash['Identificador'], data_hash['Precio'], data_hash['Peso'], data_hash['Volumen'], data_hash['Descripcion'])
#	end
	
	def test_producto()
		@producto = Producto.new("00101","20","2 kg", "20,20,50","Botella de ron")
		assert @producto.getIdentificador == "00101", " Identificador erroneo"
		assert @producto.getPrecio == "20", "El precio no es correcto"
		assert @producto.getPeso == "2 kg", " Peso erroneo "
		assert @producto.getVolumen == "20,20,50", " Volumen erroneo"
		assert @producto.getDescripcion == "Botella de ron", "El nombre no es correcto"
	end
	
end
