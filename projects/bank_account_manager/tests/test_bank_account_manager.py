import pytest

from bank_account_manager import BankAccount


def test_initial_balance():
    account = BankAccount(100)
    assert account.balance == 100


def test_deposit_increases_balance():
    account = BankAccount(100)
    assert account.deposit(50) == 150
    assert account.balance == 150


def test_withdraw_decreases_balance():
    account = BankAccount(100)
    assert account.withdraw(40) == 60


@pytest.mark.parametrize("balance", [-1, -100])
def test_negative_initial_balance_raises_error(balance):
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(balance)


@pytest.mark.parametrize("amount", [0, -10])
def test_invalid_deposit_raises_error(amount):
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Deposit amount must be greater than zero"):
        account.deposit(amount)


@pytest.mark.parametrize("amount", [0, -10])
def test_invalid_withdrawal_raises_error(amount):
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Withdrawal amount must be greater than zero"):
        account.withdraw(amount)


def test_insufficient_balance_raises_error():
    account = BankAccount(100)
    with pytest.raises(ValueError, match="Insufficient balance"):
        account.withdraw(101)
