import abc # abstract base classes
import random
# python3 allows unicode as variable name

def myrandom():
    # return float(input())
    return random.random()
class 武將:
    def __init__(self, 名字 = "無名"):
        self.名字 = 名字
        self.中毒 = 0
        self.混亂 = False
        self.龍膽 = False
        self.兵力 = 999999
        self.最大兵力 = 999999
        self.士氣 = 0
        self.兵種 = None
        self.戰法 = None
        self.傷害 = 0
        self.戰法傷害比例 = 1.0
    def 重置(self):
        self.中毒 = 0
        self.混亂 = False
        self.龍膽 = False
        self.士氣 = self.初始士氣()
        self.兵力 = self.最大兵力
    def 初始士氣(self):
        if self.戰法:
            return self.戰法.初始士氣()
        return 0
    def 全滅(self):
        return self.兵力 == 0
    def 行動(self, 回合, 位置, 我方部隊, 敵方部隊):
        if self.中毒 > 0:
            損失兵力 = int(self.兵力 * 0.15)
            my_print(self.名字 + " 中毒損失兵力: " + str(損失兵力))
            self.兵力 -= 損失兵力
        if self.混亂:
            self.混亂 = False
            my_print(self.名字 + " 解除混亂")
            return
        if self.戰法:
            if isinstance(self.戰法, 無限戰法) or self.士氣 >= 100:
                self.戰法.發動(回合, 位置, 我方部隊, 敵方部隊)
            else:
                self.普通攻擊(回合, 位置, 我方部隊, 敵方部隊)
        else:
            self.兵種.行動(回合, 位置, 我方部隊, 敵方部隊)
    def 戰法單體攻擊(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動戰法 " + self.戰法.__class__.__name__)
        列 = 位置 % 3
        目標 = 敵方部隊.選取目標(列)
        if myrandom() < self.暴擊率():
            # 必中
            my_print("暴擊!")
            傷害 = int(self.傷害計算(目標, 回合) * 公式.暴擊加成())
            目標.遭受攻擊(傷害)
        else:
            if myrandom() < 目標.閃避率():
                my_print(目標.名字 + " 閃避!")
                目標.龍膽 = False
            else:
                傷害 = self.傷害計算(目標, 回合)
                目標.遭受攻擊(傷害)
    def 戰法每列攻擊(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動戰法 " + self.戰法.__class__.__name__)
        列 = 位置 % 3
        目標群 = 敵方部隊.選取每列目標(列)
        if myrandom() < self.暴擊率():
            # 必中
            my_print("暴擊!")
            for 目標 in 目標群:
                傷害 = int(self.傷害計算(目標, 回合) * 公式.暴擊加成())
                目標.遭受攻擊(傷害)
        else:
            if myrandom() < 目標群[0].閃避率():
                my_print(目標群[0].名字 + " 閃避!")
                目標群[0].龍膽 = False
            else:
                for 目標 in 目標群:
                    傷害 = self.傷害計算(目標, 回合)
                    目標.遭受攻擊(傷害)
    def 戰法單體回復(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動戰法 " + self.戰法.__class__.__name__)
        列 = 位置 % 3
        目標 = 敵方部隊.選取目標(列)
        if myrandom() < self.暴擊率():
            # 必中
            my_print("暴擊!")
            傷害 = self.傷害計算(目標, 回合) * 目標.防禦加成() * 公式.暴擊加成()
            self.回復(傷害)
        else:
            if myrandom() < 目標.閃避率():
                my_print(目標.名字 + " 閃避!")
                目標.龍膽 = False
            else:
                傷害 = self.傷害計算(目標, 回合)
                self.回復(傷害)
    def 戰法直列攻擊(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動戰法 " + self.戰法.__class__.__name__)
        列 = 位置 % 3
        目標群 = 敵方部隊.選取列目標(列)
        if myrandom() < self.暴擊率():
            # 必中
            my_print("暴擊!")
            for 目標 in 目標群:
                傷害 = int(self.傷害計算(目標, 回合) * 公式.暴擊加成())
                目標.遭受攻擊(傷害)
            if myrandom() < self.混亂率():
                目標群[-1].遭受混亂()
        else:
            if myrandom() < 目標群[0].閃避率():
                my_print(目標群[0].名字 + " 閃避!")
                目標群[0].龍膽 = False
            else:
                for 目標 in 目標群:
                    傷害 = self.傷害計算(目標, 回合)
                    目標.遭受攻擊(傷害)
                if myrandom() < self.混亂率():
                    目標群[-1].遭受混亂()
    def 戰法單體攻擊x2(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動戰法 " + self.戰法.__class__.__name__)
        列 = 位置 % 3
        目標 = 敵方部隊.選取目標(列)
        if myrandom() < self.暴擊率():
            # 必中
            my_print("暴擊!")
            傷害 = int(self.傷害計算(目標, 回合) * 公式.暴擊加成())
            目標.遭受攻擊(傷害)
            傷害 = int(self.傷害計算(目標, 回合) * 公式.暴擊加成())
            目標.遭受攻擊(傷害)
        else:
            if myrandom() < 目標.閃避率():
                my_print(目標.名字 + " 閃避!")
                目標.龍膽 = False
            else:
                傷害 = self.傷害計算(目標, 回合)
                目標.遭受攻擊(傷害)
                傷害 = self.傷害計算(目標, 回合)
                目標.遭受攻擊(傷害)
    def 策略單體攻擊(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動策略")
        列 = 位置 % 3
        目標 = 敵方部隊.選取目標(列)
        if rmyrandom() < self.命中率():
            傷害 = self.策略傷害計算(目標, 回合)
            目標.遭受攻擊(傷害)
        else:
            my_print("失敗! " + 目標.名字 + " 毫髮無傷")
    def 策略直列攻擊(self, 回合, 位置, 敵方部隊):
        my_print(self.名字 + " 發動策略")
        列 = 位置 % 3
        目標群 = 敵方部隊.選取列目標(列)
        for 目標 in 目標群:
            if myrandom() < self.命中率():
                傷害 = self.策略傷害計算(目標, 回合)
                目標.遭受攻擊(傷害)
            else:
                my_print("失敗! " + 目標.名字 + " 毫髮無傷")
    def 設定戰法(self, 戰法名稱):
        self.戰法 = 戰法.create(戰法名稱)
        self.戰法.武將 = self
    def 設定兵種(self, 兵種名稱):
        self.兵種 = 兵種.create(兵種名稱)
        self.兵種.武將 = self
        if isinstance(self.兵種, 戰法將):
            self.設定戰法(self.兵種.戰法.__class__.__name__)
    def 設定兵力(self, 兵力):
        self.最大兵力 = 兵力
    def 設定戰法(self, 戰法名稱):
        self.戰法 = 戰法.create(戰法名稱)
        self.戰法.武將 = self
    def 設定傷害(self, 傷害):
        self.傷害 = 傷害
    def 設定戰法傷害比例(self, 戰法傷害比例):
        self.戰法傷害比例 = 戰法傷害比例
    def 遭受攻擊(self, 傷害):
        損失兵力 = min(傷害, self.兵力)
        self.兵力 -= 損失兵力
        my_print(self.名字 + "遭受攻擊損失" + str(損失兵力) + "兵力")
    def 回復(self, 傷害):
        回復兵力 = min(傷害, self.最大兵力 - self.兵力)
        self.兵力 += 回復兵力
        my_print(self.名字 + "接受回復增加" + str(回復兵力) + "兵力")
    def 遭受混亂(self):
        self.混亂 = True
        my_print(self.名字 + " 混亂!")
    def 命中率(self):
        return self.兵種.命中率()
    def 抵擋率(self):
        return self.兵種.抵擋率()
    def 暴擊率(self):
        return self.兵種.暴擊率()
    def 閃避率(self):
        if self.龍膽:
            return 0.2 + self.兵種.閃避率()
        else:
            return self.兵種.閃避率()
    def 混亂率(self):
        if self.戰法:
            return self.戰法.混亂率()
        return self.兵種.混亂率()
    def 防禦加成(self):
        return self.兵種.防禦加成()
    def 策略防禦加成(self):
        return self.兵種.策略防禦加成()
    def 基本傷害計算(self, 守方, 回合):
        傷害 = self.傷害
        傷害 *= self.兵種.傷害加成(守方.兵種)
        傷害 *= 公式.回合係數(回合)
        if isinstance(self.兵種, 戰法將):
            傷害 *= (1 + self.戰法傷害比例 * (公式.士氣攻擊加成(self.士氣) - 1))
        傷害 *= 公式.士氣防禦加成(守方.士氣)
        if self.龍膽:
            傷害 *= 公式.暴擊加成()
        傷害 *= 公式.浮動係數()
        return 傷害
    def 傷害計算(self, 守方, 回合):
        return int(self.基本傷害計算(守方, 回合) * 守方.防禦加成())
    def 策略傷害計算(self, 守方, 回合):
        return int(self.基本傷害計算(守方, 回合) * 守方.策略防禦加成())
class NPC(武將):
    def __init__(self, 兵種名稱):
        super().__init__(兵種名稱)
        self.設定兵種(兵種名稱)
class 兵種:
    def __init__(self):
        self.武將 = None
        self.戰法 = None
    def create(兵種名稱):
        if 兵種名稱 == "破甲重弩":
            return 破甲重弩()
        elif 兵種名稱 == "天機策士":
            return 天機策士()
        elif 兵種名稱 == "霸王近衛軍":
            return 霸王近衛軍()
        elif 兵種名稱 == "雲翎戰車":
            return 雲翎戰車()
        elif 兵種名稱 == "荊楚鐵衛":
            return 荊楚鐵衛()
        elif 兵種名稱 == "無雙飛騎":
            return 無雙飛騎()
        elif 兵種名稱 == "鬼謀策士":
            return 鬼謀策士()
        elif 兵種名稱 == "凌雲飛矛":
            return 凌雲飛矛()
        elif 兵種名稱 == "雙戟鐵衛":
            return 雙戟鐵衛()
        elif 兵種名稱 == "冀州驍騎":
            return 冀州驍騎()
        elif 兵種名稱 == "破陣俠士":
            return 破陣俠士()
        elif 兵種名稱 == "錦帆驚瀾衝":
            return 錦帆驚瀾衝()
        elif 兵種名稱 == "白馬義從":
            return 白馬義從()
        elif 兵種名稱 == "火靈策士":
            return 火靈策士()
        elif 兵種名稱 == "浮屠戰車":
            return 浮屠戰車()
        elif 兵種名稱 == "虎癡軍":
            return 虎癡軍()
        elif 兵種名稱 == "神電策士":
            return 神電策士()
        elif 兵種名稱 == "號天神騎":
            return 號天神騎()
        elif 兵種名稱 == "咆天虎衛":
            return 咆天虎衛()
        elif 兵種名稱 == "破軍神弩":
            return 破軍神弩()
    def 命中率(self):
        return 1
    def 抵擋率(self):
        return 0
    def 暴擊率(self):
        return 0
    def 閃避率(self):
        return 0
    def 混亂率(self):
        return 0
    def 傷害加成(self, 兵種):
        return 1
    def 防禦加成(self):
        return 1
    def 策略防禦加成(self):
        return 1

class 戰法將(兵種):
    pass
class 步兵(戰法將):
    def 抵擋率(self):
        return 0.2
class 弓兵(戰法將):
    def 暴擊率(self):
        return 0.2
class 騎兵(戰法將):
    def 閃避率(self):
        return 0.2
class 機械(兵種):
    pass
class 策士(兵種):
    @abc.abstractmethod
    def 行動(self, 回合, 位置, 我方部隊, 敵方部隊):
        pass
class 破甲重弩(弓兵):
    def __init__(self):
        self.戰法 = 決勝千里()

class 天機策士(策士):
    pass

class 霸王近衛軍(步兵):
    def __init__(self):
        self.戰法 = 霸王無雙()
    def 暴擊率(self):
        return 0.1
class 雲翎戰車(機械):
    pass

class 荊楚鐵衛(步兵):
    def __init__(self):
        self.戰法 = 恣意攻擊()
    def 暴擊率(self):
        return 0.1
    def 閃避率(self):
        return 0.1
class 無雙飛騎(騎兵):
    def __init__(self):
        self.戰法 = 縱橫無雙()
    def 傷害加成(self, 兵種):
        if isinstance(兵種, 策士):
            return 1.5
        return 1

class 鬼謀策士(策士):
    def 命中率(self):
        return 0.8
    def 行動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.策略直列攻擊(回合, 位置, 敵方部隊)
    def 傷害加成(self, 兵種):
        if isinstance(兵種, 步兵):
            return 1.5
        return 1
class 雙戟鐵衛(步兵):
    def __init__(self):
        self.戰法 = 金剛神力()
    def 防禦加成(self):
        return 0.55
    def 策略防禦加成():
        return 0.55
class 凌雲飛矛(弓兵):
    def __init__(self):
        self.戰法 = 戰鬥咆哮()
    def 暴擊率(self):
        return 0.3

class 冀州驍騎(騎兵):
    def __init__(self):
        self.戰法 = 直搗黃龍()
    def 傷害加成(self, 兵種):
        if isinstance(兵種, 弓兵):
            return 0.5
        elif isinstance(兵種, 步兵):
            return 1.5
        return 1

class 破陣俠士(策士):
    pass

class 錦帆驚瀾衝(機械):
    pass

class 白馬義從(騎兵):
    def __init__(self):
        self.戰法 = 龍膽震天()
    def 傷害加成(self, 兵種):
        if isinstance(兵種, 騎兵):
            return 1.5
        return 1
class 虎癡軍(步兵):
    def __init__(self):
        self.戰法 = 赤膊狂擊()
    def 暴擊率(self):
        return 0.1
    def 傷害加成(self, 兵種):
        if isinstance(兵種, 弓兵):
            return 1.5
        return 1
class 火靈策士(策士):
    pass

class 浮屠戰車(機械):
    pass

class 神電策士(策士):
    pass

class 咆天虎衛(步兵):
    def __init__(self):
        self.戰法 = 震天咆哮()
    def 暴擊率(self):
        return 0.1

class 破軍神弩(弓兵):
    def __init__(self):
        self.戰法 = 亂箭穿心()

class 號天神騎(騎兵):
    def __init__(self):
        self.戰法 = 號令天下()

class 戰法:
    def create(戰法名稱):
        if 戰法名稱 == "決勝千里":
            return 決勝千里()
        elif 戰法名稱 == "霸王無雙":
            return 霸王無雙()
        elif 戰法名稱 == "恣意攻擊":
            return 恣意攻擊()
        elif 戰法名稱 == "縱橫無雙":
            return 縱橫無雙()
        elif 戰法名稱 == "戰鬥咆哮":
            return 戰鬥咆哮()
        elif 戰法名稱 == "金剛神力":
            return 金剛神力()
        elif 戰法名稱 == "直搗黃龍":
            return 直搗黃龍()
        elif 戰法名稱 == "龍膽震天":
            return 龍膽震天()
        elif 戰法名稱 == "赤膊狂擊":
            return 赤膊狂擊()
        elif 戰法名稱 == "亂箭穿心":
            return 亂箭穿心()
        elif 戰法名稱 == "震天咆哮":
            return 震天咆哮()
        elif 戰法名稱 == "號令天下":
            return 號令天下()
    @abc.abstractmethod
    def 發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        assert False, "abstract method: " + self.武將.名字
    @abc.abstractmethod
    def 初始士氣(self):
        return 0
    def 混亂率(self):
        return 0
class 無限戰法(戰法):
    def 發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.無限發動(回合, 位置, 我方部隊, 敵方部隊)
        self.恢復士氣(回合)
    @abc.abstractmethod
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        assert False, "abstract method: " + self.武將.名字
    def 恢復士氣(self, 回合):
        self.武將.士氣 = 100
    def 初始士氣(self):
        return 100

class 決勝千里(無限戰法):
    pass
class 霸王無雙(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法單體攻擊x2(回合, 位置, 敵方部隊)
class 恣意攻擊(無限戰法):
    pass
class 縱橫無雙(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法每列攻擊(回合, 位置, 敵方部隊)
class 戰鬥咆哮(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法單體攻擊(回合, 位置, 敵方部隊)
    def 恢復士氣(self, 回合):
        self.武將.士氣 = max(100, 200 - 100 * (回合 - 1))
    def 初始士氣(self):
        return 300
class 金剛神力(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法單體回復(回合, 位置, 敵方部隊)
class 直搗黃龍(無限戰法):
    pass
class 龍膽震天(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法單體攻擊(回合, 位置, 敵方部隊)
        self.武將.龍膽 = not self.武將.龍膽
class 赤膊狂擊(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法單體攻擊(回合, 位置, 敵方部隊)
    def 恢復士氣(self, 回合):
        self.武將.士氣 = min(100 * (回合 + 1), 500)
class 亂箭穿心(無限戰法):
    pass
class 震天咆哮(無限戰法):
    def 無限發動(self, 回合, 位置, 我方部隊, 敵方部隊):
        self.武將.戰法直列攻擊(回合, 位置, 敵方部隊)
    def 混亂率(self):
        return 0.2
class 號令天下(無限戰法):
    pass

# ref http://forum.gamer.com.tw/C.php?bsn=18446&snA=20110
class 公式:
    def 浮動係數():
        return 0.95 + 0.1 * myrandom()
    def 殘兵係數(損失兵力, 最大兵力):
        return 1 - 損失兵力 / 2.0 / 最大兵力
    def 暴擊加成():
        return 1.3
    def 士氣攻擊加成(士氣):
        return 1 + 0.007 * (士氣 - 100)
    def 士氣防禦加成(士氣):
        return 1 / (1 + 0.002 * 士氣)
    def 回合係數(回合):
        coeff = [
            1.000, 1.012, 1.035, 1.060, 1.076,
            1.100, 1.134, 1.170, 1.211, 1.251,
            1.303, 1.351, 1.408, 1.468, 1.524,
            1.595, 1.662, 1.723, 1.800, 1.800 ]
        return coeff[回合 - 1]

class 陣型:
    def __init__(self):
        self.武將 = [None]*5
        self.順位 = 0
    @abc.abstractmethod
    def 位置(self, 順位):
        assert False, "abstract method"
    def create(陣型名稱):
        if 陣型名稱 == "魚鱗陣":
            return 魚鱗陣()
        elif 陣型名稱 == "長蛇陣":
            return 長蛇陣()
        elif 陣型名稱 == "鋒矢陣":
            return 鋒矢陣()
        elif 陣型名稱 == "偃月陣":
            return 偃月陣()
        elif 陣型名稱 == "錐型陣":
            return 錐型陣()
        elif 陣型名稱 == "八卦陣":
            return 八卦陣()
        elif 陣型名稱 == "七星陣":
            return 七星陣()
        elif 陣型名稱 == "雁型陣":
            return 雁型陣()
    def 上陣(self, 順位, 武將):
        self.武將[順位] = 武將
    def 重置(self):
        for 武將 in self.武將:
            武將.重置()
    def 回合初始(self):
        self.順位 = 0
    def 已完成(self):
        return self.順位 >= 5
    def 順位武將(self):
        while self.順位 < 5:
            武將 = self.武將[self.順位]
            位置 = self.位置(self.順位)
            self.順位 += 1
            if not 武將.全滅():
                return 武將, 位置
        return (None, None)
    def 全滅(self):
        for 順位 in range(5):
            if not self.武將[順位].全滅():
                return False
        return True
    def 選取目標(self, 列):
        if 列 == 0:
            優先序 = [0,3,6,1,4,7,2,5,8]
        elif 列 == 1:
            優先序 = [1,4,7,0,3,6,2,5,8]
        elif 列 == 2:
            優先序 = [2,5,8,1,4,7,0,3,6]
        for 序 in 優先序:
            for 順位 in range(5):
                武將 = self.武將[順位]
                if 武將.全滅():
                    continue
                if self.位置(順位) == 序:
                    return 武將
        assert False, "not found in selecting target"
    def 選取列目標(self, 列):
        if 列 == 0:
            優先序 = [0,3,6,1,4,7,2,5,8]
        elif 列 == 1:
            優先序 = [1,4,7,0,3,6,2,5,8]
        elif 列 == 2:
            優先序 = [2,5,8,1,4,7,0,3,6]
        目標群 = []
        目標列 = -1
        for 序 in 優先序:
            for 順位 in range(5):
                武將 = self.武將[順位]
                if 武將.全滅():
                    continue
                位置 = self.位置(順位)
                if 位置 == 序:
                    if len(目標群) == 0:
                        目標群.append(武將)
                        目標列 = 位置 % 3
                    elif 目標列 == 序 % 3:
                        目標群.append(武將)
        return 目標群
    def 選取每列目標(self, 列):
        目標群 = [None, None, None]
        if 列 == 0:
            優先序 = [0,3,6,1,4,7,2,5,8]
        elif 列 == 1:
            優先序 = [1,4,7,0,3,6,2,5,8]
        elif 列 == 2:
            優先序 = [2,5,8,1,4,7,0,3,6]
        目標群 = []
        目標列 = [False, False, False]
        for 序 in 優先序:
            for 順位 in range(5):
                武將 = self.武將[順位]
                if 武將.全滅():
                    continue
                位置 = self.位置(順位)
                if 位置 == 序:
                    if not 目標列[序%3]:
                        目標群.append(武將)
                        目標列[序%3] = True
        return 目標群
class 魚鱗陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 1
        elif 順位 == 1:
            return 3
        elif 順位 == 2:
            return 4
        elif 順位 == 3:
            return 5
        elif 順位 == 4:
            return 7
class 長蛇陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 0
        elif 順位 == 1:
            return 3
        elif 順位 == 2:
            return 4
        elif 順位 == 3:
            return 7
        elif 順位 == 4:
            return 8
class 鋒矢陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 0
        elif 順位 == 1:
            return 1
        elif 順位 == 2:
            return 2
        elif 順位 == 3:
            return 4
        elif 順位 == 4:
            return 7
class 偃月陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 1
        elif 順位 == 1:
            return 2
        elif 順位 == 2:
            return 3
        elif 順位 == 3:
            return 5
        elif 順位 == 4:
            return 6
class 錐型陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 1
        elif 順位 == 1:
            return 3
        elif 順位 == 2:
            return 5
        elif 順位 == 3:
            return 6
        elif 順位 == 4:
            return 8
class 八卦陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 0
        elif 順位 == 1:
            return 3
        elif 順位 == 2:
            return 4
        elif 順位 == 3:
            return 5
        elif 順位 == 4:
            return 8
class 七星陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 0
        elif 順位 == 1:
            return 2
        elif 順位 == 2:
            return 4
        elif 順位 == 3:
            return 6
        elif 順位 == 4:
            return 8
class 雁型陣(陣型):
    def 位置(self, 順位):
        if 順位 == 0:
            return 0
        elif 順位 == 1:
            return 2
        elif 順位 == 2:
            return 3
        elif 順位 == 3:
            return 5
        elif 順位 == 4:
            return 7

class 部隊:
    def __init__(self, 陣型名稱, 武將們):
        self.陣型 = 陣型.create(陣型名稱)
        for 順位 in range(5):
            self.陣型.上陣(順位, 武將們[順位])
    def 重置(self):
        self.陣型.重置()
    def 回合初始(self, 回合):
        self.回合 = 回合
        self.陣型.回合初始()
    def 已完成(self):
        return self.陣型.已完成()
    def 行動(self, 對方部隊):
        武將, 位置 = self.陣型.順位武將()
        if 武將 != None:
            武將.行動(self.回合, 位置, self, 對方部隊)
    def 全滅(self):
        return self.陣型.全滅()
    def 選取目標(self, 列):
        return self.陣型.選取目標(列)
    def 選取列目標(self, 列):
        return self.陣型.選取列目標(列)
    def 選取每列目標(self, 列):
        return self.陣型.選取每列目標(列)

_verbose = True
def my_print(str):
    global _verbose
    if _verbose:
        print(str)

"""
return value: 0: tie; 1: win; 2: lose
"""
def 戰鬥模擬(我方部隊, 敵方部隊):
    我方部隊.重置()
    敵方部隊.重置()
    for 回合 in range(1, 21):
        my_print("第%d回合" % 回合)
        我方部隊.回合初始(回合)
        敵方部隊.回合初始(回合)
        while not 我方部隊.已完成() and not 敵方部隊.已完成():
            我方部隊.行動(敵方部隊)
            if 我方部隊.全滅():
                return -1
            if 敵方部隊.全滅():
                return 1
            敵方部隊.行動(我方部隊)
            if 我方部隊.全滅():
                return -1
            if 敵方部隊.全滅():
                return 1
    my_print("平局")
    return 0

class 設定值:
    我方兵力 = 205000
    敵方兵力 = 193370

def main():
    武將們 = ["韓信", "張良", "項羽", "劉邦", "關羽", "呂布", "郭嘉", "太史慈", "典韋", "文醜", "徐庶", "甘寧", "趙雲", "周瑜", "張遼", "許褚", "司馬懿", "黃忠", "張飛", "諸葛亮", "曹操"]
    武將列表 = {}
    for 武將名字 in 武將們:
        武將列表[武將名字] = 武將(武將名字)
    趙雲 = 武將列表["趙雲"]
    太史慈 = 武將列表["太史慈"]
    典韋 = 武將列表["典韋"]
    項羽 = 武將列表["項羽"]
    許褚 = 武將列表["許褚"]
    張飛 = 武將列表["張飛"]

    太史慈.設定兵種("凌雲飛矛")
    太史慈.設定傷害(70000)
    太史慈.設定戰法傷害比例(0.6)
    趙雲.設定兵種("白馬義從")
    趙雲.設定傷害(65000)
    典韋.設定兵種("雙戟鐵衛")
    典韋.設定傷害(70000)
    項羽.設定兵種("霸王近衛軍")
    項羽.設定傷害(50000)
    許褚.設定兵種("虎癡軍")
    許褚.設定傷害(67000)
    張飛.設定兵種("咆天虎衛")
    張飛.設定傷害(55000)
    我方出戰武將 = [太史慈, 趙雲, 張飛, 許褚, 典韋]
    for 所有武將 in 我方出戰武將:
        所有武將.設定兵力(設定值.我方兵力)

    鬼謀策士 = NPC("鬼謀策士")
    鬼謀策士.設定傷害(50000)
    霸王近衛軍 = NPC("霸王近衛軍")
    霸王近衛軍.設定傷害(50000)
    霸王近衛軍.設定戰法傷害比例(0.4)
    白馬義從 = NPC("白馬義從")
    白馬義從.設定傷害(66000)
    凌雲飛矛 = NPC("凌雲飛矛")
    凌雲飛矛.設定傷害(50000)
    無雙飛騎 = NPC("無雙飛騎")
    無雙飛騎.設定傷害(50000)
    敵方出戰武將 = [鬼謀策士, 霸王近衛軍, 白馬義從, 凌雲飛矛, 無雙飛騎]
    for 所有敵將 in 敵方出戰武將:
        所有敵將.設定兵力(設定值.敵方兵力)

    我方 = 部隊("雁型陣", 我方出戰武將)
    敵方 = 部隊("七星陣", 敵方出戰武將)
    戰鬥模擬(我方, 敵方)
    return
    win = 0
    lose = 0
    global _verbose
    _verbose = False
    for i in range(100):
        result = 戰鬥模擬(我方, 敵方)
        if result > 0:
            win += 1
        elif result < 0:
            lose += 1
    print (win, lose)
if __name__ == '__main__':
    main()