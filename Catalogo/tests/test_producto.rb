
require_relative  '../src/producto'
require  'test/unit'
require 'rack/test'
require 'simplecov'
SimpleCov.start

require 'codecov'
SimpleCov.formatter = SimpleCov::Formatter::Codecov

class TestMyProducto <  Test::Unit::TestCase
	include Rack::Test::Methods

	
	def test_producto()
		@producto = Producto.new("00101","20","2 kg", "20,20,50","Botella de ron")
		assert @producto.getIdentificador == "00101", " Identificador erroneo"
		assert @producto.getPrecio == "20", "El precio no es correcto"
		assert @producto.getPeso == "2 kg", " Peso erroneo "
		assert @producto.getVolumen == "20,20,50", " Volumen erroneo"
		assert @producto.getDescripcion == "Botella de ron", "El nombre no es correcto"
	end

	def app
	    app = lambda { |env| [200, {'Content-Type' => 'application/json'}, ['All responses are OK']] }
	    builder = Rack::Builder.new
	    builder.run app
	end

	def test_app_hola
	    get '/'

	    assert last_response.ok?
	    assert_equal last_response.body, 'All responses are OK'
	end

	def test_app_id
	    get '/producto/:id'

	    assert last_response.ok?
	    assert_equal last_response.body, 'All responses are OK'
	end

	def test_app_todos
	    get '/todos'

	    assert last_response.ok?
	    assert_equal last_response.body, 'All responses are OK'
	end
	
end
