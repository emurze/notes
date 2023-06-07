# Django orm 

## Queryset

### Execution

* iterations
* slice with step
* repr(), len(), bool()

### Properties

* .ordered
* .db
* .query
* ._result_cache


### Features
* unique 
* lazy
* using cache


### Methods.

```
Filtering

.filter() 
.exclude()


Aggregation

.annotate()
.aggregate()
.alias()


Ordering

.order_by('?')
.reverse()


Select

.values(**expressions)
.value_list(flat=True, named=True)


Date

.date(kind='month')
.datetimes(kind='hour')


DML 

.get()
.create()
.update()
.delete()

.get_or_create()
.update_or_create()

.bulk_create()
.bubl_update()


Optimization

.defer() - accumulable
.only() - replaceable

.count()
.exists()
.iterator()
.contains()

.explain()
.select_for_update()
.using()

.last() / .first()
.latest() / .earliest() - last or frst by ordering

.union(all=True)
.intersection()
.difference()

.select_related() - JOIN
.prefetch_related(
    Refrech()
) - CACHE


Features

.raw()
.none()
.all()
```

### Repeat Queryset

Execution - 3

Properties - 4

Features - 3

Methods:
1. Filtering - 2
2. Aggregation - 3
3. Ordering - 2
4. Select - 2
5. Date - 2
6. DML - 8
7. Optimization - 16
8. Features - 3
