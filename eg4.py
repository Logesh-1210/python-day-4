## Type casting : 

## If any data type can be changed into String . 
## but any String cant be changed into another data type .

x = "12"
y = 1234
z = 9.9
v = int(x)

print(type(x))
print(type(y))
print(type(z))
print(type(v))
print(v+y )

## splitting concept . 

food = "Briyani , of Elegant : Famous for Thalapakatti ,  Proud of Dindugal."

values = food.split(":")[1].split(",")[0].strip()
print(values)

## spot the coupon code in the given string and the offer will be apllied on the further exquistion. 

college = "Mahendra Institute of Technology , Mahendrapuri , Namakkal  District ."
if "Mahendra" in college :
    print("Your Future will not in our hands.")
else:
    print("You have the better Future for your self")

## Finding the index position in the given string :

college = "Mahendra Institute of Technology is also affliated to the Anna University of Madras."

def tnea():
    print("The task to be Finding of the position in the given String is to be founded by the : " , college.find("Anna"))
tnea()

## finding of the initials in the two given seperate string :

name = "logesh manickam"

modified = "".join([word[0].title() for word in name.split()])

print(modified)

## Removing of the Extra Space in the given string :

college = "       Mahendra Institute of Technology    "
print(college.strip())


## findig the word position value not the index value of the variable :

name_department = "logesh manickam from the Electronics and communication engineering in mahendra institute of technology ."
position = len(name_department.split())
print(position)

