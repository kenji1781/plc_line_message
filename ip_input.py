# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 22:04:27 2019

@author: kmiss
"""
#ＩＰを入力
class plc_ip_no1():
    
    def plc_ip1(self):
        
        x1 = input("IP1を入力してください。例:192\n")
    
        return x1
    
class plc_ip_no2():
    
    def plc_ip2(self):
        
        x2 = input("IP2を入力してください。例:168\n")
    
        return x2    
    
class plc_ip_no3():
    
    def plc_ip3(self):
        
        x3 = input("IP3を入力してください。例:250\n")
    
        return x3    
    
class plc_ip_no4():
    
    def plc_ip4(self):
        
        x4 = input("IP4を入力してください。例:1\n")
    
        return x4    
    
    
    
    

#PORT№を入力
class plc_port_no():
    
    def plc_port(self):
        
        y = input("port№を入力してください。\n")
        
        return y

#==========================================================================
#プログラムの実行ブロック
#==========================================================================        
if __name__ == '__main__':
    
    ip_x1 = plc_ip_no1()
    ipx1 = ip_x1.plc_ip1()
    print(ipx1)

    ip_x2 = plc_ip_no1()
    ipx2 = ip_x2.plc_ip2()
    print(ipx2)

    ip_x3 = plc_ip_no3()
    ipx3 = ip_x3.plc_ip3()
    print(ipx3)

    ip_x4 = plc_ip_no4()
    ipx4 = ip_x4.plc_ip4()
    print(ipx4)





    
    port_x = plc_port_no()
    portx = port_x.plc_port()        
    print(portx)    