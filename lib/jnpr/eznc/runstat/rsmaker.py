from .view import RunstatView
from .rsmfields import RunstatMakerViewFields
from .table import RunstatTable

class RunstatMaker(object):
  """
  Metaclass builder for RunstatTable and RunstatView.  The RunstatMaker is a namespace
  class used to build the following items:

    GetTable
      creates a "toplevel" class object for "getting" Junos run-state information,
      e.g. get-interface-information, get-route-information, etc.

    Table
      creates a table definition, used when the run-state information has one or
      more tables within the response.

    View 
      create a table view definition. a view creates the mapping of user-defined
      field names (i.e. what *they* want) to the underlying Junos XML.  the view
      is the abstraction layer between Python and Junos/XML essentially.  the
      view is defined by a dictionary of fields.

    Fields 
      creates the field definitions that construct a view.
  """

  @classmethod
  def GetTable(cls, cmd, args=None, item=None, key=RunstatTable.NAME_XPATH, view=None, getter_name=None ):
    if getter_name is None: getter_name = "RunstatGetTable." + cmd
    new_cls = type(getter_name, (RunstatTable,), {} )
    new_cls.GET_RPC = cmd
    new_cls.GET_ARGS = args or {}
    new_cls.ITER_XPATH = item
    new_cls.NAME_XPATH = key 
    new_cls.VIEW = view
    new_cls.__module__ = __name__
    return new_cls

  @classmethod
  def Table(cls, item, key=RunstatTable.NAME_XPATH, view=None, table_name=None):
    if table_name is None: table_name = 'RunstatTable.' + item
    new_cls = type(table_name, (RunstatTable,), {} )
    new_cls.ITER_XPATH = item
    new_cls.NAME_XPATH = key 
    new_cls.VIEW = view
    new_cls.__module__ = __name__
    return new_cls

  @classmethod
  def View(cls, fields, view_name=None, **kvargs):
    """
    :fields: dictionary of fields
      recommend you use the :Fields: mechanism to create these
      rather than hardcoding the dictionary structures; since
      they might change over time.

    :view_name: to name the class (OPTIONAL)

    :kvargs:
        'groups' is a dict of name/xpath 
        @@@ document this more @@@

    """
    if view_name is None: view_name = 'RunstatView'
    new_cls = type(view_name, (RunstatView,), {})
    new_cls.FIELDS = fields
    new_cls.GROUPS = kvargs['groups'] if 'groups' in kvargs else None    
    new_cls.__module__ = __name__
    return new_cls

  @classmethod
  def Fields(cls):
    """ class method that wraps the object instance """
    return RunstatMakerViewFields()




