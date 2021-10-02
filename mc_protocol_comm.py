# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:22:36 2020

@author: kmiss
"""


class mc_protocol_set:
    
    def __init__(self,plc_d,rw,bw,add,add_q):   # インスタンス生成時に自動的に呼ばれるメソッド
        
        self.plc_rw = rw        #r:読出　w:書込
        self.plc_bw = bw        #b:bit　w:word
        self.plc_dev = plc_d    #ﾃﾞﾊﾞｲｽ
        self.plc_add = add      #先頭ｱﾄﾞﾚｽ        
        self.plc_add_q = add_q    #ﾃﾞﾊﾞｲｽ点数
        self.plc_data_q = add_q    #要求ﾃﾞｰﾀ長

        print(self.plc_rw)
        print(self.plc_bw)
        print(self.plc_dev)
        print(self.plc_add)
        print(self.plc_add_q)

#ヘッダーからリクエストユニット局番までの伝文用意
    def mc_prtcl_setup(self):

        hed = '5000'       #ヘッダ
        net = '00'         #ネットワーク番号        
        pcn = 'FF'         #pc番号
        rqun = '03FF'      #リクエストユニットIO番号
        rqst = '00'        #リクエストユニット局番号
        """
        #rdtl   =   '0000'      #リクエストデータ長
        self.cput = '0020'      #CPU監視タイマ
        com     =   '\x04'  #ｺﾏﾝﾄﾞ
        com2　= b'\x01'#ｺﾏﾝﾄﾞ2
        scom1 = b'\x00'#ｻﾌﾞｺﾏﾝﾄﾞ1
        scom2　= b'\x00'#ｻﾌﾞｺﾏﾝﾄﾞ2
        """
        mcst = hed + net + pcn + rqun + rqst
        return mcst #ヘッダーからリクエストユニット局番号まで返す。

#デバイス   
    def mc_prtcl_dev(self):
        
        if self.plc_dev == 'r':
            dev = 'X*'      #ﾃﾞﾊﾞｲｽ指定R

        elif self.plc_dev == 'b':
            dev = 'B*'      #ﾃﾞﾊﾞｲｽ指定B

        elif self.plc_dev == 'mr':
            dev = 'M*'      #ﾃﾞﾊﾞｲｽ指定MR
        
        elif self.plc_dev == 'lr':
            dev = 'L*'      #ﾃﾞﾊﾞｲｽ指定LR

        elif self.plc_dev == 'cr':
            dev = 'SM'      #ﾃﾞﾊﾞｲｽ指定CR

        elif self.plc_dev == 'cm':
            dev = 'SD'      #ﾃﾞﾊﾞｲｽ指定CM
    
        elif self.plc_dev == 'dm' or 'em':
            dev = 'D*'      #ﾃﾞﾊﾞｲｽ指定DM EM

        elif self.plc_dev == 'fm':
            dev = 'R*'      #ﾃﾞﾊﾞｲｽ指定FM

        elif self.plc_dev == 'zf':
            dev = 'ZR'      #ﾃﾞﾊﾞｲｽ指定ZF

        elif self.plc_dev == 'w':
            dev = 'W*'      #ﾃﾞﾊﾞｲｽ指定W

        elif self.plc_dev == 'tn':
            dev = 'TN'      #ﾃﾞﾊﾞｲｽ指定T現在値
        
        elif self.plc_dev == 'ts':
            dev = 'TS'      #ﾃﾞﾊﾞｲｽ指定T接点

        elif self.plc_dev == 'cn':
            dev = 'CN'      #ﾃﾞﾊﾞｲｽ指定C現在値
        
        elif self.plc_dev == 'cs':
            dev = 'CS'      #ﾃﾞﾊﾞｲｽ指定C接点

        else:
            dev = 'NG'

        return dev

#読出・書込
    def mc_prtcl_rw(self):

        if self.plc_rw == 'r':
            com = '0401'      #読出

        elif self.plc_rw == 'w':
            com = '1401'      #書込

        else:
            com = 'NG'

        return com


#ビットorワード
    def mc_prtcl_bw(self):

        if self.plc_bw == 'b':
            scm = '0001'      #ビット

        elif self.plc_bw == 'w':
            scm = '0000'      #

        else:
            scm = 'NG'

        return scm
        

#先頭デバイス
    def mc_prtcl_add(self):

        add_a = self.plc_add
        add_b = format(add_a,'06x')

        
        return add_b


#ﾃﾞﾊﾞｲｽ点数
    def mc_prtcl_add_q(self):
               
        addl_a = self.plc_add_q
        addl = format(addl_a,'04x')
           
        return addl



#要求データ長
    def mc_prtcl_data_q(self):
               
        if self.plc_rw == 'r':
            datal_a = 24
            datal = format(datal_a,'04x')
           
        elif self.plc_rw == 'w':
            
            if self.plc_bw == 'b':
                datal_a = 24
                datal_b = self.plc_data_q 
                datal_c = datal_b + datal_a        
                addl = format(datal_c,'04x')

            elif self.plc_bw == 'w':
                datal_a = 24
                datal_b = self.plc_data_q * 4
                datal_c = datal_b + datal_a        
                datal = format(datal_c,'04x')
            else:
                datal = 'NG'    
            
        else:
            datal = 'NG'   

        return datal        
        








#==========================================================================
#プログラムの実行ブロック
#==========================================================================        
if __name__ == '__main__':
    
    
    
    #オブジェクト生成
    mc_prt = mc_protocol_set('mr','r','w',1,5)
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

    mcadd_q = mc_prt.mc_prtcl_add_q()
    #戻り値を表示
    print(mcadd_q)

    mcdata_q = mc_prt.mc_prtcl_data_q()
    #戻り値を表示
    print(mcdata_q)

