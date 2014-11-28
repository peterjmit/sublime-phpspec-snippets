# Sublime PhpSpec Snippets

Make writing [PhpSpec][1] examples and matchers in your Specs a little easier in Sublime Text 2 & 3.

![PhpSpec snippet demo](http://i.imgur.com/OIlWwaa.gif)

## Installation 

This plugin is available as a [sublime package](https://sublime.wbond.net/packages/PhpSpec%20Snippets)
search for "PhpSpec Snippets".

Alternatively clone this repository into your `Packages/` folder.

## Usage
Currently this plugin provides a command to help writing examples
with PhpSpec and severals snippets to use.

### Complete example command
I hate typing underscores, and I wrote this command to ease that pain. It can be
accessed in two ways:

* Open the command panel and type "PhpSpec: complete example"
* Right click and select "PhpSpec: complete example"

The plugin will take the text from the current line and transform
it into a PhpSpec example. You can also create examples over multiple 
lines.

The snippet generator doesn't care if you include or leave out the 
`function` declaration and/or `it_`/`its_`, the generated example
will prepend those automatically.

### Shortcuts

#### SUS Constructor

`bct` BeConstructedThrough.

```php
beConstructedThrough('',array());

```

`bcw` BeConstructedWith.

```php
beConstructedWith();

```

#### Let & Let go

`let` Setup method for phpspec.

```php
function let()
{
}

```

`letgo` Teardown method for phpspec.

```php
function letgo()
{
}
```

#### Matchers

`sb` shouldBe.

```php
shouldBe();

```

`snb` shouldNotBe.

```php
shouldNotBe();

```

`sbi` shouldBeAnInstanceOf.

```php
shouldBeAnInstanceOf();

```

`snbi` shouldNotBeAnInstanceOf.

```php
shouldNotBeAnInstanceOf();

```

`sbl` shouldBeLike.

```php
shouldBeLike();

```

`snbl` shouldNotBeLike.

```php
shouldNotBeLike();

```

`se` shouldEqual.

```php
shouldBeEqual();

```

`sne` shouldNotEqual.

```php
shouldNotEqual();

```

`sht` shouldHaveType.

```php
shouldHaveType();

```

`snht` shouldNotHaveType.

```php
shouldNotHaveType();

```

`si` shouldImplement.

```php
shouldImplement();

```

`sni` shouldNotImplement.

```php
shouldNotImplement();

```

`sr` shouldReturn.

```php
shouldReturn();

```

`snr` shouldNotReturn.

```php
shouldNotReturn();

```

`st` shouldThrow.

```php
shouldThrow('')->during();

```

#### Stubs, Mocks and spies

`wr` willReturn.

```php
willReturn();

```

`wt` willThrow.

```php
willThrow();

```

`sbc` shouldBeCalled.

```php
shouldBeCalled();

```

`bnbc` shouldNotBeCalled.

```php
shouldNotBeCalled();

```

`bhbc` shouldHaveBeenCalled.

```php
shouldHaveBeenCalled();

```

`snhbc` shouldNotHaveBeenCalled.

```php
shouldNotHaveBeenCalled();

```


## TODO 
* Fix code for positioning cursor (it's a bit tempremental)

[1]: http://phpspec.net
