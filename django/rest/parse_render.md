# Parse and Render

```
def encode(model: WomenModel = WomenModel('Vlad', 'I\'m GAY')):
    """
    1. Serialize model to dict.
    2. Render to json
    """
    serialized_model = WomenSerializer(model, many=False)
    dict_ = serialized_model.data

    json = JSONRenderer().render(dict_)
    print(json)


def decode(json: bytes = io.BytesIO(b'{"title": "LERA", "content": "VLAD"}')):
    """
    1. Parse json
    2. Serialize and get validated_data
    """
    dict_ = JSONParser().parse(json)
    serializer = WomenSerializer(data=dict)
    if serializer.is_valid(raise_exception=True):
        print(serializer.validated_data)
```