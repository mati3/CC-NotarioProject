require_relative  'src/catalogo'
require  'sinatra'
require 'json'

class App < Sinatra::Base

	before do
		@catalogo = Catalogo.new()
	end

	get '/' do
		content_type :json
		{:status => 'hola mundo'}.to_json
	end

	get '/todos' do
		content_type :json
		@catalogo.to_s_json
	end

	get '/producto/:id' do |n|
		content_type :json
		@catalogo.getProdID(n)
	end
end
