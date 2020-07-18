from PublicReference.base import *

class 混沌魔灵主动技能(主动技能):
    技能施放时间 = 0.0
    脱手 = 1
    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return round((self.攻击次数 * (self.基础 + self.成长 * self.等级) + self.攻击次数2 * (self.基础2 + self.成长2 * self.等级) + self.攻击次数3 * (
                        self.基础3 + self.成长3 * self.等级)) * (1 + self.TP成长 * self.TP等级) * self.倍率,2)

class 混沌魔灵技能0(主动技能):
    名称 = '魔灵召唤：波拉斯'
    备注 = '(20S平均)'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 444.15
    成长 = 13.94
    攻击次数 = 12/4
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能1(主动技能):
    名称 = '魔灵召唤：瓦尔琪'
    备注 = '(20S平均)'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 328.09
    成长 = 14.5
    攻击次数 = 14/7
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能2(被动技能):
    名称 = '魔灵血统'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

class 混沌魔灵技能3(被动技能):
    名称 = '力量法则'
    所在等级 = 20
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['军团列阵','魔幻旋风','毁灭突进','翔空剑','聚灵升空剑','魔神百裂拳','黑暗冲击','午夜嘉年华','绚丽耀光','魔灵乱舞','黑曜之眸：亚丁降临']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.085 + 0.015 * self.等级, 5)


class 混沌魔灵技能4(主动技能):
    名称 = '魔灵召唤：狂暴布洛克'
    备注 = '(20S平均)'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 506.41
    成长 = 22.14
    攻击次数 = 14/5.5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 混沌魔灵技能5(主动技能):
    名称 = '绝对魅力'
    所在等级 = 25
    等级上限 = 20
    基础等级 = 10
    是否有伤害 = 0
    关联技能 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：大画家芭芘','魔灵召唤：旋转小冯','魔灵召唤：小吸血鬼夏伊','魔灵召唤：大富翁鲁邦','魔灵召唤：迪克老爹','魔灵召唤：红心女王艾丽莎']
    关联技能2 = ['魔灵炸弹','碎灵屠戮']
    关联技能3 = ['毁灭突进']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.012 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.035 + 0.012 * self.等级, 5)
    
    def 加成倍率3(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(0.668*(1.35 + 0.012* self.等级), 5)



class 混沌魔灵技能6(主动技能):
    名称 = '魔灵召唤：假面杰森'
    备注 = '(20S平均)'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 800.21
    成长 = 34.68
    攻击次数 = 8/7
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能7(主动技能):
    名称 = '魔灵召唤：大画家芭芘'
    备注 = '(20S平均)'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 435.41
    成长 = 18.88
    攻击次数 = 14/5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能8(主动技能):
    名称 = '魔灵召唤：旋转小冯'
    备注 = '(20S平均)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 1444.80
    成长 = 61.64
    攻击次数 = 73/90
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 混沌魔灵技能9(主动技能):
    名称 = '魔灵召唤：小吸血鬼夏伊'
    备注 = '(20S平均)'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 711.37
    成长 = 30.36
    攻击次数 = 14/3
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 混沌魔灵技能10(主动技能):
    名称 = '魔灵召唤：大富翁鲁邦'
    备注 = '(20S平均)'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 1024.96
    成长 = 38.23
    攻击次数 = 18/5
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 混沌魔灵技能11(主动技能):
    名称 = '魔灵召唤：迪克老爹'
    备注 = '(20S平均)'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 1179.84
    成长 = 55.34
    攻击次数 = 8/1.8
    CD = 20
    TP成长 = 0.10
    TP上限 = 5



class 混沌魔灵技能12(主动技能):
    名称 = '魔灵召唤：红心女王艾丽莎'
    备注 = '(20S平均)'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 1647.65
    成长 = 76.20
    攻击次数 = 12/1.8
    CD = 20
    TP成长 = 0.10
    TP上限 = 5


class 混沌魔灵技能13(主动技能):
    名称 = '军团列阵'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 31
    基础 = 3365.589353
    成长 = 659.3893343
    CD = 5
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能14(主动技能):
    名称 = '连锁共振'
    所在等级 = 20
    等级上限 = 7
    基础等级 = 1
    是否有伤害 = 0
    关联技能 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：旋转小冯','魔灵召唤：迪克老爹']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.96 + 0.02 * self.等级, 5)

    def 等级加成(self, x):
        if self.等级 != 0:
            if self.等级 + x > self.等级上限:
                self.等级 = self.等级上限
            else:
                self.等级 += x

class 混沌魔灵技能15(主动技能):
    名称 = '魔灵炸弹'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 7337.506597
    成长 = 829.5010758
    CD = 12

class 混沌魔灵技能16(主动技能):
    名称 = '魔幻旋风'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 3911.734436
    成长 = 440.6952313
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能17(主动技能):
    名称 = '毁灭突进'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 6994.958298
    成长 = 692.9359897
    CD = 12
    TP成长 = 0.10
    TP上限 = 5

class 混沌魔灵技能18(主动技能):
    名称 = '翔空剑'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9202.727129
    成长 = 1043.052922
    CD = 15.0
    TP成长 = 0.151969913
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23

class 混沌魔灵技能19(主动技能):
    名称 = '碎灵屠戮'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 41892.21924
    成长 = 4723.637535
    CD = 45.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.25
        self.CD *= 0.9

class 混沌魔灵技能20(主动技能):
    名称 = '聚灵升空剑'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 17011.56017
    成长 = 1920.39105
    CD = 40.0
    TP成长 = 0.12
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23

class 混沌魔灵技能21(被动技能):
    名称 = '魔能榨取'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            if self.等级 <= 16:
                return round(1.015 + 0.015 * self.等级, 5)
            else:
                return round(1.295 + 0.020 * (self.等级 - 16), 5)


class 混沌魔灵技能22(主动技能):
    名称 = '魔神百裂拳'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 39802.11668
    成长 = 12005.31736

    CD = 145
        
class 混沌魔灵技能23(主动技能):
    名称 = '黑暗冲击'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 17250.20664
    成长 = 1958.062756
    CD = 30
    TP成长 = 0.12
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.07

class 混沌魔灵技能24(主动技能):
    名称 = '绚丽耀光'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 16
    基础 = 45840.39485
    成长 = 5176.740704
    CD = 40.0


class 混沌魔灵技能25(被动技能):
    名称 = '亚丁之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11
    关联技能 = ['魔幻旋风','毁灭突进','翔空剑','聚灵升空剑','魔神百裂拳','黑暗冲击','午夜嘉年华','绚丽耀光','魔灵乱舞','黑曜之眸：亚丁降临']
    关联技能2 = ['魔灵召唤：波拉斯','魔灵召唤：瓦尔琪','魔灵召唤：狂暴布洛克','魔灵召唤：假面杰森','魔灵召唤：大画家芭芘','魔灵召唤：旋转小冯','魔灵召唤：小吸血鬼夏伊','魔灵召唤：大富翁鲁邦','魔灵召唤：迪克老爹','魔灵召唤：红心女王艾丽莎']
  
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.28 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.14 + 0.02 * self.等级, 5)


