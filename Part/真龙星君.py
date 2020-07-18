from PublicReference.base import *


class 真龙星君技能0(被动技能):
    名称 = '基础精通'
    倍率 = 1.0
    所在等级 = 1
    等级上限 = 200
    基础等级 = 100
    关联技能 = ['普通攻击', '空斩打']
    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(self.倍率 * (0.463 + 0.089 * self.等级), 5)

class 真龙星君技能1(主动技能):
    名称 = '普通攻击'
    备注 = '(一轮，TP为基础精通)'
    所在等级 = 1
    等级上限 = 1
    基础等级 = 1
    基础 = 224.69
    成长 = 0
    基础2 = 142.11
    成长2 = 0
    CD = 2.0
    TP成长 = 0.10
    TP上限 = 3

class 真龙星君技能2(主动技能):
    名称 = '空斩打'
    所在等级 = 1
    等级上限 = 20
    基础等级 = 10
    基础 = 84.0
    成长 = 10.5
    CD = 2.0
    TP成长 = 0.08
    TP上限 = 5

class 真龙星君技能3(主动技能):
    名称 = '落凤锤'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1449
    成长 = 168
    CD = 6.0
    TP成长 = 0.08
    TP上限 = 5

class 真龙星君技能4(主动技能):
    名称 = '疾风打'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1449
    成长 = 155
    CD = 4.4
    TP成长 = 0.08
    TP上限 = 5

class 真龙星君技能5(主动技能):
    名称 = '破魔符'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 43
    基础 = 858
    成长 = 96
    CD = 1.7
    TP成长 = 0.10
    TP上限 = 5


class 真龙星君技能6(被动技能):
    名称 = '潜龙'
    所在等级 = 15
    等级上限 = 11
    基础等级 = 1
    关联技能 = ['空斩打']
    关联技能2 = ['断空捶击','无双击']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.38 + 0.02 * self.等级, 5)

    def 加成倍率2(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.27 + 0.03 * self.等级, 5)

class 真龙星君技能7(被动技能):
    名称 = '巨兵精通'
    所在等级 = 20
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

    def 魔法攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.1 + 0.01 * self.等级, 5)

class 真龙星君技能8(主动技能):
    名称 = '断空捶击'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1224
    成长 = 143
    CD = 4.0
    TP成长 = 0.10
    TP上限 = 5


class 真龙星君技能9(主动技能):
    名称 = '升天阵'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1719.6
    成长 = 181.2
    CD = 4.3
    TP成长 = 0.08
    TP上限 = 5


class 真龙星君技能10(主动技能):
    名称 = '黑暗切割'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1962
    成长 = 232
    CD = 5.1
    TP成长 = 0.10
    TP上限 = 5


class 真龙星君技能11(主动技能):
    名称 = '朱雀符'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 2250
    成长 = 270
    CD = 5.6
    TP成长 = 0.10
    TP上限 = 5

class 真龙星君技能12(主动技能):
    名称 = '星落打'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 4196
    成长 = 472
    CD = 10.8
    TP成长 = 0.10
    TP上限 = 5


class 真龙星君技能13(主动技能):
    名称 = '巨旋风'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    近身基础 = 275
    近身成长 = 26
    远程基础 = 181
    远程成长 = 16
    攻击间隔 = 0.3
    持续时间 = 4
    CD = 7.2
    TP成长 = 0.10
    TP上限 = 5

    def 等效百分比(self, 武器类型):
        if self.等级 == 0:
            return 0
        else:
            return (1 + self.TP成长 * self.TP等级) * ((self.近身基础 + self.近身成长 * self.等级) + (int(self.持续时间 / self.攻击间隔)) * (self.远程基础 + self.远程成长 * self.等级))

class 真龙星君技能14(被动技能):
    名称 = '驱魔之书'
    所在等级 = 30
    等级上限 = 40
    基础等级 = 10
    关联技能 = ['真龙焚天','式神封灵阵','逆龙七杀','逆鳞震','灭魂符','苍龙逐日','无双击','式神：殇','疾风旋空破','落雷符','狂乱锤击','疾风打','朱雀符','黑暗切割','升天阵','落凤锤','破魔符']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1 + 0.015 * self.等级, 5)


