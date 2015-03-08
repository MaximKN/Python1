# _Python 1_

## Synopsis

This project provides support for OpenMath - an extensible standard for representing mathematical constructs. As such, these OpenMath objects can be passed around between various software applications in a system independant way. The project supports all basic OpenMath types and a few content directories.

## Code Example

We can swap between OpenMath and Python easily,
```
ParseOMstring('<OMOBJ> <OMI>42</OMI></OMOBJ>')

Output: 42
```

And vice versa:
```
OMprint(42)

Output:
<?xml version="1.0" ?>
<OMOBJ>
    <OMI>42</OMI>
</OMOBJ>
```

## API Reference

We follow the OpenMath documentation at: [www.openmath.org](www.openmath.org)

## Tests

To run some tests, type `python test.py`. This file extensively tests all OpenMath objects that we support.

## Sockets
First run the server using,
    `python server.py &`
This will bind to the localhost and listen on a specific port (50007).

Then run the client using,
    `python client.py`

The client will then sent the OpenMath objects to the server to be processed.
Once processed the server will return the value.

## Simplify function
The simplify function takes in an OpenMath document and simplifies it into
a more compact OpenMath document where it can. To run,
    `./simplify.py -i infile -o output`
The `-i flag` denotes the input file to be simplified.
The `-o flag` denotes the output file which the simplified OpenMath document will be saved in.


