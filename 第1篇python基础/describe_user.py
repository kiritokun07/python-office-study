class People:
    """定义 People 类"""

    def __init__(self, name: str, location: str, career: str):
        self.name = name
        self.location = location
        self.career = career
        self.age = 18  # 默认属性值，不需要传参

    def introduce_you(self):
        introduce = '大家好，我是{name}，今年{age}岁，来自{location}，我的工作是{career}，很高兴认识大家！'
        msg = introduce.format(name=self.name, age=self.age, location=self.location, career=self.career)
        print(msg)
