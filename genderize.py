import requests

def get_gender(name):
    """
    根据姓名预测性别

    Args:
        name: 英文姓名

    Returns:
        性别和概率
    """

    url = "https://api.genderize.io/?name=" + name
    response = requests.get(url)
    data = response.json()

    return data["gender"], data["probability"]


def main():
    # 输入姓名
    name = input("Please enter First Name：")

    # 获取性别和概率
    gender, probability = get_gender(name)

    # 输出结果
    print(f"Gender：{gender}")
    print(f"Possibility：{probability}")


if __name__ == "__main__":
    main()