class 真龙星君技能15(主动技能):
    名称 = '狂乱锤击'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 5715
    成长 = 634
    CD = 12.6
    TP成长 = 0.10
    TP上限 = 5

class 真龙星君技能16(主动技能):
    名称 = '落雷符'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 9056
    成长 = 1000
    CD = 18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1
    护石 = 0

    def 装备护石(self):
        self.倍率 *= 1.15
        self.护石 = 1

class 真龙星君技能17(主动技能):
    名称 = '疾风旋空破'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 596
    成长 = 78
    攻击次数 = 7
    基础2 = 1413
    成长2 = 158
    CD = 18
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.08
        self.攻击次数 += 1
        self.CD *= 0.85

class 真龙星君技能18(主动技能):
    名称 = '式神：殇'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 799
    成长 = 96
    攻击次数 = 15
    基础2 = 3683
    成长2 = 420
    攻击次数2 = 1
    CD = 38.5
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.攻击次数 = 0
        self.基础2 *= 4.79
        self.成长2 *= 4.79
        self.CD *= 0.95

class 真龙星君技能19(主动技能):
    名称 = '无双击'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 10210
    成长 = 1144
    CD = 36
    TP成长 = 0.10
    TP上限 = 5

class 真龙星君技能20(被动技能):
    名称 = '斗志散发'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.01 * self.等级, 5)


class 真龙星君技能21(主动技能):
    名称 = '苍龙逐日'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 31876.9
    成长 = 9169.6
    CD = 145


class 真龙星君技能22(主动技能):
    名称 = '灭魂符'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 12930
    成长 = 1420
    CD = 30.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.26
        self.CD *= 0.90


class 真龙星君技能23(主动技能):
    名称 = '逆鳞震'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 21621
    成长 = 2449
    CD = 40.0
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.20


class 真龙星君技能24(被动技能):
    名称 = '脉轮：式神'
    所在等级 = 75
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.34 + 0.02 * self.等级, 5)

class 真龙星君技能25(被动技能):
    名称 = '式神之力'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.08 + 0.02 * self.等级, 5)

    def 物理攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

    def 魔法攻击力倍率进图(self, 武器类型):
        return self.加成倍率(武器类型)

class 真龙星君技能26(主动技能):
    名称 = '逆龙七杀'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 45599
    成长 = 5149
    CD = 45


class 真龙星君技能27(主动技能):
    名称 = '式神封灵阵'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 43264
    成长 = 4877
    CD = 42.8



class 真龙星君技能28(主动技能):
    名称 = '真龙焚天'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 69915
    成长 = 21139
    攻击次数 = 1
    基础2 = 82892
    成长2 = 25027
    攻击次数2 = 0
    CD = 180.0


class 真龙星君技能29(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)


class 真龙星君技能30(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)


class 真龙星君技能31(被动技能):
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


真龙星君技能列表 = []
i = 0
while i >= 0:
    try:
        exec('真龙星君技能列表.append(真龙星君技能' + str(i) + '())')
        i += 1
    except:
        i = -1

真龙星君技能序号 = dict()
for i in range(len(真龙星君技能列表)):
    真龙星君技能序号[真龙星君技能列表[i].名称] = i

真龙星君一觉序号 = 0
真龙星君二觉序号 = 0
真龙星君三觉序号 = 0
for i in 真龙星君技能列表:
    if i.所在等级 == 50:
        真龙星君一觉序号 = 真龙星君技能序号[i.名称]
    if i.所在等级 == 85:
        真龙星君二觉序号 = 真龙星君技能序号[i.名称]
    if i.所在等级 == 100:
        真龙星君三觉序号 = 真龙星君技能序号[i.名称]

真龙星君护石选项 = ['无']
for i in 真龙星君技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        真龙星君护石选项.append(i.名称)

真龙星君符文选项 = ['无']
for i in 真龙星君技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        真龙星君符文选项.append(i.名称)


