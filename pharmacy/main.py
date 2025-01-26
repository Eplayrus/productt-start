import threading
import time


class Pharmacy:
    def __init__(self):
        self.costumers = threading.Semaphore(value= 2)


    def meet_costumer(self, costumers):

        print(f"\nПриглашаем поситителя - {costumers}")
        self.costumers.acquire()

        print(f"\nРабота с поситителем - {costumers}")
        time.sleep(5)

        print(f"\nЗавершение работы с поситителем - {costumers}")
        self.costumers.release()



    def costumer(self, count):
        for visitor in range(count):
            costumer_thread = threading.Thread(target= self.meet_costumer,
                                               args=(visitor,))
            costumer_thread.start()
            costumer_thread.join()

if __name__ == "__main__":
    pharmacy = Pharmacy()

    count = 6
    pharmacy.costumer(count)

