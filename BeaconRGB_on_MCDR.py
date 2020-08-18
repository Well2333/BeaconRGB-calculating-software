#coding=UTF-8
#auther by Well404

#MCD (From Fallen_Breath)
def onServerInfo(server, info):
	if info.isPlayer == 1:
		work(server, info)

#MCDR (From Fallen_Breath)
def on_info(server, info):
    if info.is_player:
        global player
        player = info.player
        work(server, info)

#HelpMsg
Helpmsg_BCRGB="""-----信标RGB辅助软件------
!!BCRGB #****** 输入16进制RGB数据
    例如!!BCRGB #39C5BB
!!BCRGB *** *** *** 输入10进制RGB数据
    例如!!BCRGB 57 197 187
!!BCRGB help 调出此信息
-----信标RGB辅助软件------"""

def work(server, info):
    if info.is_player:
        if info.content.startswith('!!BCRGB '):
            if info.content.startswith("!!BCRGB help"):
                server.tell(player,Helpmsg_BCRGB)
            else:
                raw_RGB = info.content[8:]
                if "#" in raw_RGB:
                    R = int(raw_RGB[1:3], 16)
                    G = int(raw_RGB[3:5], 16)
                    B = int(raw_RGB[5:7], 16)
                    server.tell(player,"此16进制RGB对应的10进制RGB为：{0} {1} {2}".format(R, G, B))
                else:
                    R, G, B = raw_RGB.split()
                    server.tell(player,"此10进制RGB对应的16进制RGB为：#{0}{1}{2}".format(hex(int(R)).replace("0x", ""),
                                                                       hex(int(G)).replace("0x", ""),
                                                                       hex(int(B)).replace("0x", "")))
                R0b = '{:0>8d}'.format(int('{:b}'.format(int(R))))
                G0b = '{:0>8d}'.format(int('{:b}'.format(int(G))))
                B0b = '{:0>8d}'.format(int('{:b}'.format(int(B))))

                Rlist = []
                Glist = []
                Blist = []
                for x in R0b:
                    Rlist.append(str(x))
                for x in G0b:
                    Glist.append(str(x))
                for x in B0b:
                    Blist.append(str(x))

                def col(n):
                    if Rlist[n] == "1":
                        if Glist[n] == "1":
                            if Blist[n] == "1":
                                return "白色"
                            else:
                                return "黄色"
                        else:
                            if Blist[n] == "1":
                                return "品红色"
                            else:
                                return "红色"
                    else:
                        if Glist[n] == "1":
                            if Blist[n] == "1":
                                return "青色"
                            else:
                                return "绿色"
                        else:
                            if Blist[n] == "1":
                                return "蓝色"
                            else:
                                return "黑色"

                server.tell(player,
                            "从上至下的排列方式为{0},{1},{2},{3},{4},{5},{6},{7},白色".format(col(0), col(1), col(2), col(3),
                                                                                  col(4),
                                                                                  col(5),
                                                                                  col(6), col(7)))
                server.tell(player, "以下列表适配于自动换色信标机，其中0为关，1为开，请根据信标机的使用说明进行具体操作")
                server.tell(player, "红色由上至下的开关情况为{0}".format(Rlist))
                server.tell(player, "绿色由上至下的开关情况为{0}".format(Glist))
                server.tell(player, "蓝色由上至下的开关情况为{0}".format(Blist))