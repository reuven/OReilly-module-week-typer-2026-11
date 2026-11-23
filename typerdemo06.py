import typer 
from datetime import datetime

def main(name:str, birthday:datetime):
    print(f'Hello, {name}. You are {datetime.now() - birthday}) old.')

if __name__ == '__main__': 
    typer.run(main)
