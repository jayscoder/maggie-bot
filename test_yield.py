
def coroutine():
    while True:
        value = yield 'a'
        print(f'Received value: {value}')

coro = coroutine()
print(next(coro))
coro.send('Hello')
