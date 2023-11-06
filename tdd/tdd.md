# TDD

![pyramide](images/pyramide.webp)

* Manual <span style="color: white">QA-Task</span>

* Functional Tests - <span style="color: white">QA-Task</span> | <span style="color: #00bfff">Dev-Task</span> have User History and Human-names

* Integration Tests - <span style="color: #00bfff">Dev-Task</span> Tasks between units or modules

* Component Tests - <span style="color: white;">QA-Task</span> ( black-box testings, comes after unittests, Is not docs for future use )<br>
Detailized func test

* Unittests - <span style="color: #00bfff">Dev-Task</span> ( white-box, should contain great project docs )

## Dev pyramide

![dev_pyramide](images/dev_pyramide.jpg)


# Django


## View

* test url
```
resolver = resolve('/')
self.assertEqual(resolver.func.view_class, HomePageView)
```

* test template
```
# manual
request = HttpRequest()
request.user = AnonymousUser()
request.method = 'GET'
response = HomePageView.as_view()(request).render()
self.assertEqual(
    response.content.decode('utf-8'),
    render_to_string('home_page.html')
)
# or
response = self.client.get('/')
self.assertTemplateUsed(response, '<template_name>')
```

* test redirect
```
```

* test json
```
```

* other behavior tests


## Model

* create and retrieve
```
# create
ListItem.objects.create(content='item_1')
ListItem.objects.create(content='item_2')
# count
self.assertEqual(2, ListItem.objects.count())
# retrieve
item_1, item_2 = ListItem.objects.all()
self.assertEqual(item_1.content, 'item_1')
self.assertEqual(item_2.content, 'item_2')
```

## Form
