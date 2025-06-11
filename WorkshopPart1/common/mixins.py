class ReadOnlyMixin:
    def __int__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)

        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
            field.widget.attrs['disabled'] = True