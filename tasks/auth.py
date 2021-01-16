from typing import Dict


from data_structures.queues.custom_queue import CustomQueue, EmptyQueueException


MOCKED_DATABASE: Dict[str, str] = {

    'Majster': '123qweASD',

    'Cziter': 'admin1',

    'powaznyUzytkownik': 'mojepowaznehaslo123',

}

class UserAuthenticationService:

    def __init__(self, queue: CustomQueue):

        self._queue = queue

    def authenticate(self):

        try:

            request_user, request_password = self._queue.dequeue()

        except EmptyQueueException:

            return 'No user to authenticate'

​

        password = MOCKED_DATABASE.get(request_user)

        if password is None:

            return f'No user with nick: {request_user}'

​

        if password == request_password:

            return f'{request_user} logged in'

        return 'Wrong password'

​

​

if __name__ == '__main__':

    queue = CustomQueue()

    service = UserAuthenticationService(queue)

​

    queue.enqueue(('Majster', '123qweASD'))

    queue.enqueue(('Cziter', 'admin1'))

​

    print(service.authenticate())

    print(service.authenticate())

    print(service.authenticate())

​

    queue.enqueue(('Mjster', '123qweASD'))

    queue.enqueue(('Majster', 'wrong_password'))

    print(service.authenticate())

    print(service.authenticate())