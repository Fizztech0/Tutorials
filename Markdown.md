# Markdown
> Find the original content here: https://learnxinyminutes.com/docs/markdown/
> 
> © 2021 [Dan Turkel](http://danturkel.com/), [Jacob Ward](http://github.com/JacobCWard/)
## HTML Elements

<!--This means we can use HTML elements in Markdown, such as the comment 
element, and they won't be affected by a markdown parser. However, if you 
create an HTML element in your markdown file, you cannot use markdown syntax 
within that element's contents.-->

## Headings

># This is an <h1>
>## This is an <h2>
>### This is an <h3>
>#### This is an <h4>
>##### This is an <h5>
>###### This is an <h6>
>
>This is an h1
>=============
>
>This is an h2
>-------------

## Simple text styles

>*This text is in italics.*
>_And so is this text._
>
>**This text is in bold.**
>__And so is this text.__
>
>***This text is in both.***
>**_As is this!_**
>*__And this!__*
>
>~~This text is rendered with strikethrough.~~

## Paragraphs

>This is a paragraph. I'm typing in a paragraph isn't this fun?
>
>Now I'm in paragraph 2.
>I'm still in paragraph 2 too!
>
>
>I'm in paragraph three!

Should you ever want to insert an HTML <br /> tag, you can end a paragraph with two or more spaces and then begin a new paragraph.
>I end with two spaces (highlight me to see them).
>
>There's a <br /> above me!

Block quotes are easy and done with the > character.

> This is a block quote. You can either
> manually wrap your lines and put a `>` before every line or you can let your lines get really long and wrap on their own.
> It doesn't make a difference so long as they start with a `>`.

> You can also use more than one level
>> of indentation?
> How neat is that?

## Lists

Unordered lists can be made using asterisks, pluses, or hyphens.

>* Item
>* Item
>* Another item
>
>or
>
>+ Item
>+ Item
>+ One more item
>
>or
>
>- Item
>- Item
>- One last item

Ordered lists are done with a number followed by a period.

>1. Item one
>2. Item two
>3. Item three

You don’t even have to label the items correctly and Markdown will still render the numbers in order, but this may not be a good idea.

>1. Item one
>1. Item two
>1. Item three

(This renders the same as the above example)

You can also use sublists

>1. Item one
>2. Item two
>3. Item three
>    * Sub-item
>    * Sub-item
>4. Item four

There are even task lists. This creates HTML checkboxes.

>Boxes below without the 'x' are unchecked HTML checkboxes.
>- [ ] First task to complete.
>- [ ] Second task that needs done
>This checkbox below will be a checked HTML checkbox.
>- [x] This task has been completed

## Code Blocks
You can indicate a code block (which uses the \<code\> element) by indenting a line with four spaces or a tab.

    This is code
    So is this
You can also re-tab (or add an additional four spaces) for indentation inside your code

    my_array.each do |item|
        puts item
    end
Inline code can be created using the backtick character `

>John didn't even know what the `go_to()` function did!

In GitHub Flavored Markdown, you can use a special syntax for code

```ruby
def foobar
    puts "Hello world!"
end
```

The above text doesn’t require indenting, plus GitHub will use syntax highlighting of the language you specify after 
the “`

## Horizontal rule

Horizontal rules (\<hr/\>) are easily added with three or more asterisks or hyphens, with or without spaces.

>***
>---
>- - -
>****************

## Links

One of the best things about markdown is how easy it is to make links. Put the text to display in hard brackets [] followed by the url in parentheses ()

>[Click me!](http://test.com/)

You can also add a link title using quotes inside the parentheses.

>[Click me!](http://test.com/ "Link to Test.com")

Relative paths work too.

>[Go to music](/music/).

Markdown also supports reference style links.

>[Click this link][link1] for more info about it!
>
>[Also check out this link][foobar] if you want to.
>
>[link1]: http://test.com/ "Cool!"
>[foobar]: http://foobar.biz/ "Alright!"

The title can also be in single quotes or in parentheses, or omitted entirely. The references can be anywhere in your
document and the reference IDs can be anything so long as they are unique.

There is also "implicit naming” which lets you use the link text as the id.

>[This][] is a link.
>
>[this]: http://thisisalink.com/

But it’s not that commonly used.

## Images

Images are done the same way as links but with an exclamation point in front!

>![This is the alt-attribute for my image](http://imgur.com/myimage.jpg "An optional title")

And reference style works as expected.

>![This is the alt-attribute.][myimage]

[myimage]: relative/urls/cool/image.jpg "if you need a title, it's here"

## Miscellany

### Auto-links

><http://testwebsite.com/> is equivalent to
> 
>[http://testwebsite.com/](http://testwebsite.com/)

### Auto-links for emails
><foo@bar.com>

### Escaping characters
>I want to type *this text surrounded by asterisks* but I don't want it to be
>in italics, so I do this: \*this text surrounded by asterisks\*.

### Keyboard keys
In GitHub Flavored Markdown, you can use a \<kbd\> tag to represent keyboard keys.

>Your computer crashed? Try sending a
><kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Del</kbd>

### Tables
Tables are only available in GitHub Flavored Markdown and are slightly cumbersome, but if you really want it:

| Col1         | Col2     | Col3          |
| :----------- | :------: | ------------: |
| Left-aligned | Centered | Right-aligned |
| blah         | blah     | blah          |

or, for the same results

Col 1 | Col2 | Col3
:-- | :-: | --:
Ugh this is so ugly | make it | stop

For more info, check out John Gruber’s official post of syntax 
[here](http://daringfireball.net/projects/markdown/syntax) and Adam Pritchard’s great cheatsheet 
[here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet).
---
Originally contributed by Dan Turkel, and updated by 
[11 contributor(s)](https://github.com/adambard/learnxinyminutes-docs/blame/master/markdown.html.markdown).

---
© 2021 [Dan Turkel](http://danturkel.com/), [Jacob Ward](http://github.com/JacobCWard/)