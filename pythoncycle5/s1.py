f=open("hello.txt","r")
content=f.readlines()
print("file content is",content)
x=['haiiii']
x.append(content)
print("after appand line is",x)