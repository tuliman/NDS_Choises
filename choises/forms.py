from django import forms
from .models import Objects


class ObjectsForm(forms.ModelForm):
    class Meta:
        model = Objects
        fields = '__all__'

    def clean_value(self):
        cd = self.cleaned_data

        data = cd['value'].replace(',', '.')
        if data.replace('.', '').isdigit() and (data[-3] == ',' or data[-3] == '.' or data[-2] == ',' or
                                                data[-2] == '.'):
            return data
        else:
            raise forms.ValidationError('Строка не состоит из цифр или имеет неправильные разделители, список '
                                        'разделителей(. или ,) Копееек не может быть болше 100 ')

    def clean_nds_value(self):
        cd = self.cleaned_data
        if cd['nds_value'] > 100 or cd['nds_value'] < 0:
            raise forms.ValidationError('Должно возвращаться положительное чисто не больше 100%')
        else:
            return cd['nds_value']
