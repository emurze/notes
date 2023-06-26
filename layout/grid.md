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
grid-auto-flow: row | column | dense;

gap: 20px;
row-gap: 20px | 20%;
column-gap: 20px;

align-items: stretch;
justify-items: stretch;


instance

grid-area: header;

grid-row: 1 / 2:
grid-row-start: auto;
grid-row-end: auto;

grid-column: 1 - start line / 2 - end line;
grid-column-start: auto;
grid-column-end: auto | span 2 | 2;

order: 1; - must have each element

align-self: stretch;
justify-self: stretch;

margin: auto; - center


minmax(no-fr, 1fr)
fitcontent - auto with max-width
repeat(3, 1fr)
repeat(auto-fit, minmax(250px, 1fr))


padding | margin must be without percent for browser compatibility
margin works without collapse

implicit and explicit instances

row - bottom -> up
column - left -> right

you can set and use grid-titles [row2 - title] 1fr

```
