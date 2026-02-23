# Exhaustive Markdown Rendering Test

## 1. Headings

# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

Setext Heading 1
=================

Setext Heading 2
-----------------

####### Not a heading (7 levels)

## Heading with `inline code` and **bold** and *italic*

## Heading with [a link](https://example.com)

#  Heading with extra leading spaces

## 2. Emphasis & Inline Formatting

This is **bold text** and this is __also bold__.

This is *italic text* and this is _also italic_.

This is ***bold and italic*** and this is ___also bold and italic___.

This is **_bold with nested italic_** and *__italic with nested bold__*.

This is ~~strikethrough~~ text.

This is ~~**strikethrough bold**~~ and ~~*strikethrough italic*~~.

This is ~~***strikethrough bold italic***~~.

Mid**word**bold and mid*word*italic.

Multiple **bold** words **in** one **line**.

Underscores_in_the_middle_of_words should not italicize.

But _single underscores around words_ should italicize.

**Bold text that spans
across multiple lines**

## 3. Inline Code

Use `console.log()` for debugging.

Use `` `backtick` `` inside inline code (double backticks).

Use ``` `` ``` triple backticks to show double backticks.

Inline code with special chars: `<div class="test">&amp;</div>`

`code at start` of line and at `end of line`

A very long inline code: `const reallyLongVariableName = someFunction(parameter1, parameter2, parameter3, parameter4, parameter5)`

## 4. Code Blocks

```javascript
function hello() {
  console.log('Hello, world!')
  return 42
}
```

```python
def fibonacci(n):
    """Calculate fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

```sql
SELECT u.name, COUNT(*) AS total
FROM "users" u
JOIN "orders" o ON u.id = o.user_id
WHERE u.active = true
GROUP BY u.name
HAVING COUNT(*) > 5
ORDER BY total DESC;
```

```
Plain code block with no language specified
  preserving   whitespace   and   indentation
    line 3
```

```json
{
  "key": "value",
  "number": 42,
  "nested": {
    "array": [1, 2, 3],
    "null": null,
    "boolean": true
  }
}
```

    Indented code block (4 spaces)
    This is an older code block syntax
    Some renderers handle this differently

```
Code block with empty lines:

Line after empty line

Another line after empty line
```

```html
<!-- HTML code with special characters -->
<div class="container">
  <p>Hello &amp; goodbye</p>
  <img src="test.png" alt="<test>" />
