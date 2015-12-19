# python3 allows unicode as variable name
class 武將:
    def __init__(self, 名字, 兵種名稱):
        self.名字 = 名字
        self.兵種 = 兵種.create(兵種名稱)

class 兵種:
    def create(兵種名稱):
        if 兵種名稱 == "荊楚鐵衛":
            return 荊楚鐵衛()
        elif 兵種名稱 == "霸王近衛軍":
            return 霸王近衛軍()
        elif 兵種名稱 == "雙戟鐵衛":
            return 雙戟鐵衛()

class 步兵(兵種):
    pass

class 弓兵(兵種):
    pass

class 騎兵(兵種):
    pass

class 機械(兵種):
    pass

class 策士(兵種):
    pass

class 荊楚鐵衛(步兵):
    def __init__(self):
        self.戰法 = 恣意攻擊(self)

class 霸王近衛軍(步兵):
    def __init__(self):
        self.戰法 = 霸王無雙(self)

class 雙戟鐵衛(步兵):
    def __init__(self):
        self.戰法 = 金剛神力(self)

class 戰法:
    def __init__(self, 施展武將):
        self.施展武將 = 施展武將

class 霸王無雙(戰法):
    def __init__(self, 施展武將):
        super().__init__(施展武將)

class 恣意攻擊(戰法):
    def __init__(self, 施展武將):
        super().__init__(施展武將)

class 金剛神力(戰法):
    def __init__(self, 施展武將):
        super().__init__(施展武將)

class 陣型:
    pass

class 長蛇陣(陣型):
    pass

def main():
    武將列表 = {
        "關羽" : 武將("關羽", "荊楚鐵衛"),
        "項羽" : 武將("項羽", "霸王近衛軍"),
        "典韋" : 武將("典韋", "雙戟鐵衛"),
    }
    敵將列表 = []
    for (name, general) in 武將列表.items():
        print(name, general.兵種.__class__.__name__)

if __name__ == '__main__':
    main()