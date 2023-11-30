from apis.utils.email_provider import EmailProvider, EmailServiceConfig
from apis.service import email


class EmailService:
    def __init__(self, to, template_id, template_values):
        self.to = to
        self.template_values = template_values
        self.template_id = template_id
        self.provider = EmailServiceConfig.MSG91.value

    def validate_provider(self):
        if self.provider == EmailProvider.MSG91.value:
            email.send_email_to_msg91(self)
            return True
        else:
            return {"status": False, "message": "Provider Not Integrated"}


def send_email(to, template_id, template_values):
    email_service = EmailService(to, template_id, template_values)
    email_service.validate_provider()
    return True
