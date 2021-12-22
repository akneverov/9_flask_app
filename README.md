# 9_flask_app(creating microserver)

Сервис находится в файле [Flask.py](Flask.py) и запускается корректно.

![](./Screenshots/outcome.jpg)

При попытке воспользоваться запросом GET(получение информации о пользователях)[get_ex.py](get_ex.py) до регистрации первого пользователя выводится соответствующее уведомление.

![](./Screenshots/CheckBeforeReg.jpg)

Post запрос реализован в [reg_ex.py](reg_ex.py) и реализует регистрацию пользователей.

![](./Screenshots/SuccessReg1.jpg)
![](./Screenshots/SuccessReg2.jpg)

При попытке регистрации уже существующего пользователя выдает соответствующее уведомление.

![](./Screenshots/SameNameReg.jpg)

Get запрос реализован через вывод информации о зарегистрированных пользователях.

![](./Screenshots/GetResults.jpg)
