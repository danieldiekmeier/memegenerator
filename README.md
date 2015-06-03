# Python Meme Generator
## Bonus: Alfred-Workflow

## Introduction
This is a Meme-Generator for Python, using PIL (with FreeType). It can put captions at the top and the bottom of images.

## Requirements
To use the Meme Generator, you have to have Python (duh!) and PIL (Python Image Library) with working FreeType.

To use the Alfred-Workflow, you have to have Alfred2 with the Powerpack installed.

## Installation

Download or fork or whatever this Repository, it has everything you need. It even comes with a few meme templates to get you started.

If you want to use the Alfred2-Workflow, I'd advice you to put the `memegenerator`-Folder into `~/dev/` (because this is where the Workflow will look for the files. If you feel uncomfortable using `~/dev/`, you can just edit the paths in the Workflow according to your needs.

The Workflow also tries to start a Virtual Environment called "venv" before running the Script, because I assume you installed the PIL there and not globally.

Again, the Generator is not that complicated, if you do not want to use a Workflow, you can just change a few lines and you'll be alright.

To install the Alfred-Workflow, you just have to Open it.

## Command-Line Usage

The memegenerator.py uses images with the extension `.jpg` in the same folder it is in.

So, assuming the script is in using `~/dev/memegenerator/`, all the image files should be there, too.

For Example: If you wanted to create a Success Kid-Meme, you'd put a file `successkid.jpg` (with the empty template) into `~/dev/memegenerator/`. It's really not that hard.

If you want to use the Generator from the Command Line, you only put in `python memegenerator.py successkid "Top Caption" "Bottom Caption"`, hit Enter, and it will generate `temp.png` and save it to the same folder the Generator is located in.

The `temp.png` will have the same size as the template you put in. It will be overwritten the next time you use the Generator, so rename or move it, if you want to keep it.

### Arguments

The Generator takes several arguments and treats them as follows:

#### One Argument
``` bash
$ python memegenerator.py "Lorem Ipsum"
```
Launching the script with only one argument will fall back and use a template file called `standard.jpg`. This is intended as a shortcut if you primarily create one type of meme. The given Argument will be used as the bottom caption.

#### Two Arguments
``` bash
$ python memegenerator.py memetype "Lorem Ipsum"
```
This is similar to One Argument: The second Argument will be printed as the bottom caption on the meme template of your choosing.
#### Three Arguments
``` bash
$ python memegenerator.py memetype "Lorem Ipsum" "Dolor Sit"
```
This uses the second Argument as top caption, and the third as bottom caption.

The Memegenerator doesn't support more than three Arguments at the moment.

### Using the Alfred Workflow
The Workflow takes the same arguments as the script and works the same. As a bonus, it will open the `temp.png` with Preview.app, select everything, copy it to the clipboard and close Preview.app again.

Now you can paste the image into Messages, Tweetbot, Photoshop or any other App that supports this.

Using Applescript to open and close Preview, just to copy it to the Clipboard is a little messy, so if you have a better idea, send a pull request my way or open a ticket.

## API Usage

It is also possible to use memegenerator as an imported library. The memegenerator module has a single top-level method, `make_meme(topString, bottomString, filename)`. The first two arguments specify the text which will appear on the image. The final argument is the full filename to the source image to be used. A file with the name 'temp.png' will be placed into the current directory. If no text is required for the top (or bottom), pass in the empty string.

## Notes

Feel free to use, fork and improve, and send me Pull Requests if you think you really got something great that should be included here.
