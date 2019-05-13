from sentiment_classifier import LoadedModel

"""

You can copy-paste those reviews and test it in browser or just RUN model_test.py
It seems that short reviews likely be assigned as negative. I didn't check train data, but it seems every review got
a lot words. 

"""

test = LoadedModel()

positive = test.process("""Качество связи просто поражает после HTC - очень четкий и чистый звук, сигнал лучше! Купил в 
европе без русских букв - за неделю печатаю вслепую- клавиатура потрясающая! словарь подбора слов работает на пять с 
плюсом (в памяти остаются часто набираемые вами слова, любое слово печаю не более чем на треть - потом выбираю что 
предлагает система). Операционная система очень быстрая. по сути три блока - 1) hub куда сбрасываются все сообщения 
ваших почтовых ящиков, фейсбука, whаtsap ,sms, данные по входящим исходящим, оповещения о днях рождения из контакта. 
все это 
  сбрасывается в одну корзину! Это безумно удобно ни одного сообщения вы не пропустите! 2)все запущенные программы 
  3) меню установленных программ. Никаких зависаний, между любыми программами переходы без задержки моментальные! 
  единственное что - нехватает виджитов после HTC! Очень удобная система поиска по телефону - проводите пальцем вверх 
  по экрану( так он включается) потом можете напечатать sms или call и часть имени контакта. все телефон звонит адресату 
  или вы набираете сообщение. также можно найти любую программу, фотографию или файл сразу не заходя в соответсвующие 
  приложения. мне показалась такая мелочь удобной. также можно например не заходя в твиттер или файсбук менять статус: 
  написать twit или face в меню поиска и далее статус! Резюме: телефон не для игр, экран маловат, иногда не очень удобно
   из-за этого серфить в интернете.Но в принципе к этому быстро привыкаешь и это не так уж сильно напрягает. всяких 
   бестолковых приложения "ради поиграться" как для андоида вы не найдете, их дейсвительно мало. Телефон для работы, 
   для переписки, клавиатура супер, HUB - очень удобная вещь! ну и связь выше похвал! Примечание: на моей коробке 
   с телефоном написано что во франции сети могут не поддерживаться. действительно - сеть пропадла очень часто в париже
   . так что кто часто туда мотается - учитывайте! """)

negative = test.process("""     1. 3g интернет так и не удалось настроить. Проблема "серых" APN. Оператор Ростелеком. 
Сменить оператора невозможно
    2. Нет one note и нормальной интеграции со skydrive. Это необходимо. Конвертированная андроидная прога, не идет. 
    Программа, которая, вроде, работает с One note есть только для Playbook.
     3. Поиск не сбрасывается. т.е. если ты начал набирать Ивано.. И нашел контакт, через некоторое время стал набирать 
     петро.., то сначала надо удалить оставшееся в строке поиска. Когда много работаешь с телефоном, это выносит.
    4. Блютус с гарнитурой работает некорректно. Команда "перезвонить" не воспринимается, подъем трубки работает через 
    раз. Зачастую надо нажать кнопку и на гарнитуре и на телефоне. Голосового набора без 3g нет, чтения смс нет, 
    голосового управления нет.
    5. Интерфейс перегружен. Много мелких обозначений для такого маленького экрана. Прям привет WinMobile, дайте стилус
     ))))
    6. Хваленый "хаб" нечитаем. При не самом большом количестве уведомлений: плотный календарь, звонки, смс, 3 почты. 
    Зачастую непонятно что там вообще произошло. Приходится вглядываться и искать. Много езжу в машине - напрягает
    7. Подвисает. Не подолгу, и не часто, но это происходит просто при работе с интерфейсом. Прям как на андроид.
    8. Клавиатура с русской гравировкой не эргономична. Буквы сливаются приходится подолгу искать. До этого был 
    клавиатурник SonyEricsson Aspen p1i там клава была и удобнее и читаемее, да и тактильно равномерно выпуклые 
    клавиши находились пальцами лучше даже в перчатках. Тут в перчатках что-либо сделать вообще нереально.
    9. Не удалось настроить IP телефонию. Перепробовал все программы, какие смог найти. Не хочет работать и все.
     Глубоко не копал, т.к. на тот момент уже все поддостало.
    10. В BBRY World большинство программ платные, и тестового периода попробовать нет. При том, что, судя по отзывам,
     половина вообще не работают как так, вообще?
    11. Люфт задней крышки. Не критично, конечно, но она сдвигается каждый раз как подносишь телефон к уху.

Комментарий:
    К q10 долго присматривался. В итоге взял. Заставлял себя с ним ходить неделю, все думал, что привыкну. 
    Не вышло вообще. Сложил я его обратно в коробочку и стараюсь забыть.
    Телефон опоздал года на 2-3. если бы я перешел на него сразу, после win mobile, то, наверное, со многим мог бы
     смириться, но после WP уже решительно не хочется.
    Мале количество программ совсем не пугало, лишь бы основное было, но и его нет.
    Многое решается танцами с бубном, перепрошивками (любой форум почитайте) и т.п., но заниматься этим мне совершенно 
    не хочется и не интересно. Нужен просто рабочий инструмент, который требует к себе минимального внимания как к
     инструменту. А тут, прямо, привет с андроида. Непаханое поле для выкрутасов с непонятным финалом (особенно, когда, 
     скачав очередную прошивку, получаешь полный букет вирусов и рекламы в браузерах на компе)""")

print(positive)
print(negative)
