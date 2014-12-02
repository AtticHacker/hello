all: build
build: src/Main.hs
	ghc src/Main.hs -o hello
