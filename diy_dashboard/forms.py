from django import forms
from .models import Trade

class TradeForm(forms.ModelForm):
    class Meta:
        model = Trade
        fields = [
        	'symbol', 'entry_date', 'strategy', 'quantity', 'entry_price', 
            'risk', 'target', 'exit_price', 'exit_date', 'exit_reason', 
            'profit_loss', 'percent_change',
        ]
        widgets = {
        	'symbol': forms.TextInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder": "Enter symbol",
        		}),
        	'entry_date': forms.DateInput(
        		attrs={
        			"class":	"form-control date",
                    "placeholder": "Enter entry date",
        		}),
        	'strategy': forms.TextInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder": "Enter strategy",
        		}),
        	'quantity': forms.NumberInput(
        		attrs={
        			"class":	"form-control",
                    "placeholder": "Enter quantity",
                    "min": 1,
        		}),
            'entry_price': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter entry price",
                }),
            'risk': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter risk",
                }),
            'target': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter target",
                }),
            'exit_price': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter exit price",
                }),
            'exit_date': forms.DateInput(
                attrs={
                    "class":    "form-control date",
                    "placeholder": "Enter exit date",
                }),
            'exit_reason': forms.Textarea(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter exit reason",
                }),
            'profit_loss': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter profit/loss",
                }),
            'percent_change': forms.NumberInput(
                attrs={
                    "class":    "form-control",
                    "placeholder": "Enter percent change",
                }),
        }
