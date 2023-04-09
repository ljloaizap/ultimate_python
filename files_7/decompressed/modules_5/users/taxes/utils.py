if __name__ != "__main__":

    # from ..management.crud import save # relative import
    from users.management.crud import save  # absolute import
    print(f'> {__name__}')

    def pay_taxes():
        print('> (From Utils) Paying taxes...')
        save()
else:
    print('> Maintenance tasks...')
