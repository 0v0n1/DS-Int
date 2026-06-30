f= open("batch.txt","w")
f.write("Hello")
f.close()

with open("batch.txt","w")as f:
    f.write("Hey \n")
    f.write("my name is avani \n")
    f.write("python is a snake \n")

lis=["Python is the dominant programming language utilized to build modern artificial intelligence (AI) and machine learning solutions.",
     "Its clean and simple syntax allows developers to focus on solving complex AI problems rather than fighting difficult code structures.",
     "The language provides powerful pre-built frameworks like TensorFlow and PyTorch that drastically reduce development time for neural networks.",
     "Developers also use specialized libraries like Pandas and NumPy to easily clean, slice, and process the massive datasets required to train AI models."]
with open("batch.txt", "w") as f:
    f.writelines(line + '\n' for line in lis)
    #f.write('\n'.join(lis))

#with open("batch.txt", "r") as f:
    '''for line in f:
        print (line.strip())'''
    '''content= f.readline()
    print(content)'''

with open("batch.txt", "a") as f:
    f.write("adding new line \n")

with open("batch.txt", "r") as f:
    #f.seek(0)
    f.read(10)
    f.tell()