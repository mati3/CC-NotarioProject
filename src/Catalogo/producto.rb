
class Producto
		
	def initialize(identificador, precio, peso, volumen, descripcion)
		@identificador = identificador
		@precio = precio
		@peso = peso
		@volumen = volumen
		@descripcion = descripcion
	end
	
	public

	def setIdentificador(i)
		@identificador = i
	end

	def getIdentificador()
		return @identificador
	end
	
	def setPrecio(n)
		@precio = n
	end
	
	def getPrecio()
		return @precio
	end

	def setPeso(p)
		@peso = p
	end

	def getPeso()
		return @peso
	end
		
	def setVolumen(volumen)
		@volumen = volumen
	end

	def getVolumen()
		return @volumen
	end

	def setDescripcion(descripcion)
		@descripcion = descripcion
	end

	def getDescripcion()
		return @descripcion
	end
		


	def to_s
		cadena = " Producto: Identificador: #{ @identificador}
		precio: #{@precio}
		Peso : #{@peso}
		Volumen : #{@volumen}
		Descripcion : #{@descripcion}"
		return cadena
	end
	
	def to_s_json
		{"identificador" => @identificador,
		"precio" => @precio ,
		"peso" => @peso,
		"volumen" => @volumen,
		"descripcion" => @descripcion}.to_json
	end
end


