require 'simplecov'
SimpleCov.start do
  track_files "test_producto.rb"
end

require 'codecov'
SimpleCov.formatter = SimpleCov::Formatter::Codecov

class TestMyProducto <  Test::Unit::TestCase

end
