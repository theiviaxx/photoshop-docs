.. _Socket:

================================================
Socket
================================================


Description
-----------

Creates a TCP/IP connection, or establishes a TCP/IP server.




Properties
^^^^^^^^^^

+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`connected<Socket.connected>` readonly | When true, the connection is active.                                                     |
+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`encoding<Socket.encoding>` readonly   | Sets or retrieves the name of the encoding used to transmit data.                        |
+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`eof<Socket.eof>` readonly             | When true, the receive buffer is empty.                                                  |
+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`error<Socket.error>` readonly         | A message describing the most recent error. Setting this value clears any error message. |
+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`host<Socket.host>` readonly           | The name of the remote computer when a connection is established.                        |
+---------------------------------------------+------------------------------------------------------------------------------------------+
| :ref:`timeout<Socket.timeout>` readonly     | The timeout in seconds to be applied to read or write operations.                        |
+---------------------------------------------+------------------------------------------------------------------------------------------+




Constructors
^^^^^^^^^^^^

+---------------------------------------+------------------------------+
| :ref:`Socket<Socket.Socket>` readonly | Creates a new Socket object. |
+---------------------------------------+------------------------------+


Methods
^^^^^^^

+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`close<Socket.close>` readonly     | Terminates the open connection.                                                                                                       |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`listen<Socket.listen>` readonly   | Instructs the object to start listening for an incoming connection.                                                                   |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`open<Socket.open>` readonly       | Opens the connection for subsequent read/write operations.                                                                            |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`poll<Socket.poll>` readonly       | Checks a listening object for a new incoming connection.                                                                              |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`read<Socket.read>` readonly       | Reads up to the specified number of characters from the connection. CR characters are ignored unless the encoding is set to "BINARY". |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`readln<Socket.readln>` readonly   | Reads one line of text up to the next line feed.                                                                                      |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`write<Socket.write>` readonly     | Concatenates all arguments into a single string and writes that string to the connection.                                             |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+
| :ref:`writeln<Socket.writeln>` readonly | Concatenates all arguments into a single string, appends a LF character, and writes that string to the connection.                    |
+-----------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------+






.. container:: hide

   .. toctree::
      :hidden:
      :maxdepth: 1

      Socket/host.rst
      Socket/encoding.rst
      Socket/error.rst
      Socket/eof.rst
      Socket/connected.rst
      Socket/timeout.rst
      
      

      Socket/open.rst
      Socket/listen.rst
      Socket/close.rst
      Socket/read.rst
      Socket/readln.rst
      Socket/write.rst
      Socket/writeln.rst
      Socket/poll.rst
      
      
      
      Socket/Socket.rst
      