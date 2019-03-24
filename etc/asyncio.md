### asyncio 정리 

#### couroutine 이란?  
코루틴의 개념을 이해하기 위해서 서브루틴의 개념을 먼저 이해하자.  
- 서브루틴이란?  
서브루틴은 함수, 메서드에 해당되며 메인 루틴에서 서브루틴을 실행 할 경우 특정 지점(서브)에서 return 이 될때까지 루틴을 실행한 후 원위치(메인)로 돌아온다.  

- 코루틴과 서브루틴의 차이점 2가지
    - 코루틴의 경우, return 이 아닌 yield 를 통해 값을 전달하며 값을 내놓았다는 것이 해당 루틴의 종료를 의미하는 것이 아니라 중단되었음을 의미한다. 이는 멈춘 지점으로 돌아와 다시 코루틴을 실행할 수 있음을 의미한다.  
    한마디로 중간에 멈춰서 특정위치로 돌아갔다가 다시 원래위치로 돌아와 나머지 루틴을 실행할 수 있다.  
    - 서브루틴의 진입점과 반환점은 한 개뿐이지만 코루틴은 여러개의 진입지저이 존재한다.
    
코루틴을 이해하기 위해서 yield 를 살펴보자.
- yield 란?  
python generator 객체에 사용되는 문법이며 generator 객체 생성 후 next() 함수를 실행하면 다음 yield 지점에서 값을 내놓도록 동작한다.
    ```python
    def print_abc():
        yield print('a')
        yield print('b')
        yield 1
  
    a = print_abc()
    next(a)
    next(a)
    print(type(next(a)))

    # a
    # b
    # c
    ```  
    ```yield x``` 에서 yield 는 값을 내놓은 '시점/지점' 에 해당하며 x 는 내놓을 '값'에 해당한다.  
    - send() 를 통해 값을 전달할 수도 있다.   
        ```python
        def test1(i):
            print('start test1 coroutine')
            while i:
                b = yield i
                i += b
        a = test1(5)

        print(next(a))
        print(a.send(3))
        print(a.send(7))
        
        # start test1 coroutine
        # 5
        # 8
        # 15
        ```  
        ```b = yield i``` 에서 b 는 send() 를 통해 '전달되는 값의 변수명' 에 해당한다. '=' 때문에 b 의 의미가 약간 헷갈리긴 하지만 일단 코드상에서 하는 역할은 저렇다.  
    
    - genarator 객체이기때문에 for 문에 다음과 같이 활용가능하다.
        ```python
        def countdown(n):
            while n > 0:
                yield n
                n -= 1
        for i in countdown(5):
            print(i, end=" ")
            
        ### 5 4 3 2 1
        ```  
        
    - 만약 100까지의 숫자를 리스트에 담도록한다면 range 를 사용할 경우 100개의 숫자를 가져올 메모리 공간이 필요하다. 하지만 yield 를 사용하면 숫자를 100번에 나눠 가져올 수 있으므로 메모리 공간을 절약할 수 있다. 이 점이 yield 제네레이터의 유용성이라고 한다.  
    
코루틴은 보통 caller 와 callee 로 존재하는 종속적인 관계의 흐름에 해당되지 않는다. 코루틴을 동작하게 하기 위해선 호출이 필요하지만 이를 종속적으로 보지 않고 대등하게 값을 입력하고 내어주는 대등한 관계의 흐름이라고 본다. 제어권을 주고 받는다고 이해하자.  
이때 값의 입력과 값을 가져온다는 의미가 중요하다. 값의 입력은 send() 를 통해 이뤄지는데 ```b = yield i``` 의 경우 b 를 입력하고 i 를 가져오게된다.  
이해하기가 좀 어렵지만 언제든지 코루틴에 해당되는 동작을 이어서 실행할 수 있고 대기 상태로 값의 입력을 받을 수 있기때문에 서브루틴과 다른 방식이라고 받아들이면 될 것 같다.   

#### 비동기 IO 코루틴을 위한 asyncio

- 코루틴 
    > A coroutine is a special function that can give up control to its caller without losing its state. A coroutine is a consumer and an extension of a generator. One of their big benefits over threads is that they don’t use very much memory to execute. Note that when you call a coroutine function, it doesn’t actually execute. Instead it will return a coroutine object that you can pass to the event loop to have it executed either immediately or later on.
- future
    > One other term you will likely run across when you are using the asyncio module is future. A future is basically an object that represents the result of work that hasn’t completed. Your event loop can watch future objects and wait for them to finish. When a future finishes, it is set to done. Asyncio also supports locks and semaphores.
- Task
    > The last piece of information I want to mention is the Task. A Task is a wrapper for a coroutine and a subclass of Future. You can even schedule a Task using the event loop.

안타깝게도 asyncio 에서 사용되는 코루틴은 genarator 기반의 코루틴과 다른 방식이라고 한다. 하지만 동작하는 개념은 동일한 듯하고 단지 사용하는 문법적인 측면에서 다른점이 있는 듯하다.  
asyncio 에서는 async 와 await 문법을 사용하여 비동기 IO 를 구현한다. 밑의 설명을 보니 genarator 와 비교해서 async, await 를 언급한다.
> The async and await keywords were added in Python 3.5 to define a native coroutine and make them a distinct type when compared with a generator based coroutine. If you’d like an in-depth description of async and await, you will want to check out PEP 492.


  
- async 란?  
코루틴으로 정의하려는 함수의 def 앞에 붙여준다.  

- await 란?  
코루틴 함수 내부에서 비동기 작업을 호출할 때 앞에 붙여줘야하며 호출되는 함수 역시 비동기 코루틴(async 가 붙은)함수여야 한다. 병렬적으로 코드가 실행될 지점에 붙여주면 되며 await 가 붙은 지점에서 요청을 보낸 후 기다리는 시간 동안 다음 task 를 진행하는 시점이 된다.

- ensure_future() 란?  
async 나 await 로 작성된 코루틴은 create_task(coroutine) 을 통해 TASK 객체가 된다. task 객체가 아니라면 loop 를 실행시킬 수 없으므로 필수적으로 create_task()를 해주어야 한다.  
이때 ensure_future(coroutine) 과 같이 코루틴 함수를 인자로 넣어 실행시켜주면 ensure_future() 안쪽에서 create_task() 를 실행시켜서 TASK 객체를 만들어준다.  
그외에도 Future 객체인지 검사한 후 아닐 경우 ValueError 를 발생시키는 역할 또한 존재한다.

#### 브런치 프로젝트에 사용한 코드(request 및 aiohttp)
```python
async def detail_crawl(url, article_txid):
    print(f'Send request .. {url}')

    async with aiohttp.ClientSession() as sess:
        async with sess.get(url) as res:
            r = await res.text()
```

- aiohttp.ClientSession() 란?  
client 에 해당되는 나의 세션 객체를 생성하며 안쪽에서 loop 를 get 하게된다. get 한 loop 를 통해 request 작업을 실행한다.

- 코드 작동  
위에서 설명 했듯이 await 코드 바로 위쪽에서 다음 TASK 로 넘어가게 된다. 다음 TASK 로 넘어갈 경우 다시 loop 를 get 하게 되며 첫번째 loop 와 두번째 loop 는 동일하다. 또한 디버그를 통해 thread_id 값이 같음을 확인했으므로 멀티쓰레드와 비동기가 다른 방식이라는 것을 확인할 수 있다.