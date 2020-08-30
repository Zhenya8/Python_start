'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.'''

from time import sleep


class TrafficLight:
    traffic_color = ['RED', 'YELLOW', 'GREEN']

    def running(self):
        while True:
            for color in self.traffic_color:
                if color == self.traffic_color[0]:
                    print(f'\033[31m\033[1m {color} - STOP!')
                    sleep(7)
                if color == self.traffic_color[1]:
                    print(f'\033[33m {color} - WAIT!')
                    sleep(2)
                if color == self.traffic_color[2]:
                    print(f'\033[32m {color} - GO!')
                    sleep(7)
                    print(f'\033[33m {color} - WAIT!')
                    sleep(2)


traffic = TrafficLight()
traffic.running()
# Не поняла, почему все принты жирные получились. Прописала только для одного, а работает для всех