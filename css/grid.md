# Grid

```
grid-template: repeat(2, 1fr) / repeat(3, 1fr);
gird-template-columns: auto minmax(300px, 1fr) fitcontent(400px);
grid-template-rows: 1fr 1fr

grid-template-areas:
    "header header"
    "side content"

grid-auto-rows: 200px; - one item in rows
grid-auto-columns 500px; - one item in columns
grid-auto-flow: row | column | dense - row, but without blanks;

gap: 20px;
row-gap: 20px | 20%;
column-gap: 20px;

align-items: stretch;
justify-items: stretch;


instance

grid-area: header;

grid-row: 1 / 2; - start, end
grid-row-start: auto;
grid-row-end: auto;

grid-column: 1 - start line / 2 - end line;
grid-column-start: auto;
grid-column-end: auto | span 2 | 2;

order: 1; - must have each element

align-self: stretch;
justify-self: stretch;

margin: auto; - center



padding | margin must be without percent for browser compatibility
margin works without collapse

implicit and explicit instances

row - vertical
column - horizontal

you can set and use grid-titles [row2 - title] 1fr


minmax(no-fr, fr)

1. minmax(100px, 1fr) - 1fr with min
2. mimax(auto, 250px)
3. mimax(250px, auto) - 250px to all

repeat(auto-fit | auto-fill, minmax(250px, 1fr))
fit-content(max-width) - auto (inline)
span - go span 2


1. grid-template-areas:
      "header header"
      "footer footer";
      "sidebar main"

    grid-area: "header";

2. grid-area: 1 / 1 / 2 / 2


USING when grid-template: none;

grid-auto-rows: 200px; - one item in rows
grid-auto-columns 500px; - one item in columns
grid-auto-flow: row | column | dense;


```
# Repeat

| Title    | place explicit grid    | align                              | gap                   | order=z-index  | place implicit grid          | relation           |
| -------- | ---------------------- |----------------------------------- | --------------------- | -------------- | ---------------------------- | ------------------ |
| Wrapper  | grid-template          | justify/align -items               | gap & row/column -gap |                | grid-auto - rows/column/flow | grid-template-area |
| instance | grid-row & grid-column | align/justify -self & margin: auto |                       | (each)         |                              | grid-area          |


minmax(no-fr, 1fr) &
fitcontent(max-width) &
repeat(auto-fit, ...) &
grid without percent padding | margin
