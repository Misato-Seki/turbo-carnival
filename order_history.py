class OrderHistory:
    """
    ユーザーの注文履歴を管理するクラス
    """
    def __init__(self):
        """
        ユーザーごとに注文履歴を保存するための辞書を初期化します。
        """
        self.orders = {}  # ユーザーごとの注文履歴を保存する辞書

    def add_order(self, email, order):
        """
        新しい注文をユーザーの注文履歴に追加します。

        Args:
            email (str): ユーザーのメールアドレス。
            order (dict): 注文内容を含む辞書。
        """
        if email not in self.orders:
            self.orders[email] = []
        self.orders[email].append(order)

    def view_order_history(self, email):
        """
        ユーザーの過去の注文履歴を取得します。

        Args:
            email (str): ユーザーのメールアドレス。

        Returns:
            dict: 注文履歴が見つかった場合は、注文内容のリストを返します。
                  注文履歴がない場合はエラーメッセージを返します。
        """
        if email not in self.orders or len(self.orders[email]) == 0:
            return {"success": False, "error": "No orders found"}  # 注文履歴がない場合
        return {"success": True, "orders": self.orders[email]}  # 注文履歴がある場合

class UserProfile:
    """
    ユーザープロフィールを管理するクラス。
    注文履歴の表示機能を含む。
    """
    def __init__(self, email):
        """
        ユーザーのメールアドレスを設定し、注文履歴機能を利用できるようにします。
        """
        self.email = email
        self.order_history = OrderHistory()  # 注文履歴を管理するインスタンス

    def add_order(self, order):
        """
        ユーザーの注文履歴に新しい注文を追加します。
        
        Args:
            order (dict): 注文内容を含む辞書。
        """
        self.order_history.add_order(self.email, order)

    def view_order_history(self):
        """
        ユーザーの注文履歴を表示します。
        
        Returns:
            dict: 注文履歴が見つかればそれを返し、なければエラーメッセージを返します。
        """
        return self.order_history.view_order_history(self.email)