</div>
```

## 5. Links

[Basic link](https://example.com)

[Link with title](https://example.com "Example Title")

[Link with **bold** text](https://example.com)

[Link with `code` text](https://example.com)

<https://autolinked-url.com>

<user@example.com>

[Reference-style link][ref1]

[Reference link with number][1]

[Link using definition as text][]

[ref1]: https://example.com "Reference 1"
[1]: https://example.com/numbered
[Link using definition as text]: https://example.com/self-ref

Bare URL (GFM autolink): https://www.example.com/path?query=value&other=123#anchor

Adjacent links: [link1](https://example.com) [link2](https://example.com)

Link with parentheses in URL: [Wikipedia](https://en.wikipedia.org/wiki/Markdown_(software))

## 6. Images

![Alt text for image](https://via.placeholder.com/150 "Image title")

![](https://via.placeholder.com/100)

[![Image as link](https://via.placeholder.com/100)](https://example.com)

![Very long alt text that describes the image in great detail for accessibility purposes](https://via.placeholder.com/200)

## 7. Unordered Lists

- Item 1
- Item 2
- Item 3

* Asterisk item 1
* Asterisk item 2

+ Plus item 1
+ Plus item 2

- Level 1
  - Level 2
    - Level 3
      - Level 4
        - Level 5

- Item with **bold**
- Item with *italic*
- Item with `code`
- Item with [link](https://example.com)
- Item with ~~strikethrough~~

## 8. Ordered Lists

1. First item
2. Second item
3. Third item

1. All starting with 1
1. Renderer should auto-number
1. These correctly

0. Starting with zero
1. Then one

10. Starting at ten
11. Eleven
12. Twelve

1. Level 1
   1. Level 2
      1. Level 3
         1. Level 4

1. Item with **bold** and *italic*
2. Item with `inline code`
3. Item with [a link](https://example.com)

## 9. Mixed & Complex Lists

1. Ordered parent
   - Unordered child
   - Another unordered child
     1. Back to ordered
     2. Second ordered

- Unordered parent
  1. Ordered child
  2. Another ordered child
     - Back to unordered

- List item with multiple paragraphs

  This is the second paragraph under the same list item.

  And a third paragraph.

- Next list item

1. Ordered item with a code block:

   ```python
   print("code inside list")
   ```

2. Next item after code block

- Item with a blockquote:

  > This is a blockquote inside a list item

- Next item

## 10. Task Lists

- [ ] Unchecked task
- [x] Checked task
- [ ] Another unchecked task
- [x] Another checked task

- [ ] Task with **bold text**
- [x] Task with `inline code`
- [ ] Task with [a link](https://example.com)

1. [ ] Ordered task list
2. [x] Checked ordered task
3. [ ] Third ordered task

- [ ] Parent task
  - [ ] Sub-task 1
  - [x] Sub-task 2
  - [ ] Sub-task 3

## 11. Blockquotes

> Simple blockquote

> Blockquote with **bold**, *italic*, and `code`.

> Multi-line blockquote
> that continues on the next line
> and the line after that.

> Blockquote with multiple paragraphs.
>
> Second paragraph in blockquote.
>
> Third paragraph in blockquote.

> Nested blockquote level 1
>> Nested blockquote level 2
>>> Nested blockquote level 3

> Blockquote with a list:
> - Item 1
> - Item 2
> - Item 3

> Blockquote with code:
> ```python
> print("hello from blockquote")
> ```

> Blockquote with a heading:
> ### Heading inside blockquote

> **Note:** This is a styled callout-like blockquote with bold prefix.

## 12. Horizontal Rules

Above the rule

---

Between rules

***

Another rule style

___

Below all rules

## 13. Tables

| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

| Left Aligned | Center Aligned | Right Aligned |
|:------------|:-------------:|-------------:|
| Left        |    Center     |        Right |
| Data        |     Data      |         Data |

| Feature | Supported | Notes |
|---------|-----------|-------|
| **Bold** | Yes | `works` |
| *Italic* | Yes | [link](https://example.com) |
| ~~Strike~~ | Yes | |
| `Code` | Yes | |

| Single Column |
|--------------|
| Row 1        |
| Row 2        |

| One | Two | Three | Four | Five | Six | Seven | Eight |
|-----|-----|-------|------|------|-----|-------|-------|
| a | b | c | d | e | f | g | h |

| Sparse |  | Table |
|--------|--|-------|
|        |  | Only this cell has content |
| Data   |  |       |

| Column with a very long header name | Short |
|--------------------------------------|-------|
| data | data |

| Pipe in cell | Result |
|-------------|--------|
| Use `\|` to escape | Works |

## 14. Footnotes

Here is a simple footnote[^1].

Here is a footnote with a long label[^long-label].

Multiple references to the same footnote[^1] appear correctly[^1].

Footnote inside **bold text[^2]** and *italic text[^3]*.

[^1]: This is the first footnote.
[^long-label]: This is a footnote with a longer label name.
[^2]: Footnote referenced from bold text.
[^3]: Footnote referenced from italic text.

## 15. Math (KaTeX)

Inline math: $E = mc^2$ and $a^2 + b^2 = c^2$

$$
\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
$$

$$
\begin{bmatrix}
a & b \\
c & d
\end{bmatrix}
\begin{bmatrix}
x \\
y
\end{bmatrix}
=
\begin{bmatrix}
ax + by \\
cx + dy
\end{bmatrix}
$$

Inline: $\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$

$$
f(x) = \begin{cases}
x^2 & \text{if } x \geq 0 \\
-x^2 & \text{if } x < 0
\end{cases}
$$

$$\lim_{x \to \infty} \frac{1}{x} = 0$$

Invalid math that should not crash: $\invalidcommand{test}$

Dollar signs that are not math: The price is $5 and $10.

## 16. HTML Content

<div>This is raw HTML that should be shown as text for safety</div>

<details>
<summary>Collapsible section</summary>
Content that GitHub would show in a collapsible.
</details>

<kbd>Ctrl</kbd> + <kbd>C</kbd>

<sub>subscript</sub> and <sup>superscript</sup>

<mark>highlighted text</mark>

Text with <br> a line break tag.

<table><tr><td>HTML table</td></tr></table>

## 17. Escape Characters

\*Not italic\*

\*\*Not bold\*\*

\# Not a heading

\- Not a list item

\[Not a link\](https://example.com)

\`Not code\`

Backslash: \\

Special characters: \~ \| \{ \} \( \) \. \!

## 18. Line Breaks & Whitespace

This line has two trailing spaces
so it should have a line break.

This line has a backslash\
line break (GFM).

This is one paragraph
that should be on the same line.

This is paragraph one.

This is paragraph two (separated by blank line).

## 19. Special Characters & Entities

HTML entities: &amp; &lt; &gt; &quot; &copy; &reg; &trade;

Unicode: — – … © ® ™ • § ¶ † ‡ ° ± × ÷

Emoji (native): 😀 🚀 ✅ ❌ ⚠️ 📝 🔗 💡

Emoji shortcodes (GFM): :smile: :rocket: :white_check_mark:

Smart quotes: "double" and 'single'

Arrows: → ← ↑ ↓ ↔ ⇒ ⇐

## 20. Edge Cases & Stress Tests

### Empty elements
-
>
```
```

### Single character elements
- a
> b

**x**

*y*

### Consecutive block elements

# Heading immediately followed by

> A blockquote immediately followed by

---

- A list immediately followed by

| Table |
|-------|
| cell  |

### Deeply nested content

> > > > > Five levels of blockquote nesting

- - - - - Five levels of list nesting (may not render correctly)

### Long unbroken text

Thisisaverylongwordthathasnospacesandshouldtesthowtherenderinghandlesoverfloworverywidecontent_abcdefghijklmnopqrstuvwxyz0123456789

### Adjacent formatting

**bold***italic*`code`~~strike~~**bold again**

### Incomplete/malformed markdown

**unclosed bold

*unclosed italic

[unclosed link(https://example.com

`unclosed code

```
unclosed code block

### Just a URL on its own line

https://www.example.com/standalone-url

### Trailing/leading whitespace in elements

**  bold with inner spaces  **

*  italic with inner spaces  *

### Mixed content paragraph

This paragraph has **bold**, *italic*, ~~strikethrough~~, `inline code`, a [link](https://example.com), a footnote[^1], math $x^2$, and an image ![img](https://via.placeholder.com/20) all in one line.

### Zero-width and special Unicode

Zero-width space: [​] (between brackets)
Zero-width joiner: [‍] (between brackets)
Right-to-left mark: [‏] (between brackets)

### Numbered list restart

1. First list, item 1
2. First list, item 2

Some text between lists.

1. Second list, item 1 (should restart at 1)
2. Second list, item 2

### Table with no body

| Header Only |
|-------------|

### Paragraph-level line breaks

First line
Second line (soft break, should be same paragraph)

First line
Second line (hard break with trailing spaces)
