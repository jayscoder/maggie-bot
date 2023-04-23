
def coroutine():
    while True:
        value = yield 'a'
        # print(f'Received value: {value}')

coro = coroutine()
next(coro)
print(coro.send('Hello'))
