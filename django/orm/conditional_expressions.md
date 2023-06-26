# Condition expressions

```
1. When(account_type=Client.GOLD, then='name')

2. When(Q(name__startswith="John") | Q(name__startswith="Paul"),
        then='name')

3. When( Exists( Client.objects.filter(...) ), then=F("") or Value('string') )

4. Client.objects.annotate(
       cost=Case(
           When(account_type=Client.AccountTypes.GOLD, then=Value('5%')),
           When(account_type=Client.AccountTypes.PLATINUM,
        вR)
       )
   )
```
