
class Catalogo
		
	attr_accessor :arrayProductos

	def initialize()
		file = File.read('src/ejemploCatalogo.json')
    		data_hash2 = JSON.parse(file)
    		@productos = []
    		i=0
    		data_hash2.each do |value|
    			@productos[i] = Producto.new(value['identificador'], value['precio'], value['peso'], value['volumen'], value['descripcion'])
    			i=i+1
   
    		@arrayProductos = @productos
	end
	
	public

	def to_s
		cadena = "\n Todos los Productos:\n"
		@arrayProductos.each do |j|
			cadena += " #{j.to_s}\n"
		end
		return cadena
	end
	
end


