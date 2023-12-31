from dataclasses import dataclass
import time
import asyncio


@dataclass
class Messgage:
    n: int = 0

    def __aiter__(self):
        print("__aither__")
        return self

    async def __anext__(self):
        if self.n == 5:
            raise StopAsyncIteration
        self.n += 1
        return self.n - 1


async def fn(what):
    await asyncio.sleep(1)
    print(what)


async def countdown():
    n = 0
    while n <= 10:
        await asyncio.sleep(0.1)
        yield n
        n += 1


def sync_countdown():
    n = 0
    while n <= 10:
        time.sleep(0.1)
        yield n
        n += 1


async def main():
    # task = asyncio.create_task(fn("showmethemoney"))
    # asyncio.create_task(fn("operationcwal"))
    # asyncio.create_task(fn("powerovershelming"))

    # async for i in countdown():
    #     print(f"async: {i}")

    # for i in sync_countdown():
    #     print(f"sync: {i}")

    _coroutine = fn("blacksheepwall")
    print(type(_coroutine))
    _task = asyncio.create_task(fn("thegathering"))
    print(type(_task))

    asyncio.gather(
        fn("showmethemoney"),
        fn("operationcwal"),
        fn("foodforthought"),
    )

    await asyncio.create_task(fn("powerovershelming"))

    await _coroutine

    # m = Messgage()
    # async for msg in m:
    #     print(msg)


asyncio.run(main())
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# loop.close()
