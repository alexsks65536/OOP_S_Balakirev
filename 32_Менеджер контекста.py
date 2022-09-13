fp = None
try:
    with open("myfile.txt") as fp:
        for t in fp:
            print(t)
except Exception as e:
    print(e)