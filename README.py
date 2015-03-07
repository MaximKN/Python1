################ Sockets #######################
First run the server using,
    python server.py &
This will bind to the localhost and listen on a specific port.

Then run the client using,
    python client.py

The client will then sent the OpenMath objects to the server to be processed.
Once processed the server will return the value.



################# Simplify function ##################
The simplify function takes in an OpenMath document and simplifies it into
a more compact OpenMath document where it can. To run,
    ./simplify.py -i infile -o output
The -i flag denotes the input file to be simplified.
The -o flag denotes the output file which the simplified OpenMath document will be saved in.
