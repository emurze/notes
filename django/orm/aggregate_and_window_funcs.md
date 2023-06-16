# Aggregate functions

```

Agregate(output_field=None, distinct=True, filter=Q(pk__gt=3), default=1)

Avg()
Max()
Min()
Count()
Sum()

Math

StdDev()
Variance()

GROUP BY

values('is_active'): that group by
annotate(total=Count('id')): that aggregate
```

```
WINDOW functions

Rank functions

ROW_NUMBER - pk
RANK - pk, but located as groups with gaps in values
DENSE_RANK - pk, but located as groups without gaps in values
NTILE(3) - DIVIDE PARTITIONED PARTS ON 3 equals parts


Analytical functions

PERCENT_RANK
PERCENTILE_CONT
PERCENTILE_DISC
CUME_DIST


Shift functions

NTH_VALUE(field, number) - all values by numbers with ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
LEAD - by pk
LAG - by pk
LAST_VALUE - all last values with ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING
FIRST_VALUE - all first values with ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING


Aggregate | Window functions works by Framed

ROWS and RANGE always with ORDER BY

ORDER BY ... ROWS BETWEEN ... and ...
UNBOUNDED PRECEDING - window starts with first string of group
UNBOUNDED FOLLOWING - window ends with last row of group
CURRENT ROW - window ends or starts with current row
1 or <value> PRECEDING | 1 or <value> FOLLOWING - only in ROWS

gifs - https://learnsql.com/blog/difference-between-rows-range-window-functions/


ValueRange(start=None, end=None)

RowRange(start=None, end=None)


Blog.objects.annotate(
   test=Window(
      Sum(Length('title')),
      partition_by='tags',
      order_by='category',
      frame=RowRange(-1, 0)
   ), len=Length('title')
).values('tags__name', 'len', 'test')
```
