# file handling in python 

#to create the file , even if u use the write thing it will get the created 
f = open("vishwas.txt","x")
f.write(" vishwas is a good boy ")
f.close()
# remember the "w" will overwrite the content in the file

# to add content to the file without overwriting use append "a"
f=open("vishwas.txt","a")
f.write(" i am in the python lab")
f.close()

#this is to read the content in the file 
f=open("vishwas.txt","r")
#to print or display the content 
data=f.read()
print(data)

#if u want the content line by line 
data2=f.readlines()
print(data2)

#the modes are
# w means write 
#x to create 
#r+ is to read and write 
#r is to read 
#a is to append
#a+ is used to append and read 

# with (waht it does is it closes the file automatically and hands eof error )
with open("vishwas.txt","a+") as f:
    f.write("vishwas is the best guy and is using the with ")
    res=f.read()
    print(res)
    
# csv file handling 
import csv

data = [
    ['User', 'Action', 'Points'],
    ['Dude', 'Login', '10'],
    ['Gemini', 'Search', '50'],
    ['Player1', 'Win', '100']
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("--- FILE CONTENT ---")
with open('data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
 
    


