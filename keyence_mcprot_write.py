from mc_protocol_comm import*
from ip_input import*
import socket
import time


class mc_protocol_write:

    def __init__(self,plc_d,rw,bw,add,add_q):   # インスタンス生成時に自動的に呼ばれるメソッド


    #ｺﾏﾝﾄﾞ生成
        mc_prt = mc_protocol_set('dm','w','w',1,1)

    #メソッドを実行
        mshed = mc_prt.mc_prtcl_setup()
    #戻り値を表示
        print(mshed)

        mcdev = mc_prt.mc_prtcl_dev()
    #戻り値を表示
        print(mcdev)

        mcrw = mc_prt.mc_prtcl_rw()
    #戻り値を表示
        print(mcrw)

        mcbw = mc_prt.mc_prtcl_bw()
    #戻り値を表示
        print(mcbw)

        mcadd = mc_prt.mc_prtcl_add()
    #戻り値を表示
        print(mcadd)

mcdata_q = mc_prt.mc_prtcl_data_q()
#戻り値を表示
print(mcdata_q)

mcadd_q = mc_prt.mc_prtcl_add_q()
#戻り値を表示
print(mcadd_q)

mcdata_q = mc_prt.mc_prtcl_data_q()
#戻り値を表示
print(mcdata_q)

mc_pro = mshed + mcdata_q + '0020' + mcrw + mcbw + mcdev + mcadd + mcadd_q + '0002'
mc_pro = mc_pro.encode('ASCII')
print(mc_pro)

#================================================================
#プログラムの開始
#================================================================               
#インスタンス化
i1 = plc_ip_no1()
i2 = plc_ip_no2()
i3 = plc_ip_no3()
i4 = plc_ip_no4()

p = plc_port_no()

#ip設定
host1 = i1.plc_ip1()
host2 = i2.plc_ip2()
host3 = i3.plc_ip3()
host4 = i4.plc_ip4()

host = host1 + "." + host2 + "." + host3 + "." + host4
port = int(p.plc_port())


while True:
    
    except socket.error as e:
      print("通信エラー")
      time.sleep(1)

#print ("Default socket timeout: %s" % client.gettimeout())
client.settimeout(60)
print ("socket timeout:",client.gettimeout())      
resp = client.recv(2048)
"""
i = 0     
 
if Ture == resp: 

    while i <= 10 :
    
        time.sleep(1)
        if i <10 :
    #通信開通ﾁｪｯｸ
            if sid == resp[9] and b'x00' == resp[12] and  b'x00' == resp[13]:
                print("通信OK")
                break
            else:
                print("通信NG")
                client.close()
                break
            i = i+1
else:
    print("通信NG")
    client.close()
 """   
    
    
#print("****************************************")
#print(" デバイスを指定してください。")
#print(" cio dm wr hr")
#print("****************************************")




print('receive')


print(resp) 

client.close() 