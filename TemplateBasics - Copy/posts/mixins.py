class ReadOnlyFieldsMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            self.fields[field].disabled = True
            field.widget.attrs['readonly'] = True