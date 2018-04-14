Notifier {#Notifier}
========

Description
-----------

An event-handler object that tells the script to execute specified code
when a specified event occurs. For notifiers to work, they must be
enabled. See the \'notifiers enabled\' property of the Application
object. Events that occur within scripts do not generally trigger
notifiers, because they occur inside of a \"play script\" event.

### Properties

  ------------------------------------------------- -----------------------------------------------
  [event\<Notifier.event\>]{role="ref"} readonly    The event ID in four characters or a unique
                                                    string that the notifier is associated with.

  [eventClass\<Notifier.eventClass\>]{role="ref"}   The class ID associated with the event for the
  readonly                                          Notifier object, four characters or a unique
                                                    string.

  [eventFile\<Notifier.eventFile\>]{role="ref"}     The path to the file to execute when the event
  readonly                                          occurs/activates the notifier.

  [parent\<Notifier.parent\>]{role="ref"} readonly  The object\'s container.

  [typename\<Notifier.typename\>]{role="ref"}       The class name of the object.
  readonly                                          
  ------------------------------------------------- -----------------------------------------------

### Methods

  ----------------------------------------------- -----------------------
  [remove\<Notifier.remove\>]{role="ref"}         Deletes this object.
  readonly                                        

  [removeAll\<Notifier.removeAll\>]{role="ref"}   Deletes all elements.
  readonly                                        
  ----------------------------------------------- -----------------------

::: {.container .hide}
::: {.toctree}
Notifier/parent.rst Notifier/typename.rst Notifier/event.rst
Notifier/eventFile.rst Notifier/eventClass.rst

Notifier/remove.rst Notifier/removeAll.rst
:::
:::
