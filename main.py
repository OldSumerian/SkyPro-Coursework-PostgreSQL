from utils.utils import create_database, create_tables, fill_tables


def user_interface():
    db_name = input('Введите название создаваемой базы данных:\n')
    create_database(db_name)
    create_tables(db_name)
    fill_tables(db_name)


if __name__ == '__main__':
    user_interface()
