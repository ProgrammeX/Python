import datetime
出生年份 = input("请输入您的出生年份：")
当前年份 = datetime.datetime.now().year
年龄 = 当前年份 - int(出生年份)
print("您的年龄为："+str(年龄) + "岁")
if 年龄<18:
    print("您现在是未成年人")

if 年龄>=18 and 年龄<66:
    print("您现在是青年人")

if 年龄>=66 and 年龄<80:
    print("您现在是中年人")

if 年龄>=80:
    print("您现在是老年人")

if 年龄>81:
    print("真老，我都不大相信")
