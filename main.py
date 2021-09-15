import time

import requests

from encrypt import encrypt_data

api = {
    'login': 'https://changjiang.yuketang.cn/pc/login/verify_pwd_login/',
    'onlesson': 'https://changjiang.yuketang.cn/v/course_meta/on_lesson_courses',
    'attendlesson': 'https://changjiang.yuketang.cn/v/lesson/lesson_info_v2',
}


def login(ipone, pwd):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://changjiang.yuketang.cn',
        'Host': 'changjiang.yuketang.cn',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 14_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 MQQBrowser/11.8.3 Mobile/15E148 Safari/604.1 QBWebViewUA/2 QBWebViewType/1 WKType/1',
        'X-CSRFToken': 'B5bIlxImKX4IpDiYKWuNs8sc02hgbSCV',
        'Referer': 'https://changjiang.yuketang.cn/web',
        'X-Requested-With': 'XMLHttpRequest',
    }

    data = '{"type":"PP","name":"' + ipone + '","pwd":"' + encrypt_data(pwd) + '"}'

    response = requests.post(api['login'], headers=headers,
                             data=data, verify=False)
    print(response.json())
    if (response.json().get("success")):
        print("login success")
        return response.cookies

    else:
        print("login error")
        raise Exception("login error")


def getOnLessonData(cookie):
    response = requests.get(url=api['onlesson'], cookies=cookie)
    print(response.json())
    if 'data' in response.json():
        onlessons = response.json()['data']['on_lessons']
        return onlessons
    else:
        onlessons = []
        return onlessons


def attendLesson(cookies, lesson_id):
    params = {
        'lesson_id': lesson_id
    }
    response = requests.get(url=api['attendlesson'], cookies=cookies, params=params)
    data = response.json()
    if data['success']:
        lesson_name = data['data']['classroom']['courseName']
        return lesson_name

def doAction():
    cookie = login("your ipone", "your password")
    while (True):
        print('start one')
        on_lessons = getOnLessonData(cookie)
        if len(on_lessons) != 0:
            for i in on_lessons:
                lesson_id = i['lesson_id']
                lesson_name = attendLesson(cookies=cookie, lesson_id=lesson_id)
                print(lesson_name)
        time.sleep(60)


if __name__ == '__main__':
    # doAction()
    cookie = login("15762323410", "Lx1793786487")
