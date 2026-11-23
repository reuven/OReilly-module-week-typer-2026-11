import typer 

def main(favorite_number:int):
    print(f'Your favorite number is {favorite_number}? Great, one less than that is {favorite_number - 1}')

if __name__ == '__main__': 
    typer.run(main)
