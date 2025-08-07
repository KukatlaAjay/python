dic={"ajay": 45,"sanjay":47,"akash":48,"ajay":30}# not allow duplicated values
print(dic)
dic1={"ajay":45,"cars":["maruthi","benz"],"budget":(1000,2000,1585)}# allow different data types
print(dic1)
# dict constructor
dic2=dict(name="aj",car ="benz",quantity=1)
print(dic2)
#access item
print(dic1["ajay"])
# or use get() method
x=dic1.get("ajay")
print(x)
# keys() method will return set of keys present in the dictionary
y=dic.keys()
print(y)
# or to print values use values()
z=dic.values()# or we can directly excute by print statement
print(z)
dic["year"]=2020 # after inserting new item we sholud again specify key or values method
print(dic.keys())
#item()
print(dic.items())# list with dictionary items
# check if model exsit
if "ajay" in dic:
    print("yes")
# change value
dic1["ajay"]=4453
print(dic1)
# or use update()
dic7={"ajay":52,"jh":55}
print(dic7)
dic7.update({"ajay":9948})
print(dic7)
#add new item
dic["colour"]="red"
print(dic)
# or use updatE()
dic7.update({"color":"red"})
print(dic7)
#pop() method remove the value of specialized key value
dic7.pop("jh")
print(dic7)
dic7.popitem() #popitem() method will change last inseated item
print(dic7)
# del keyword
del dic["akash"]
print(dic)
#clear() this method will empties the dictionary
#dic2.clear()
#print(dic2)
# copy one dictionary to other 
#dic=dic7 #in this case copy is not possible bacause dic is updated with dic7 values and dic values or gone
#print(dic)
#so use copy method
di=dic7.copy()
print(di)
# or dict()
a=dict(dic7)
print(a)
# nested dictionary
family={
    "home1":{"father":"ramaiah","mother":"rama"},
    "childrens":{"son":"ajay","daughter":"amulya"}
}
print(family)
print(family["home1"]["father"])
# or another way
home1={"father":"ramaiah","mother":"rama"},
childrens={"son":"ajay","daughter":"amulya"}
family={"home1":home1,
        "childrens":childrens
        }    
print(family)