from allauth.account.forms import ResetPasswordKeyForm
class MyCustomResetPasswordKeyForm(ResetPasswordKeyForm):

    def save(self):

        # Add your own processing here.
        print("testeS")
        print(self.user)
        # Ensure you call the parent class's save.
        # .save() does not return anything
        super(MyCustomResetPasswordKeyForm, self).save()