PAGE_URL: str = 'https://stellarburgers.nomoreparties.site'

RESTORE_PASSWORD_TEXT = 'Восстановление пароля'

USER_MAIL = '1q2w3e@yandex.ru'

ORDERS_LINE_TEXT = 'Лента заказов'

INGRIDIENTS_EXPECTED_TEXT = 'Детали ингредиента'

CONSTRUCT_TEXT = 'Соберите бургер'

USER_PASS = "1q2w3e"

ORDER_TEXT_EXPECTED_TEXT = '9999'

SCRIPT_TEXT = """
        var source = arguments[0];
        var target = arguments[1];
        var evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        target.dispatchEvent(evt);
        evt = document.createEvent("DragEvent");
        evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
        source.dispatchEvent(evt);
        """
