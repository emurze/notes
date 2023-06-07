# Meta options

```

Interfaces

abstract
proxy
managed


Default

base_manager_name
default_manager_name
default_related_name - '%(field_name)s_set'


DB

db_table
db_table_comment
db_tablespace


Ordering 

ordering
ordering_with_respect_to + API


Naming 

varbose_name / plural
app_lable - for libraries


Permissions

pemissions
default_permissions - ('add', 'change', 'delete', 'view')


Requirements

required_db_features
required_db_vendor - ('MongoDb', 'Postgres')


Features

indexes: list[index]
constraints: list[constraint]
get_latest_by - order to latest()
```

### Repeat Meta options

1. Interfaces - 3
2. Default - 3
3. DB - 3
4. Ordering - 2
5. Permissions - 2
6. Naming - 3
7. Features - 3
