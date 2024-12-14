from rest_framework.exceptions import ValidationError
from datetime import datetime
import re


def validate_text(value):
    if re.search(r'<.*?>', value):
        raise ValidationError('HTML teglaridan foydalanishga yo‘l qo‘yilmaydi.')

    if re.search(r'(script|onload|onclick|onerror)', value, re.IGNORECASE):
        raise ValidationError('JavaScript kiritmalari taqiqlangan.')

    if re.search(r'[<>%$]', value):
        raise ValidationError('Maxsus belgilar (<>%$) kiritishga yo‘l qo‘yilmaydi.')

def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if re.match(email_regex, email):
        return True
    else:
        return False

def check_verify_code(user, code):
    verifies = user.verify_codes.filter(expration_time__gte=datetime.now(), code=code, is_confirmed=False)
    if not verifies.exists():
        data = {
            "message": "Verification code is invalid",
        }
        raise ValidationError(data)
    verifies.update(is_confirmed=True)
    return True

