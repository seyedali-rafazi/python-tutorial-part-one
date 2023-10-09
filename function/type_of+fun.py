def greeting(first_name):
    print(f"hi {first_name}")

def get_greeting(first_name):
    return f"hi {first_name}"

file = open("content.txt" , "w")
file.write(get_greeting(input("Say your name: ")))