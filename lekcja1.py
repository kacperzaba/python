# f = open("logh.txt", "w")
# with open("logh.txt") as f:
#     if 2 > 3:
#         f.write("Yes")
#     else:
#         x = "111"
        
#         f.write("Woops! I have deleted the content!")
#         f.close()
#         print(f.read(int(x)))

#     lines = f.readlines()

# f = open("text.txt", "w")
# with open('text.txt') as f:
#     text = f.read()

with open("demofile0.txt", "w") as f:
    f = open("demofile2.txt", "a")
    f.write("Now the file has more content!")
    f.close()

#open and read the file after the appending:
    # f = open("demofile2.txt", "r")
    # print(f.read()) 