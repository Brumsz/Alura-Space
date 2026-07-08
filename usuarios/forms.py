from django import forms

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label='Nome de Login', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )
    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-group',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro', 
        required=True, 
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: João Silva',
            }
        )
    )

    email = forms.EmailField(
        label='Email', 
        required=True, 
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: exemplo@gmail.com',
            }
        )
    )

    senha=forms.CharField(
        label='Senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua senha',
            }
        ),
    )

    senha_confirmada = forms.CharField(
        label='Confirmar senha', 
        required=True, 
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a sua novamente',
            }
        ),
    )

    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos neste espaço')
            else:
                return nome
    
    def clean_senha_confirmada(self):
         senha = self.cleaned_data.get('senha')
         senha_confirmada = self.cleaned_data.get('senha_confirmada')

         if senha != senha_confirmada:
              raise forms.ValidationError('Senhas não são iguais')
         else:
             return senha_confirmada
         

