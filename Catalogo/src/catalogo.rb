require_relative 'producto'

class Catalogo
		
	attr_accessor :arrayProductos

	def initialize()
		file = File.read('./src/ejemploCatalogo.json')
    		data_hash2 = JSON.parse(file)
    		@productos = []
    		i=0
    		data_hash2.each do |value|
    			@productos[i] = Producto.new(value['Identificador'], value['Precio'], value['Peso'], value['Volumen'], value['Descripcion'])
    			i=i+1
   		end
    		@arrayProductos = @productos
	end
	
	public

	def getProdID(id)
		prod = nil
		@arrayProductos.each do |j|
			if j.getIdentificador == id then
				prod = j
				break j
			end
		end
		return prod.to_s_json
	end



	def to_s
		cadena = "\n Todos los Productos:\n"
		@arrayProductos.each do |j|
			cadena += " #{j.to_s}\n"
		end
		return cadena
	end

	def to_s_json
		cadena = "\n [ "
		@arrayProductos.each do |j|
			cadena += "\n #{j.to_s_json}" + ","
		end
		cadena = cadena.slice(1..cadena.length - 2)
		#cadena = cadena.substring(0, cadena.length - 1)
		cadena += "\n ] \n"
		return cadena
	end

end


