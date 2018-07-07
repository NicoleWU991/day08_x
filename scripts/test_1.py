import allure


class Test_c:
    @allure.step(title='first test')
    def test_01(self):
        print('this is my first item')
        assert True
    def test_02(self):
        print('this is second item')
        assert False