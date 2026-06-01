# ============================================
# 题目33：面向对象实战——银行账户系统
# 知识点：综合运用类/继承/异常/property
# ============================================

from datetime import datetime
from abc import ABC, abstractmethod

# --- 自定义异常 ---
class BankError(Exception):
    pass

class InsufficientFundsError(BankError):
    def __init__(self, balance, amount):
        super().__init__(f"余额不足：余额 ¥{balance:.2f}，需要 ¥{amount:.2f}")
        self.balance = balance
        self.amount = amount

class InvalidAmountError(BankError):
    pass

# --- 交易记录 ---
class Transaction:
    def __init__(self, ttype, amount, balance_after, note=""):
        self.type = ttype
        self.amount = amount
        self.balance_after = balance_after
        self.note = note
        self.timestamp = datetime.now()

    def __str__(self):
        ts = self.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        sign = "+" if self.type == "存款" else "-"
        return (f"[{ts}] {self.type}: {sign}¥{self.amount:.2f} "
                f"-> 余额: ¥{self.balance_after:.2f}"
                + (f" ({self.note})" if self.note else ""))


# --- 抽象基类 ---
class Account(ABC):
    _account_counter = 1000

    def __init__(self, owner, initial_balance=0.0):
        Account._account_counter += 1
        self._account_id = f"ACC{Account._account_counter}"
        self._owner = owner
        self._balance = 0.0
        self._transactions = []

        if initial_balance > 0:
            self.deposit(initial_balance, "开户初始存款")

    @property
    def account_id(self):
        return self._account_id

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount, note=""):
        if amount <= 0:
            raise InvalidAmountError(f"存款金额必须为正数，收到：{amount}")
        self._balance += amount
        tx = Transaction("存款", amount, self._balance, note)
        self._transactions.append(tx)
        return tx

    def withdraw(self, amount, note=""):
        if amount <= 0:
            raise InvalidAmountError(f"取款金额必须为正数，收到：{amount}")
        self._check_withdraw(amount)
        self._balance -= amount
        tx = Transaction("取款", amount, self._balance, note)
        self._transactions.append(tx)
        return tx

    @abstractmethod
    def _check_withdraw(self, amount):
        pass

    def get_history(self, last_n=None):
        txs = self._transactions[-last_n:] if last_n else self._transactions
        return txs

    def print_statement(self):
        print(f"\n{'='*50}")
        print(f"账户: {self._account_id}  户主: {self._owner}")
        print(f"账户类型: {self.__class__.__name__}")
        print(f"当前余额: ¥{self._balance:.2f}")
        print(f"{'-'*50}")
        if not self._transactions:
            print("暂无交易记录")
        else:
            for tx in self._transactions:
                print(f"  {tx}")
        print(f"{'='*50}")

    def __str__(self):
        return f"{self.__class__.__name__}[{self._account_id}]({self._owner}, ¥{self._balance:.2f})"

    def __repr__(self):
        return str(self)


# --- 普通账户：余额不能为负 ---
class SavingsAccount(Account):
    def __init__(self, owner, initial_balance=0.0, interest_rate=0.025):
        self.interest_rate = interest_rate
        super().__init__(owner, initial_balance)

    def _check_withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)

    def apply_interest(self):
        interest = self._balance * self.interest_rate
        self.deposit(interest, f"年利息（{self.interest_rate:.1%}）")
        return interest


# --- 信用账户：允许透支 ---
class CreditAccount(Account):
    def __init__(self, owner, credit_limit=5000.0):
        self.credit_limit = credit_limit
        super().__init__(owner, 0.0)

    def _check_withdraw(self, amount):
        available = self._balance + self.credit_limit
        if amount > available:
            raise InsufficientFundsError(available, amount)

    @property
    def available_credit(self):
        return max(0, self.credit_limit + self._balance)


# --- 银行类 ---
class Bank:
    def __init__(self, name):
        self.name = name
        self._accounts = {}

    def open_account(self, account):
        self._accounts[account.account_id] = account
        print(f"[{self.name}] 开户成功：{account}")
        return account

    def get_account(self, account_id):
        if account_id not in self._accounts:
            raise BankError(f"账户不存在：{account_id}")
        return self._accounts[account_id]

    def transfer(self, from_id, to_id, amount):
        from_acc = self.get_account(from_id)
        to_acc = self.get_account(to_id)
        from_acc.withdraw(amount, f"转账至 {to_id}")
        to_acc.deposit(amount, f"来自 {from_id} 的转账")
        print(f"转账成功：{from_acc.owner} -> {to_acc.owner} ¥{amount:.2f}")

    def total_assets(self):
        return sum(a.balance for a in self._accounts.values() if a.balance > 0)

    def summary(self):
        print(f"\n{'='*50}")
        print(f"  {self.name} 汇总")
        print(f"{'='*50}")
        for acc in self._accounts.values():
            print(f"  {acc}")
        print(f"\n  总资产: ¥{self.total_assets():.2f}")


# --- 测试 ---
if __name__ == "__main__":
    bank = Bank("Python 银行")

    # 开户
    zhang = bank.open_account(SavingsAccount("张三", 1000))
    li = bank.open_account(SavingsAccount("李四", 500, interest_rate=0.03))
    vip = bank.open_account(CreditAccount("王五", credit_limit=10000))

    print(f"\n王五可用信用额度：¥{vip.available_credit:.2f}")

    # 操作
    zhang.deposit(500, "工资")
    zhang.withdraw(200, "购物")

    li.deposit(300, "奖金")
    interest = li.apply_interest()
    print(f"\n李四利息：¥{interest:.2f}")

    vip.withdraw(3000, "消费")
    print(f"王五透支后余额：¥{vip.balance:.2f}")
    print(f"王五剩余可用额度：¥{vip.available_credit:.2f}")

    # 转账
    bank.transfer(zhang.account_id, li.account_id, 300)

    # 错误处理
    try:
        zhang.withdraw(99999, "大额取款")
    except InsufficientFundsError as e:
        print(f"\n取款失败：{e}")

    # 打印账单
    zhang.print_statement()

    # 银行汇总
    bank.summary()
