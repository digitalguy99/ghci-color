# Colorize GHCi

this script colorizes ghci output.

![screenshot](https://raw.github.com/rhysd/ghci-color/master/cap.jpg)

- initial message
- fundamental operator `+` `-` `*` `/`
- parentheses and blackets `()` `{}` `[]`
- double colon operator `::`
- arrow operator `->` `=>`

## Requirements

sed (stream editor) or PowerShell

## Installation

Clone the repository to local machine:

```
git clone https://github.com/rhysd/ghci-color.git
```

Put the script file in directory listed in `PATH` environment variable:

- [ghci-color](./ghci-color) for Mac/Linux
- [ghci-color.ps1](./ghci-color.ps1) for Windows

>If you are using Windows, run the following as well on your CLI:
>```cmd
>setx PATHEXT "%PATHEXT%;.PS1" /M
>```

Run `ghci-color` instead of ghci.

## License

This repository is distributed under the MIT license.

    Copyright (c) 2012 rhysd

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
    of the Software, and to permit persons to whom the Software is furnished to do so,
    subject to the following conditions:


    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
    INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
    PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
    LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR
    THE USE OR OTHER DEALINGS IN THE SOFTWARE.