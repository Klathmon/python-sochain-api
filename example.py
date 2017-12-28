"""
Copyright (c) 2017 Fabian Affolter <fabian@affolter-engineering.ch>

Licensed under MIT. All rights reserved.
"""
import asyncio
import aiohttp

from pysochain import ChainSo


@asyncio.coroutine
def main():
    with aiohttp.ClientSession() as session:
        api = ChainSo(
            'LTC', 'M9m37h3dVkLDS13wYK7vcs7ck6MMMX6yhK', loop, session)
        yield from api.async_get_data()

        # Print the data
        for key, value in api.data.items():
            print("{}: {}".format(key, value))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
