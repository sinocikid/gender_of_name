import requests

def get_gender(name):
    """
    Predict gender based on name

    Args:
        name: First Name

    Returns:
        Gender and Possibility
    """

    url = "https://api.genderize.io/?name=" + name
    response = requests.get(url)
    data = response.json()

    return data["gender"], data["probability"]


def main():
    # input name
    name = input("Please enter First Name：")

    # get gender and probability
    gender, probability = get_gender(name)

    # 输出结果
    print(f"Gender：{gender}")
    print(f"Possibility：{probability}")


if __name__ == "__main__":
    main()
