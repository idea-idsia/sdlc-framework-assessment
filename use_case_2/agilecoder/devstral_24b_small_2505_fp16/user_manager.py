class UserRole:
    HELPDESK_USER = 1
    SIMPLE_USER = 2
class UserManager:
    def can_modify_ticket(self, user_role):
        if user_role == UserRole.HELPDESK_USER:
            return True
        return False