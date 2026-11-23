import typer 
import rich

def main(first:int, second:int, name:str = 'Reuven'):
    rich.print(f'{name}, {first} * {second} = {first*second} :smile:')

if __name__ == '__main__': 
    typer.run(main)
