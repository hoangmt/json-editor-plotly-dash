# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class ReactJSONEditor(Component):
    """A ReactJSONEditor component.


Keyword arguments:
- className (string; optional)
- json (list | dict; required)
- height (number; optional)
- width (number; optional)
- escapeUnicode (boolean; optional)
- sortObjectKeys (boolean; optional)
- history (boolean; optional)
- mode (a value equal to: 'tree', 'view', 'form', 'code', 'text'; optional)
- name (string; optional)
- schema (dict; optional)
- search (boolean; optional)
- indentation (number; optional)
- theme (string; optional)

Available events: """
    @_explicitize_args
    def __init__(self, className=Component.UNDEFINED, json=Component.REQUIRED, height=Component.UNDEFINED, width=Component.UNDEFINED, onChange=Component.UNDEFINED, onEditable=Component.UNDEFINED, onError=Component.UNDEFINED, onModeChange=Component.UNDEFINED, escapeUnicode=Component.UNDEFINED, sortObjectKeys=Component.UNDEFINED, history=Component.UNDEFINED, mode=Component.UNDEFINED, name=Component.UNDEFINED, schema=Component.UNDEFINED, search=Component.UNDEFINED, indentation=Component.UNDEFINED, theme=Component.UNDEFINED, **kwargs):
        self._prop_names = ['className', 'json', 'height', 'width', 'escapeUnicode', 'sortObjectKeys', 'history', 'mode', 'name', 'schema', 'search', 'indentation', 'theme']
        self._type = 'ReactJSONEditor'
        self._namespace = 'json_dash'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['className', 'json', 'height', 'width', 'escapeUnicode', 'sortObjectKeys', 'history', 'mode', 'name', 'schema', 'search', 'indentation', 'theme']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in ['json']:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(ReactJSONEditor, self).__init__(**args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('ReactJSONEditor(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'ReactJSONEditor(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
