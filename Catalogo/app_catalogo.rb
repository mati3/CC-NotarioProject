require_relative  'src/catalogo'
require  'sinatra'

class App < Sinatra::Base

	before do
		@catalogo = Catalogo.new()
	end

	get '/' do
		'hola mundo'
	end

	get '/todos' do
		@catalogo.to_s_json
	end

	get '/producto/:id' do |n|
		@catalogo.getProdID(n)
	end
end
