import logging
import random
import threading
import time

total_tickets = 50
available_tickets = 10

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Seller(threading.Thread):

    def __init__(self, semaphore: threading.Semaphore):
        super().__init__()
        self.sem = semaphore
        self.tickets_sold = 0
        logger.info('Seller started work')

    def run(self):
        global total_tickets
        is_running = True
        while is_running:
            self.random_sleep()
            with self.sem:
                if total_tickets <= 0:
                    break
                self.tickets_sold += 1
                total_tickets -= 1
                logger.info(f'{self.getName()} sold one;  {total_tickets} left')

        logger.info(f'Seller {self.getName()} sold {self.tickets_sold} tickets')

    def random_sleep(self):
        time.sleep(random.randint(0, 1))


class Director(threading.Thread):
    def __init__(self, semaphore: threading.Semaphore):
        super(Director, self).__init__()
        self.lock = semaphore
        logger.info('Director started work')

    def run(self):
        global total_tickets, available_tickets
        while total_tickets:
            if available_tickets < 4:
                with self.lock:
                    tickets_to_print = 10 - (available_tickets % 10)
                    if tickets_to_print > total_tickets:
                        tickets_to_print = total_tickets
                    available_tickets += tickets_to_print
                    total_tickets -= tickets_to_print
                    logger.info(f'Director put {tickets_to_print} new tickets')
        logger.info('Director has stopped working. No tickets left')


def main():
    semaphore = threading.Semaphore()
    director = Director(semaphore=semaphore)
    director.start()
    sellers = [director]

    for _ in range(4):
        seller = Seller(semaphore)
        seller.start()
        sellers.append(seller)

    for seller in sellers:
        seller.join()


if __name__ == '__main__':
    main()
