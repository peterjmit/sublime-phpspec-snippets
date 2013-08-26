# Sublime PhpSpec Snippets

Make writing [PhpSpec][1] a little less repetitive

## Installation 

Clone the repository into your `Packages/` folder

## Usage
Currently this plugin provides one command to help writing examples
with PhpSpec

### Complete example command
I hate typing underscores, and I wrote this command to ease that pain.

* Open the command panel and type "PhpSpec: complete example"
* Right click and select "PhpSpec: complete example"

The plugin will take the text from the current line and transform
it into a PhpSpec example

For example once you have your spec class you can write the following

```php
namespace spec;

use PhpSpec\ObjectBehavior;
use Prophecy\Argument;

class MarkdownSpec extends ObjectBehavior
{
    // ...

    converts plain text to html
}
```

With that line selected, if you run the command it will convert
the text to the following

 ```php
namespace spec;

use PhpSpec\ObjectBehavior;
use Prophecy\Argument;

class MarkdownSpec extends ObjectBehavior
{
    // ...

    function it_converts_plain_text_to_html()
    {

    }
}
```

Sublime text is lacking a plugin for PhpSpec so it would be 
great if some folks could contribute.

## TODO 
* Place cursor in correct position for generated example
* Snippets for creating a "it_" tempalte

[1]: http://phpspec.net