class 混沌魔灵技能26(主动技能):
    名称 = '午夜嘉年华'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 18
    基础 = 30330.11652
    成长 = 3428.96276
    CD = 50.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.23

class 混沌魔灵技能27(主动技能):
    名称 = '魔灵乱舞'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 54106.82012
    成长 = 6109.036658
    CD = 50.0

class 混沌魔灵技能28(主动技能):
    名称 = '黑曜之眸：亚丁降临'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 88031
    成长 = 26517.15652
    CD = 180


class 混沌魔灵技能29(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

class 混沌魔灵技能30(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

class 混沌魔灵技能31(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)


混沌魔灵技能列表 = []
i = 0
while i >= 0:
    try:
        exec('混沌魔灵技能列表.append(混沌魔灵技能' + str(i) + '())')
        i += 1
    except:
        i = -1

混沌魔灵技能序号 = dict()
for i in range(len(混沌魔灵技能列表)):
    混沌魔灵技能序号[混沌魔灵技能列表[i].名称] = i

混沌魔灵技能一觉序号 = 0
混沌魔灵技能二觉序号 = 0
混沌魔灵技能三觉序号 = 0
for i in 混沌魔灵技能列表:
    if i.所在等级 == 50:
        混沌魔灵技能一觉序号 = 混沌魔灵技能序号[i.名称]
    if i.所在等级 == 85:
        混沌魔灵技能二觉序号 = 混沌魔灵技能序号[i.名称]
    if i.所在等级 == 100:
        混沌魔灵技能三觉序号 = 混沌魔灵技能序号[i.名称]

混沌魔灵技能护石选项 = ['无']
for i in 混沌魔灵技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        混沌魔灵技能护石选项.append(i.名称)

混沌魔灵符文选项 = ['无']
for i in 混沌魔灵技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        混沌魔灵符文选项.append(i.名称)


class 混沌魔灵角色属性(角色属性):
    职业名称 = '混沌魔灵'

    武器选项 = ['太刀', '钝器', '巨剑', '短剑']

    # '物理百分比','魔法百分比','物理固伤','魔法固伤'
    伤害类型选择 = ['魔法固伤']

    # 默认
    伤害类型 = '魔法固伤'
    防具类型 = '重甲'
    防具精通属性 = ['智力']

    主BUFF = 2

    # 基础属性(含唤醒)
    基础力量 = 798.0
    基础智力 = 958.0

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0

    def __init__(self):
        self.技能栏 = deepcopy(混沌魔灵技能列表)
        self.技能序号 = deepcopy(混沌魔灵技能序号)


class 混沌魔灵(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 混沌魔灵角色属性()
        self.角色属性A = 混沌魔灵角色属性()
        self.角色属性B = 混沌魔灵角色属性()
        self.一觉序号 = 混沌魔灵技能一觉序号
        self.二觉序号 = 混沌魔灵技能二觉序号
        self.三觉序号 = 混沌魔灵技能三觉序号
        self.护石选项 = deepcopy(混沌魔灵技能护石选项)
        self.符文选项 = deepcopy(混沌魔灵符文选项)