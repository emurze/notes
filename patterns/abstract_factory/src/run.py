from factory import AdminFactory, BaseFactory, ClientFactory, ModeratorFactory


def client_code(factory: BaseFactory) -> None:
    user = factory.create_user()
    game = factory.create_game()

    print(user)
    print(game)


if __name__ == '__main__':
    client_code(ClientFactory())
    client_code(ModeratorFactory())
    client_code(AdminFactory())