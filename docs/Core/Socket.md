Socket {#Socket}
======

Description
-----------

Creates a TCP/IP connection, or establishes a TCP/IP server.

### Properties

  --------------------------------------------- -----------------------------------------------
  [connected\<Socket.connected\>]{role="ref"}   When true, the connection is active.
  readonly                                      

  [encoding\<Socket.encoding\>]{role="ref"}     Sets or retrieves the name of the encoding used
  readonly                                      to transmit data.

  [eof\<Socket.eof\>]{role="ref"} readonly      When true, the receive buffer is empty.

  [error\<Socket.error\>]{role="ref"} readonly  A message describing the most recent error.
                                                Setting this value clears any error message.

  [host\<Socket.host\>]{role="ref"} readonly    The name of the remote computer when a
                                                connection is established.

  [timeout\<Socket.timeout\>]{role="ref"}       The timeout in seconds to be applied to read or
  readonly                                      write operations.
  --------------------------------------------- -----------------------------------------------

### Constructors

  --------------------------------------- ------------------------------
  [Socket\<Socket.Socket\>]{role="ref"}   Creates a new Socket object.
  readonly                                
  --------------------------------------- ------------------------------

### Methods

  ----------------------------------------- ------------------------------------------------------
  [close\<Socket.close\>]{role="ref"}       Terminates the open connection.
  readonly                                  

  [listen\<Socket.listen\>]{role="ref"}     Instructs the object to start listening for an
  readonly                                  incoming connection.

  [open\<Socket.open\>]{role="ref"}         Opens the connection for subsequent read/write
  readonly                                  operations.

  [poll\<Socket.poll\>]{role="ref"}         Checks a listening object for a new incoming
  readonly                                  connection.

  [read\<Socket.read\>]{role="ref"}         Reads up to the specified number of characters from
  readonly                                  the connection. CR characters are ignored unless the
                                            encoding is set to \"BINARY\".

  [readln\<Socket.readln\>]{role="ref"}     Reads one line of text up to the next line feed.
  readonly                                  

  [write\<Socket.write\>]{role="ref"}       Concatenates all arguments into a single string and
  readonly                                  writes that string to the connection.

  [writeln\<Socket.writeln\>]{role="ref"}   Concatenates all arguments into a single string,
  readonly                                  appends a LF character, and writes that string to the
                                            connection.
  ----------------------------------------- ------------------------------------------------------

::: {.container .hide}
::: {.toctree}
Socket/host.rst Socket/encoding.rst Socket/error.rst Socket/eof.rst
Socket/connected.rst Socket/timeout.rst

Socket/open.rst Socket/listen.rst Socket/close.rst Socket/read.rst
Socket/readln.rst Socket/write.rst Socket/writeln.rst Socket/poll.rst

Socket/Socket.rst
:::
:::
