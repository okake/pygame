import numpy as np

class map:
    def __init__(self,size):
        #2次元情報 map[x][y] = state
        #中身はstate,current value,max value
        #valueは増えてから最大になるまで時間がかかる
        #state -1:何もなし -2:壁 -3:壊せない壁 else:生物id
        self.map = np.zeros((size,size))
        self.current_value = np.zeros((size,size))
        self.max_value = np.zeros((size,size))
        self.size = size
        
        #縁の生成
        for i in range(size):
            self.map[0][i] = -3
            self.map[size-1][i] = -3
            self.map[i][0] = -3
            self.map[i][size-1] = -3

    def apdate_values(self):
        #価値の更新
        #今の価値から2割増やす
        next_value = self.current_value
        pluses = self.max_value*0.2
        next_value += pluses
        for i in range(self.size):
            for j in range(self.size):
                self.current_value[i][j] = min(self.current_value[i][j],next_value[i][j])

    def get_indivisuals(self):
        #個体のidを辞書型でもって座標を返す
        res = {}
        for i in range(self.size):
            for j in range(self.size):
                if self.map[i][j] >= 0:
                    res[self.map[i][j]] = (i,j)
        
        return res