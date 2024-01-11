from pg_message import send_message
import requests


def list_expression():
    list_list = [[[1, 2], [2, 3], [3, 4]], [[4, 5], [5, 6], [6, 7]], [[]]]
    result_list = [c1[0] for row in list_list for c1 in row if len(c1) > 0]
    print("{}, {}".format(result_list, 1))


def use_send():
    send_message.send("Hello, world!")


if __name__ == '__main__':
    use_send()
    req = requests.get(url='https://www.baidu.com')
    print(req)
