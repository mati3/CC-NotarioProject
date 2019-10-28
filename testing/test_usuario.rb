
require_relative  'src/Usuarios/usuario'
require  'test/unit'
#require  "json"

class TestMyUsuario <  Test::Unit::TestCase

#	def setup 
#		file = File.read('src/Usuarios/ejemploUsuario.json')
#		data_hash = JSON.parse(file)
#		
#		@usuario = usuario.new(data_hash['Identificador'], data_hash['Nombre'], data_hash['Correo'], data_hash['Direccion envio'], data_hash['Metodo pago'])
#	end
	
	def test_usuario()
		@usuario = usuario.new("00001","Matilde","mati331@correo.ugr.es", "Daniel Saucedo","Al contado")
		assert @usuario.getIdentificador == "00001", " Identificador erroneo"
		assert @usuario.getNombre == "Matilde", "El nombre no es correcto"
		assert @usuario.getCorreo == "mati331@correo.ugr.es", " Correo erroneo "
		assert @usuario.getDireccion == "Daniel Saucedo", " Direccion erronea"
		assert @usuario.getPago == "Al contado", "El metodo de pago no es correcto"
	end
	
end
