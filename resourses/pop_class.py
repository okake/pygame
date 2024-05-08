import numpy as np
import random

class individual:
    def __init__(self,id,genome,pos):
        self.id = id

        self.genome = genome
        #基礎 1~100
        self.hp = genome[0]   #体力
        self.mp = genome[1]   #魔法
        self.str = genome[2]  #攻撃力 
        self.dif = genome[3]  #防御力
        self.agi = genome[4]  #素早さ
        
        #ライフサイクル
        self.mtb = genome[5]  #代謝　高いほど単位時間当たりに消費するエネルギーが多く、体力の回復も早い、寿命は短くなる 100stp~10000stp
        self.fert = genome[6] #繁殖力 繁殖はライフステップの50%経過後から始める　繁殖可能な時期の何割で繁殖するかを決定する　0.1~0.5

        #行動アルゴ関係
        self.prey = genome[7] #攻撃性　高いほど他の生物を食べてエネルギーを採る傾向にある -1~1連続値
        self.move = genome[8] #どのくらい動くか 0~1連続値
        
        #性染色体
        self.col_r,self.col_g,self.col_b = genome[9],genome[10],genome[11] #色 0~255
        self.head,self.body,self.leg = genome[12],genome[13],genome[14] #体　いずれはCPPNとかで作って創発させたいけど今はとりあえずこれで　実装は後で
        self.modify = genome[15:] #基礎能力にかかるバイアス 0.9~1.1

        self.x,self.y = pos #初期配置

    def next_move(self,sight):
        #状態を入力して行動を出力
        #sight:近傍10マス(マンハッタン)の生物の情報　10*5(基礎ステータス)
        #攻撃性が正で0.5
        #ここやる
        a

class population:
    def __init__(self,childs):
        self.childs = []

    def append_child(self,child):
        self.childs.append(child)


def define_init_genome():
    #新規個体の生成
    res = []
    #基礎
    res.append(random.randint(20,100)) #体力
    for i in range(4):
        res.append(random.randint(1,100)) #その他基礎ステ

    #ライフサイクル
    res.append(random.randint(100,10000)) #代謝
    res.append(random.uniform(0.1,0.5)) #繁殖力

    #行動アルゴ
    res.append(random.uniform(-1.0,1.0))
    res.append(random.random())

    #性染色体
    for i in range(3):res.append(random.randint(0,255)) #color
    for i in range(3):res.append(random.random()) #形態　今はダミー
    for i in range(5):res.append(random.random()) #バイアス

    pos = (random.randint(0,1200),random.randint(0,800))

    return res,pos