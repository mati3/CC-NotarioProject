
require_relative  'src/catalogo'
require  'sinatra'

	set :port, 8181

	before do
		@catalogo = Catalogo.new()
	end

	get '/' do
		'hola mundo'
	end

	get '/todos' do
		#@catalogo.to_s
		@catalogo.to_s_json
	end

	get '/producto/:id' do |n|
		@catalogo.getProdID(n)
	end
