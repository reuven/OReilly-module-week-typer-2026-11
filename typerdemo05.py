import typer 
import rich

def main(first:int, second:int, name:str = 'Reuven', use_emoji:bool=True):
    if use_emoji:
        rich.print(f'{name}, {first} * {second} = {first*second} :smile:')
    else:
        rich.print(f'{name}, {first} * {second} = {first*second}')

if __name__ == '__main__': 
    typer.run(main)
