from datetime import date

from model import Wallet, Person, Base
# from common.base import session_factory

from sqlalchemy import create_engine
engine = create_engine('sqlite:///assignment2.db')
Base.metadata.create_all(engine)


def session_factory():
    from sqlalchemy.orm import sessionmaker
    DBSession = sessionmaker(bind=engine)
    return DBSession()


def create_wallets():
    session = session_factory()
    walletA = Wallet('0x12345', 1000, "345LKJHJFHLJHDIUSHidhjsdsdf37428")
    walletB = Wallet('0x12345', 2000, "345LKJHJFHLJHDadfyidhjsdsdf37428")
    session.add(walletA)
    session.add(walletB)
    session.commit()
    session.close()


# def create_wallets():
#     session = session_factory()
#     bruno = Person("Bruno Krebs", date(1984, 10, 20), 182, 84.5)
#     john = Person("John Doe", date(1990, 5, 17), 173, 90)
#     session.add(bruno)
#     session.add(john)
#     session.commit()
#     session.close()


def get_wallets():
    session = session_factory()
    wallet_query = session.query(Wallet)
    session.close()
    return wallet_query.all()


if __name__ == "__main__":
    wallets = get_wallets()
    if len(wallets) == 0:
        create_wallets()
    wallets = get_wallets()

    for wallet in wallets:
        print(wallet)
