import typer 

def main(first:int, second:int, name:str):
    print(f'{name}, {first} * {second} = {first*second}')

if __name__ == '__main__': 
    typer.run(main)
