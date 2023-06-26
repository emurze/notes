# Images

```

1. width: 100%; - expands to full other object width & responsive
2. max-width: 100%; - image size & responsive
3. parent - height: 200px;
   self - width: 100%; height: 100%;

   object-fit: fill | contain | none | cover
   object-position: ...

   &__item {
       padding: 0 0 58% 0; !!!
       //overflow: hidden;
       text-align: center;
       position: relative; !!! - to height or flex or ...

       img {
           height: 100%;
           width: 100%;
           object-fit: cover;
           position: absolute; !!!
           top: 0; !!!
           left: 0;        
           max-width: 2560px;
           max-height: 1390px; !!!
       }

.container {
    display: flex;
    margin: 0 -20px;

    &__column {
        padding: 0 20px;
        flex: 0 1 33.333%;
    }
    &__item {
        padding: 0 0 58% 0;
        text-align: center;
        position: relative;

        img {
            height: 100%;
            width: 100%;
            object-fit: cover;
            position: absolute;
            top: 0;
            left: 0;
        }
    }
}
4. picture source !!!

```
