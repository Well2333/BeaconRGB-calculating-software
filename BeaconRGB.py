Rlist=[]
Glist=[]
Blist=[]
raw_RGB=input("请输入10进制的RGB值，中间用空格分割，或16进制的RGB值，用#开头且不需要空格:")
if "#" in raw_RGB:
    R=int(raw_RGB[1:3],16)
    G=int(raw_RGB[3:5],16)
    B=int(raw_RGB[5:7],16)
    print("此16进制RGB对应的10进制RGB为：{0} {1} {2}".format(R,G,B))
else:
    R,G,B=raw_RGB.split()
    print("此10进制RGB对应的16进制RGB为：#{0}{1}{2}".format(hex(int(R)).replace("0x",""),hex(int(G)).replace("0x",""),hex(int(B)).replace("0x","")))
R0b='{:0>8d}'.format(int('{:b}'.format(int(R))))
G0b='{:0>8d}'.format(int('{:b}'.format(int(G))))
B0b='{:0>8d}'.format(int('{:b}'.format(int(B))))
for x in R0b:
    Rlist.append(str(x))
for x in G0b:
    Glist.append(str(x))
for x in B0b:
    Blist.append(str(x))

def col(n):
    if Rlist[n]=="1":
        if Glist[n]=="1":
            if Blist[n]=="1":
                return "白色"
            else:
                return "黄色"
        else:
            if Blist[n]=="1":
                return "品红色"
            else:
                return "红色"
    else:
        if Glist[n]=="1":
            if Blist[n]=="1":
                return "青色"
            else:
                return "绿色"
        else:
            if Blist[n]=="1":
                return "蓝色"
            else:
                return "黑色"

print("从上至下的排列方式为{0},{1},{2},{3},{4},{5},{6},{7},白色".format(col(0),col(1),col(2),col(3),col(4),col(5),col(6),col(7)))
print("以下列表适配于自动RGB信标机，其中0为关，1为开，请根据信标机的使用说明进行具体操作")
print("红色由上至下的开关情况为",Rlist)
print("绿色由上至下的开关情况为",Glist)
print("蓝色由上至下的开关情况为",Blist)
input("按任意键以退出")
                
