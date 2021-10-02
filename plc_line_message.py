from mc_protocol_comm import*
#from ip_input import*
from python_line_message import*
import socket
import time
import  requests


#ｺﾏﾝﾄﾞ生成
mc_prt = mc_protocol_set('dm','r','w',1,1)
#メソッドを実行
mshed = mc_prt.mc_prtcl_setup()
#戻り値を表示
print('mshed:'+mshed)

mcdev = mc_prt.mc_prtcl_dev()
#戻り値を表示
print('mcdev:'+mcdev)

mcrw = mc_prt.mc_prtcl_rw()
#戻り値を表示
print('mcrw:'+mcrw)

mcbw = mc_prt.mc_prtcl_bw()
#戻り値を表示
print('mcbw:'+mcbw)

mcadd = mc_prt.mc_prtcl_add()
#戻り値を表示
print('mcadd:'+mcadd)

mcdata_q = mc_prt.mc_prtcl_data_q()
#戻り値を表示
print('mcdata_q:'+mcdata_q)

mcadd_q = mc_prt.mc_prtcl_add_q()
#戻り値を表示
print('mcadd_q:'+mcadd_q)


#mc_pro = icf+rsv+gct+dna+da1+da2+sna+sa1+sa2+sid+cm1+cm2+tx1+tx2+tx3+tx4+tx5+tx6#+tx7+tx8
mc_pro = mshed + mcdata_q + '0020' + mcrw + mcbw + mcdev + mcadd + mcadd_q
mc_pro = mc_pro.encode('ASCII')
print(mc_pro)

#================================================================
#プログラムの開始
#================================================================               
#インスタンス化
#i1 = plc_ip_no1()
#i2 = plc_ip_no2()
#i3 = plc_ip_no3()
#i4 = plc_ip_no4()

#p = plc_port_no()

#ip設定
#host1 = i1.plc_ip1()
#host2 = i2.plc_ip2()
#host3 = i3.plc_ip3()
#host4 = i4.plc_ip4()
#ip設定
host1 = "192"
host2 = "168"
host3 = "50"
host4 = "10"


host = host1 + "." + host2 + "." + host3 + "." + host4
port = 5000


while True:
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#tx = plc_device_choice()
#入力したＩＰとPORTで通信が確立したかをチェック。 
        client.connect((host, port))    
        client.send(mc_pro)
        print("通信開始...")
        break
    except socket.error as e:
      print("通信エラー")
      time.sleep(5)

#print ("Default socket timeout: %s" % client.gettimeout())
client.settimeout(60)
print ("socket timeout:",client.gettimeout())      
resp = client.recv(2048)


print('receive')
print(resp) 
print(type(resp))
resp_decode = resp.decode('utf-8')
print(resp_decode)
print(type(resp_decode))

client.close() 


print(resp_decode[-4:])


line = line_notify()

line.line_messeage(resp_decode[-4:])
