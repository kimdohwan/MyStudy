import time

import requests
import asyncio
from functools import partial

from bs4 import BeautifulSoup


async def get_text_from_url(url):

    print(f'Send rquest to ... {url}')

    # loop 생성해주고
    loop = asyncio.get_event_loop()

    # loop.run_in_executor 에서는 keyword 인자를 사용할 수 없어서 partial을 활용
    request = partial(requests.get, url, headers={
        'user-agent': 'Mozila/5.0'})

    # 쓰레드풀을 만들거라면 concurrent.futures.threadpoolexecutor 사용
    res = await loop.run_in_executor(None, request)
    print(f'Get response from ... {url}')

    text = BeautifulSoup(res.text, 'html.parser').text
    print(text[:100].strip())


async def main():
    base_url = 'https://www.macmillandictionary.com/us/dictionary/american/{keyword}'
    keywords = ['hi', 'apple', 'banana', 'call', 'feel',
                'hello', 'bye', 'like', 'love', 'environmental',
                'buzz', 'ambition', 'determine']

    # 아직 실행된 것이 아니라, 실행 할 것을 계획하는 단계
    # list futures 에는 Task 객체가 keyword 갯수만큼 담겨있다
    # 보류중인 Task 를 10개 담아놓은 후 asyncio.gather() 에 전달한다
    futures = [asyncio.ensure_future(get_text_from_url(
        base_url.format(keyword=keyword))) for keyword in keywords]

    # asterisk(*)을 사용해서 unpacking 상태로 넣어줘야 한다
    # 보류중인 task 들을 실행시킨다
    await asyncio.gather(*futures)


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()
    print(f'TIME: {end - start}')
