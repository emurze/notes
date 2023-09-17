# Naming structure

```

<header class="header">
  <nav class="header__menu"></nav>
</header>

<main class="main">
  <aside class="sidebar">        - independent block for filters, adds, secondary content
    <nav class="sidebar__menu">
    </nav>                       - dependent element for several main navigation "<ul><li><a>"
  </aside>
  <section class="content">
    <div class="content__title"></div> - must have
  </section>
  <article class="post">          - independent block (article, post, comment)
    <div class="post__title"></div> - must have
  </article>
</main>

<footer>
</footer>

<time></time>
<address></address> - contact

<div>
  <img>
  <img>
</div>

less - better
```

# Repeat

1. **header**, **footer**, **main**, **sidebar**, dependent **nav**
2. **section** with title - for content grouping, 
   **article** with title - independent can torn out without loss of meaning  
3. **time**, **address**
