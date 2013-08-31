# Sublime PhpSpec Snippets

Make writing [PhpSpec][1] examples in your Specs a little easier in Sublime Text 2 & 3

![PhpSpec snippet demo](http://i.imgur.com/OIlWwaa.gif)

## Installation 

This plugin is available as a [sublime package](https://sublime.wbond.net/packages/PhpSpec%20Snippets)
search for "PhpSpec Snippets".

Alternatively clone this repository into your `Packages/` folder.

## Usage
Currently this plugin provides one command to help writing examples
with PhpSpec

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
will prepend those automatically


## TODO 
* Fix code for positioning cursor (it's a bit tempremental)

[1]: http://phpspec.net
