from django.core.exceptions import ValidationError

def valid_extension(value):
    if (not value.name.endswith('.rar') and
        not value.name.endswith('.sb3') and
        not value.name.endswith('.sb2') and
        not value.name.endswith('.sb')):

        raise ValidationError("Archivos permitidos: .sb2, .sb, .rar")
