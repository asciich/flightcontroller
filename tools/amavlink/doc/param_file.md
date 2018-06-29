# Amavlink Param.files

To ensure reproducible settings on the flightcontroller [amavlink](readme.md) supports setting parameters from a param.file.

## Simple param file

The simpliest form of a param.file is a text value containing a PARAM_NAME, delimiter and the VALUE.
```#``` can be used for comments:

```bash
# This is a comment line
CH7_OPT=7
CH8_OPT : 8 # This sets CH8_OPT to 8
RC11_DZ, 0
```

## Supported delimiters

Currently these delimiters are supported:

* ```=```
* ```:```
* ```,```

## Markdown files

A param file can also be written as markdown file (like this example). 
Ensure all Paramaters are in betweekn code blocks and the code block is at the beginning of a line.
**Inline code blocks are not supported.**
Everything outside codeblocks is threated as comment and ignored:

```
# This is a comment line
CH7_OPT=7
CH8_OPT : 8 # This sets CH8_OPT to 8
RC11_DZ, 0
```

Code block lines without delimiter or spaces between words in the PARAM_NAME are ignored:

```bash
echo "Is ignored as there is no delimiter"
echo "a=b" # is ignored as there is a space in the PARAM_VALUE
ls # Is ignored as there is no delimiter
```

## Upload example 

To upload this file:

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --verify /params/param_file.md"
```

To verify this file:

```bash
docker run --net=host --rm -v $(pwd):/params -it asciich/amavlink sh -c "amavlink paramfile --verify /params/param_file.md"
```

