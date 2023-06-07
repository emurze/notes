# Django orm 

### Queryset execution

* iterations
* slice with step
* repr(), len(), bool()

### Queryset properties

* .ordered
* .db
* .query
* ._result_cache


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