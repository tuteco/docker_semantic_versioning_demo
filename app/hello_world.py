from time import sleep

# the program will print hello world
#  every 3 second unitl you terminate it
print("every three seconds, 3,2,1,.... ")

n = 1

while True:
    print(f"Hello, {n}. World ")

    n += 1

    sleep(3)