class Aspect:
    """
    アスペクト比の計算
    16:9 : ハイビジョン
    3:2 : フィルムカメラ
    4:3 : アカデミー比
    2:1 : スコープ・サイズ
    1:1.618 : 黄金比
    1:1.414 : 白銀比
    result_dict : 全ての比率を格納するdict
    """

    result_dict = {}
    # Stable Diffusion用に8で割り切れす画像サイズ
    result_divisible8 = {}

    aspect_size = {
        "without_change" : "without_change",
        "square" : "1:1",
        "hi_vision_ratio" : "16:9",
        "camera_ratio" : "3:2",
        "academy_ratio" : "4:3",
        "scope_ratio" : "2:1",
        "golden_ratio" : "1:1.618",
        "silver_ratio" : "1:1.414",

        "swap_hi_vision_ratio" : "9:16",
        "swap_camera_ratio" : "2:3",
        "swap_academy_ratio" : "3:4",
        "swap_scope_ratio" : "1:2",
        "swap_golden_ratio" : "1.618:1",
        "swap_silver_ratio" : "1.414:1"
    }

    without_change = "without_change"
    square = "1:1"
    hi_vision_ratio = "16:9"
    camera_ratio = "3:2"
    academy_ratio = "4:3"
    scope_ratio = "2:1"
    golden_ratio = "1:1.618"
    silver_ratio = "1:1.414"

    swap_hi_vision_ratio = "9:16"
    swap_camera_ratio = "2:3"
    swap_academy_ratio = "3:4"
    swap_scope_ratio = "1:2"
    swap_golden_ratio = "1.618:1"
    swap_silver_ratio = "1.414:1"

    def __init__(self, width=512, height=512):
        """初期値

        Args:
            width (int, optional): 横幅. Defaults to 0.
            height (int, optional): 縦幅. Defaults to 0.

        widthを0にしていないとwidthが優先されます
        """
        self.width = width
        self.height = height

        self.width_resize = 0
        self.height_resize = 0

    def result(self, ratio, width_ratio, height_ratio):

        if self.worh():
            self.height = round(self.width * width_ratio)
            Aspect.result_dict.update({f"{ratio}":{"width" : self.width,"height" : self.height}})

            self.resize8()
            Aspect.result_divisible8.update({f"{ratio}":{"width" : self.width_resize,"height" : self.height_resize}})
            return Aspect.result_dict, Aspect.result_divisible8
        else:
            self.width = round(self.height * height_ratio)
            Aspect.result_dict.update({f"{ratio}":{"width" : self.width,"height" : self.height}})
            
            self.resize8()
            Aspect.result_divisible8.update({f"{ratio}":{"width" : self.width_resize,"height" : self.height_resize}})
            return Aspect.result_dict, Aspect.result_divisible8

    def withoutChange(self):
        """入力値そのままのサイズ
        
        """
        return Aspect.result_dict.update({f"{Aspect.without_change}":{"width" : self.width,"height" : self.height}})
        # return self.result(ratio="without_change", width_ratio=1, height_ratio=1)

    def w1h1(self, ratio="1:1", width_ratio=(1 / 1), height_ratio=(1 / 1)):
        """正方形
        1:1
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def w16h9(self, ratio="16:9", width_ratio=(9 / 16), height_ratio=(16 / 9)):
        """横長
        16:9
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def w3h2(self, ratio="3:2", width_ratio=(2 / 3), height_ratio=(3 / 2)):
        """横長
        3:2
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def w4h3(self, ratio="4:3", width_ratio=(3 / 4), height_ratio=(4 / 3)):
        """横長
        4:3
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def w2h1(self, ratio="2:1", width_ratio=(1 / 2), height_ratio=(2 / 1)):
        """横長
        2:1
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def goldenRatio(self, ratio="1:1.618", width_ratio=(1 / 1.618), height_ratio=(1.618 / 1)):
        """横長
        1:1.618
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def silverRatio(self, ratio="1:1.414", width_ratio=(1 / 1.414), height_ratio=(1.414 / 1)):
        """横長
        1:1.414
        """
        return self.result(ratio=ratio, width_ratio=width_ratio, height_ratio=height_ratio)

    def resize8(self):
        def check(size):
            while True:
                if size % 8 == 0:
                    return size
                else:
                    size += 1

        self.width_resize = check(self.width)
        self.height_resize = check(self.height)

    def worh(self):
        if self.width != 0:
            return True
        else:
            return False

    def all(self):
        """すべて
        """
        self.withoutChange()
        self.w1h1()
        self.w16h9()
        self.w3h2()
        self.w4h3()
        self.w2h1()
        self.goldenRatio()
        self.silverRatio()

        self.w16h9(ratio="9:16", width_ratio=(16 / 9), height_ratio=(9 / 16))
        self.w3h2(ratio="2:3", width_ratio=(3 / 2), height_ratio=(2 / 3))
        self.w4h3(ratio="3:4", width_ratio=(4 / 3), height_ratio=(3 / 4))
        self.w2h1(ratio="1:2", width_ratio=(2 / 1), height_ratio=(1 / 2))
        self.goldenRatio(ratio="1.618:1", width_ratio=(1.618 / 1), height_ratio=(1 / 1.618))
        self.silverRatio(ratio="1.414:1", width_ratio=(1.414 / 1), height_ratio=(1 / 1.414))

    def w2hAll(self):
        """横長
        """
        self.withoutChange()
        self.w1h1()
        self.w16h9()
        self.w3h2()
        self.w4h3()
        self.w2h1()
        self.goldenRatio()
        self.silverRatio()

    def t2wAll(self):
        """縦長
        """
        self.withoutChange()
        self.w16h9(ratio="9:16", width_ratio=(16 / 9), height_ratio=(9 / 16))
        self.w3h2(ratio="2:3", width_ratio=(3 / 2), height_ratio=(2 / 3))
        self.w4h3(ratio="3:4", width_ratio=(4 / 3), height_ratio=(3 / 4))
        self.w2h1(ratio="1:2", width_ratio=(2 / 1), height_ratio=(1 / 2))
        self.goldenRatio(ratio="1.618:1", width_ratio=(1.618 / 1), height_ratio=(1 / 1.618))
        self.silverRatio(ratio="1.414:1", width_ratio=(1.414 / 1), height_ratio=(1 / 1.414))
