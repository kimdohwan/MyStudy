

#### Serialization
- serialization is the processing of translating **data structures, or object state** into **a format that can be stored** (for example, **in a file or memory buffer**) or transmitted (for example, **across a network connection link**) and reconstructed later (possibly in a different computer environment).  

#### django restframework  
1. serialize 를 해주는 class 작성
  - serializer.Serializer: 직접 class attribute 및 create, update 등 작성 요구됨  
  - serializer.ModelSerializer:   
    - django 의 model 을 입력받아 serializer 해준다
    - fields 값에 전송, 응답 하고자 하는 model 의 attribute(column) 설정  
2. serialize 된 data 를 전달하는 view 작성  
  - APIView  
  - generics
  - mixins

```python
class SnippetList(APIView):
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)
```
```python
class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
```
```python
class SnippetList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
```
