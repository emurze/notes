# TDD

![pyramide](images/pyramide.webp)

* Manual <span style="color: white">QA-Task</span>

* Functional Tests - <span style="color: white">QA-Task</span> | <span style="color: #00bfff">Dev-Task</span> have User History and Human-names

* Integration Tests - <span style="color: #00bfff">Dev-Task</span> Tasks between units or modules. Access to unit is not required.

* Component Tests - <span style="color: white;">QA-Task</span> ( black-box testings, comes after unittests, Is not docs for future use )<br>
Detailized func test

* Unittests - <span style="color: #00bfff">Dev-Task</span> ( white-box, should contain great project docs ) - <br>
<span style="color: green;">Checks correctness of the 1 unit of behavior if not then it's integration test</span> Access to unit is required

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
response = self.client.post('/', data={})
self.assertEqual(response.status_code, HTTPStatus.FOUND)
self.assertEqual(response['LOCATION'], '/')
#
self.assertRedirects()
```

* behavior integration tests ( can create item, etc )
```
| can create post
|
| show post when necessary
|
| can display items
```

* Form validation
```
def test_duplicate() -> None:
    pass
#
def test_form_invalid_not_saved_item(self) -> None:
    self.client.post(self.url, data={'content': 'Hi' * 600})
    self.assertEqual(List.objects.count(), 0)
    self.assertEqual(ListItem.objects.count(), 0)
#
def test_form_invalid_show_maxlength_error(self) -> None:
    response = self.client.post(self.url, data={'content': 'Hi' * 600})
    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertContains(response, self.form_maxlength_error)
#
def test_form_invalid_show_null_error(self) -> None:
    response = self.client.post(self.url, data={'content': ''})
    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertContains(response, self.form_required_error)
#
def test_form_invalid_template(self) -> None:
    response = self.client.post(self.url, data={'content': ''})
    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertTemplateUsed(response, self.base_template)
```

* Don't forget
```
response.status_code == HTTPStatus.OK | etc
```

* Always test context_data variables


## Model

```

validation tests

   - .pk equal to field

   - default

   - not null

   - unique

   - check_constraint

   - fk m2m

* test get_absolute_url | meta attrs like ordering, unique, etc
```


## Form

* unittests checking constraints base and from models ( dupilicates, not null )
```
class ToDoCreateItemFormTest(TestCase):
    def test_content_maxlength_constraint(self) -> None:
        form = TodoCreateItemForm(data={'content': 'New item' * 200})
        self.assertIn(
            'Ensure this value has at most 256 characters',
            str(form.errors['content']),
        )
```

* integration tests
```
def test_get(self) -> None:
    response = self.client.get('/')
    html = response.content.decode('utf-8')

    self.assertEqual(response.status_code, HTTPStatus.OK)
    self.assertIn('<h2>Add Item</h2>', html)
#
def test_post_success(self) -> None:
    response = self.client.post('/', data={'content': 'Hi'})

    self.assertEqual(response.status_code, HTTPStatus.FOUND)
    self.assertEqual(response['LOCATION'], '/')

    self.assertRedirects()
#
def test_error_message(self) -> None:
    response = self.client.post('/', data={'content': 'Hi' * 600})
    html = response.content.decode('utf-8')

    self.assertEqual(response.status_code, 200)
    self.assertIn('Ensure this value has at most 256 characters', html)

    self.assertContains()
#
def test_error_and_not_saved_item(self) -> None:
    self.client.post('/', data={'content': 'Hi' * 600})
    self.assertEqual(ListItem.objects.count(), 0)
```

* test attrs
```
def test_form_content_classes(self) -> None:
    form = TodoCreateItemForm(data={'content': 'New item'})
    self.assertIn('class="form-control', form.as_p())
```

* test view uses right form_class for error and get
```
def test_home_page_uses_item_form(self):
    response = self.client.get('/')
    self.assertIsInstance(response.context['form'], ItemForm)
```

* test all response.context variables context['items'] context['title']


## Mixin

* unittest
```
class TestHomePageItemsListMixin(TestCase):
    """Unittest"""

    class Mixin(ListItemMixin, TemplateView):
        template_name = 'home_page.html'

    def setUp(self) -> None:
        self.view = self.Mixin()

    def test_context_data_items(self) -> None:
        context = self.view.get_context_data()
        self.assertIsInstance(context['items'], QuerySet)
```

* integration view test
```
response = self.client.get(self.url)
self.assertIsInstance(response.context['items'], QuerySet)
```


## Single Test for layout

```
self.assertAlmostEqual(
  1,
  1
  delta=20,
)
```

## Advices

```
Highlight contexts:

  form_valid

  form_invalid

  get

  post

Know can spread to several layers ( model, view, forms ) like Form Validation
```

## Django features


```
django doesn't execute Validation

use .full_clean()

or form.is_valid()
```

## Django unittest features

```
resolve(self.url)

self.client.get(self.url)

self.client.post(self.url, data={})

self.user = User.objects.create_user(
    username='vlad', password='146080ce'
)
self.client.login(username='vlad', password='146080ce')

self.assertTrue()

self.assertEqual()

self.assertAlmostEqual()

self.assertContains()

self.assertRedirects()

self.assertIn()

self.assertTemplateUsed()

self.assertRaises()

self.assertIsNone()
```

## TDD cycle

```
functional test -> unittest fail -> code success -> refactor success
```

## Mocks

```
.called
.call_args -> call() or ((,), {})
.return_value -> Mock

@patch('apps.hi.module')
class Hi:
  pass

@patch('apps.hi.module.messages')
def func(mock: MagicMock):
  pass


# Only existing methods and args
StrictMock = mock.create_autospec(Bar, spec_set=True)

1. Mocking for declarative

2. Mocking for external dependences
```

## Mail

```
# test success messages

# test mail.output

# test POP3 mail if stage server
```


## Commands

```
coverage run manage.py test

coverage report
```
