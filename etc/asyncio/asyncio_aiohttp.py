import asyncio
import time

import aiohttp

# aiohttp 를 쓰는 이유:
# requests module 은 coroutine 으로 만들어진 module 이 아니기때문에
# 내부적으로 thread 를 만들어서 동작한다. 따라서 요청의 수가 많아질수록
# context switching 의 비용(시간, cpu 의 작업)이 발생한다.
# 비동기 http 통신 lib 인 aiohttp 를 이용하면 coroutine 을 이용한
# 비동기 방식을 이용할 수 있다.

# asycio 를 제대로 사용하기 위해서는 사용하는 module 들이 모두 coroutine으로
# 작성되어있어야 한다.
# Aewsome Asyncio(https://github.com/timofurrer/awesome-asyncio)
# 위 페이지에는 asyncio 기반 module 을 소개하고 있다
from bs4 import BeautifulSoup


async def get_text_from_url(url):
    print(f'Send request to ... {url}')

    async with aiohttp.ClientSession() as sess:
        async with sess.get(url, headers={'user-agent': 'Mozila/5.0'}) as res:
            text = await res.text()

    print(f'Get response from ... {url}')
    text = BeautifulSoup(text, 'html.parser').text
    print(text[:100].strip())


async def main():
    base_url = 'https://www.macmillandictionary.com/us/dictionary/american/{keyword}'
    keywords = ['hi', 'apple', 'banana', 'call', 'feel',
                'hello', 'bye', 'like', 'love', 'environmental',
                'buzz', 'ambition', 'determine']

    # 아직 실행된 것이 아니라, 실행할 것을 계획하는 단계
    futures = [asyncio.ensure_future(get_text_from_url(
        base_url.format(keyword=keyword))) for keyword in keywords]

    await asyncio.gather(*futures)


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    end = time.time()
    print(f'TIME: {end - start}')