class 真龙星君角色属性(角色属性):
    职业名称 = '真龙星君'

    武器选项 = ['念珠', '战斧']


    主BUFF = 1.76

    # 基础属性(含唤醒)
    基础力量 = 906.0
    基础智力 = 904.0

    # 适用系统奶加成
    力量 = 基础力量
    智力 = 基础智力

    防具类型 = '板甲'

    # 人物基础 + 唤醒
    物理攻击力 = 65.0
    魔法攻击力 = 65.0
    独立攻击力 = 1045.0
    火属性强化 = 13
    冰属性强化 = 13
    光属性强化 = 13
    暗属性强化 = 13
    远古记忆 = 0
    反身空斩打 = 0
    力法及精通 = 0

    def __init__(self):
        self.技能栏 = deepcopy(真龙星君技能列表)
        self.技能序号 = deepcopy(真龙星君技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['落雷符']].CD -= self.技能栏[self.技能序号['落雷符']].等级 * 9/140
        if self.技能栏[self.技能序号['落雷符']].护石 == 1:
            self.技能栏[self.技能序号['落雷符']].CD *= 0.85
        if self.技能栏[self.技能序号['潜龙']].等级 != 0:
            self.技能栏[self.技能序号['普通攻击']].基础 += 200
            self.技能栏[self.技能序号['普通攻击']].基础2 *= 1.56 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].近身基础 *= 1.23 + 0.02 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].近身成长 *= 1.23 + 0.02 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].远程基础 *= 1.36 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].远程成长 *= 1.36 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['巨旋风']].持续时间 += 1.3 + 0.05 * self.技能栏[self.技能序号['潜龙']].等级
            self.技能栏[self.技能序号['疾风旋空破']].攻击次数 += 2
        if self.反身空斩打 == 1:
            self.技能栏[self.技能序号['空斩打']].被动倍率 *= (1 + 0.1 * self.技能栏[self.技能序号['普通攻击']].TP等级) * (2.92 + 0.08 * self.技能栏[self.技能序号['潜龙']].等级)
        else:
            self.技能栏[self.技能序号['空斩打']].被动倍率 *= (1 + 0.1 * self.技能栏[self.技能序号['普通攻击']].TP等级) * (1.96 + 0.04 * self.技能栏[self.技能序号['潜龙']].等级)
        if self.力法及精通 == 0 or self.力法及精通 == 1:
            self.技能栏[self.技能序号['真龙焚天']].攻击次数 = 0
            self.技能栏[self.技能序号['真龙焚天']].攻击次数2 = 1
            self.技能栏[self.技能序号['无双击']].被动倍率 *= 1.2

class 真龙星君(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 真龙星君角色属性()
        self.角色属性A = 真龙星君角色属性()
        self.角色属性B = 真龙星君角色属性()
        self.一觉序号 = 真龙星君一觉序号
        self.二觉序号 = 真龙星君二觉序号
        self.三觉序号 = 真龙星君三觉序号
        self.护石选项 = deepcopy(真龙星君护石选项)
        self.符文选项 = deepcopy(真龙星君符文选项)

    def 界面(self):
        super().界面()

        self.力法及精通选择=MyQComboBox(self.main_frame2)
        self.力法及精通选择.addItem('板甲力驱')
        self.力法及精通选择.addItem('重甲力驱')
        self.力法及精通选择.addItem('布甲法驱')
        self.力法及精通选择.resize(120,20)
        self.力法及精通选择.move(315,480)

        self.反身空斩打=QCheckBox('三段空斩打',self.main_frame2)
        self.反身空斩打.resize(100,20)
        self.反身空斩打.move(325,520)
        self.反身空斩打.setStyleSheet(复选框样式)
        self.反身空斩打.setToolTip('触发潜龙冲击波')

    def 输入属性(self, 属性, x = 0):
        super().输入属性(属性)
        if self.反身空斩打.isChecked():
            属性.反身空斩打 = 1
        属性.力法及精通 = self.力法及精通选择.currentIndex()
        if 属性.力法及精通 == 0:
            属性.防具类型 = '板甲'
            属性.伤害类型 = '物理百分比'
            属性.防具精通属性 = '力量'
        if 属性.力法及精通 == 1:
            属性.防具类型 = '重甲'
            属性.伤害类型 = '物理百分比'
            属性.防具精通属性 = '力量'
        if 属性.力法及精通 == 2:
            属性.防具类型 = '布甲'
            属性.伤害类型 = '魔法百分比'
            属性.防具精通属性 = '智力'
