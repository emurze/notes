# Padding Margin

```

box-sizing: border-box | content-box;

border-box - margin | border | padding + content + padding | border | margin
content-box - margin | border | padding | content | padding | border | margin


1. border-box decrease content via padding

2. padding + bg-image + bg-posiiton
   padding + absolute element + relative main + left: 0; top: 0;

li {
  padding-left: 15px;
  background-image: url("../images/minus.svg")
  background-position: 0 3px;
  background-repeat: no-repeat;
}

&::before {
    content: "";
    position: absolute;
    left: 33px;
    z-index: 3;
    width: 15px;
    height: 15px;
    background: url("../images/minus.svg") 0 3px no-repeat;
}

3. padding + overflow and image

4. margin: 0 auto;

5. shift - relative + z-index + -margin

6. .container {
      display: flex;
      margin: 0 -40px;

      .column {
          flex: 0 1 33.333%;
          padding: 0 40px;

          .item {
              background-color: purple;
              padding: 15px;
          }
      }
  }

7. decrease objest or slider - margin: 0 -30px, padding: 0 30px;  

8. mix for difference logic portgolie__header header and apple__header header

9. increase link square via padding

10. higher element has padding or margin and last_child
```

### Repeat

1. border_box
2. <li> photo 2 patterns
3. decrease image via padding
4. center object
5. shift with -margin
6. space between flex elements
7. full decrease via padding and -margin
8. mix
9. increase link square via padding
10. higher element has margin | padding and use last_child margin reset
