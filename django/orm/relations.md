# Relations

```

Many API

.all()
.add() + through_defaults
.create(bulk=True) - !
.set(clear=False)
.remove()
.clear()


Class can access classes dependent on it via
ManyToManyField or ForeignKey through _set or related_name.
```

##### AVFN - access via field_name
##### AVSORN - access via _set or related_name


| field_name      | API for independent class | API for dependent class |
| --------------- | ------------------------- | ----------------------- |
| OneToOneField   | One API - **AVFN**        | One API - **AVFN**      |
| ForeignKey      | Many API - **AVSORN**     | One API - **AVFN**      |
| ManyToManyField | Many API - **AVSORN**     | Many API - **AVFN**    |
