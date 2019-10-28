
class Usuario
		
	def initialize(identificador, nombre, correo, direccion, pago)
		@identificador = identificador
		@nombre = nombre
		@correo = correo
		@direccion = direccion
		@pago = pago
	end
	
	public

	def setIdentificador(i)
		@identificador = i
	end

	def getIdentificador()
		return @identificador
	end
	
	def setNombre(n)
		@nombre = n
	end
	
	def getNombre()
		return @nombre
	end

	def setCorreo(p)
		@correo = p
	end

	def getCorreo()
		return @correo
	end
		
	def setDireccion(direccion)
		@direccion = direccion
	end

	def getDireccion()
		return @direccion
	end

	def setPago(pago)
		@pago = pago
	end

	def getPago()
		return @pago
	end
		


	def to_s
		cadena = " Usuario: Identificador: #{ @identificador}
		Nombre: #{@nombre}
		Correo : #{@correo}
		Direccion : #{@direccion}
		Pago : #{@pago}"
		return cadena
	end
	
	def to_s_json
		{"identificador" => @identificador ,
		"nombre" => @nombre,
		"correo" => @correo,
		"direccion" => @direccion
		"pago" => @pago}.to_json
	end
end


