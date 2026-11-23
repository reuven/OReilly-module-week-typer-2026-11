import typer 

def main(name:str):
    print(f'Hello, {name}!')

if __name__ == '__main__':   # only run code below here if the file is being run directly -- if it's imported, ignore this stuff
    typer.run(main)
