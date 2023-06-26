# Expressions

## Examples
```
1. Currency.objects.filter(
       cost__gt=F("avg_cost") * 2 - 150
   ).count()

2. Currency.objects.values(
      "title", difference=F("cost") - F("avg_cost")
   )

3. Currency.objects.annotate(
      l=Concat(
         Cast('cost', output_field=models.TextField()),
         Cast('avg_cost', output_field=models.TextField())
      )
      ).order_by(
         Length('l').desc()
      ).values('pk', 'l')
   )

4. Blog.objects.order_by(
      F('title').desc(nulls_first=True)
   )

   .asc(nulls_last=True)
   .desc(nulls_first=True)

5. ExpressionWrapper for output_field with difference types

   Blog.objects.annotate(
      calculation=ExpressionWrapper(
         Concat(
            F("title"), Value(' '), F("created__year")
         ),
         output_field=CharField()
      )
   ).values('pk', 'calculation')

6. Feature
   CharField.register_lookup(Length)
   print(Blog.objects.order_by('obj__length'))

7. Func()
   Give you possibility to call sql functions
   Blog.objects.annotate(
      title_lower=Func(F('title'), function='LENGTH')
   )

   class Lower(Func):
      function = 'LOWER'

   Blog.objects.values('tags').annotate(
      l=Count('title') - Count('slug')
   ).values_list('l', flat=True)

8. Value('string')

   Blog.objects.values('tags').annotate(
      l=Concat(
          Value('| '),
          Round(
              Avg(Length('slug'), default=0),
              output_field=IntegerField()
          ),
          Value(' |'),
          output_field=CharField()
      )
   ).values_list('l', flat=True)

9. Subquery(output_field) + OuterRef() + [:1],
   Exists(output_field) -> bool

   Blog.objects.annotate(
      rfe=Exists(
          Tag.objects.filter(blog__pk=OuterRef('pk'))
      )
   ).values('rfe')

   WHERE EXISTS or ~EXISTS

   Blog.objects.filter(
      Exists(
          Tag.objects.filter(blog__pk=OuterRef('pk'))
      )
   )

   https://django.fun/en/docs/django/4.1/ref/models/expressions/#using-aggregates-within-a-subquery-expression
   .order_by() - set empty select

10. FlteredRelation
    USAGE - <| JOIN ON |> better than WHERE CONDITION

    queryset = Blog.objects.annotate(
        tags2023=FilteredRelation(
            'tags',
            condition=Q(created__second__in=[*range(1, 60, 2)])
        )
    ).values('title', 'tags2023__pk')

11. Race Problem

    currency.cost = F("cost") + 1

    instead of

    currency.cost += 1


    F-Repeat Problem

    Problem - cost was 320 -> 322

    currency.cost = F("cost") + 1
    currency.save()
    currency.title = 'test 5'
    currency.save()
    currency.refresh_from_db()
    print(currency.cost)

12. Window functions

    Blog.objects.annotate(
        exp_name=Round(
           Window(
              expression,
              **window

              // partition_by,
              // order_by,
              // frame,
              // output_field

           )
        )
    )

```


### Repeat Expressions

1. expressions in .filter, .annotate(), .values() & F
2. .asc(null_last, null_first) F().desc()
3. ExpressionWrapper for output_field with difference types.
4. Value('string')
5. Field.register_lookup(Func)
6. Func()
7. Count('title') + Count('slug')
8. Subquery, Exists in select or where, OuteRef + [:1],
9. FlteredRelation instead of condition in where.
10. Race, F-repeat problems and .order_by() is empty soluton.
11. Window functions - 12 + frame
