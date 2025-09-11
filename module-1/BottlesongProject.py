def countdown(bottles):

    # Loop while more than 1 bottle remains

    while bottles > 1:

        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")

        print(f"Take one down and pass it around, {bottles - 1} {'bottle' if bottles - 1 == 1 else 'bottles'} of beer on the wall.\n")

        bottles -= 1
        
    # Handle the last bottle

    if bottles == 1:

        print("1 bottle of beer on the wall, 1 bottle of beer.")

        print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        
def main():

    # Ask the user

    bottles = int(input("How many bottles of beer are on the wall? "))

    countdown(bottles)

    print("Time to buy more beer!")
    
if __name__ == "__main__":

    main()