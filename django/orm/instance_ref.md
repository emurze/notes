# Instance ref

```
1. Add methods to Manager or Model
2. instance.refresh_from_db() - update instances_values to db_values
	 Model.from_db() - get + instance settings
	 instance._state.db = 'default' or 'postgres' or None
	 instance._state.adding = False, True - it is adding?

3.
instance.full_clean(
	 exclude=None,

	 // implicity
	 clean_fields - method 1
	 clean - method 2

	 validate_unique=True, - method 3
	 vlidate_constraints=True - method 4
)

4.
.only(), .defer() -> get_deffered_fields()

choices -> get_<field_name>_display()

DateField - get_next_by_<date_field_name>
						get_previous_by_<date_field_name>

5.
save(
		self,
		force_insert=False, - possible error
		force_update=False, - possible error
		using=None,
		update_field=None - update list of fields
)

save operations
1. send pre-save signal

2. process functions signal
3. prepare data             - Saving
4. INSERT OR UPDATE to db

5. send post-save


```

## Repeat

1. Add methods
2. 2 take from db methods
3. clean
4. instance.get_methods() - 3
5. save operations
