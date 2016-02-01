##Итоговый отчет по проекту «Сервис микроблогов»
Титова Анна, гр.107, ПМИ ФКН
Ментор: Казаринов Андрей

##О самом проекте
Проект “Сервис микроблоггов” предполагает front- и back-end разработку веб-приложения, позволяющего пользователям публиковать короткие сообщения (аналог Твиттера). Соответственно, оно должно поддерживать регистрацию и авторизацию юзеров, публикацию постов от их имени, а так же возможность настройки профиля, просмотра ленты друзей и подписок. Вся реализация происходит на языке python с применением таких фреймворков, как flask и jinja2. Front-end разработка производится средствами html при поддержке таблиц стилей и скриптов Twitter Bootstrap. Само же веб-приложение поднимается с помощью NGINX и USWGI, причем все файлы находятся на виртуальной машине Amazon AWS Ubuntu Server. Еще одной важной составляющей проекта являются базы данных – MySQL и SQLAlchemy были собраны в одно мощное средство для поддержки пользователей и их постов. 
Так же по мере развития проекта добавлялись новые задачи – симпатичный user-friendly интерфейс приложения для облегчения работы с ним, возможность оценивать посты других пользователей, репостить их записи себе, редактировать свой профиль, смотреть список подписок, писать комментарии к записям, а также возможность поиска по #тегам.

##Реализация формальных критериев
Итак, рассмотрим сами критерии. За работающее приложение и возможность публикации тех самых коротких сообщений ставится 4-5, за возможность зафолловить пользователя и читать ленту своих подписок – 6-7 баллов, и за лайки, комментарии и прочие прелести продвинутых пользователей уже можно рассчитывать на «отлично». Реализованное мною приложение удовлетворяет всем критериям оценки 6-7 (включая «нижестоящие», то есть 4-5). 

##Реализация проекта.
  Итак, теперь мы подобрались к основной и самой занимательной части отчета – реализация. Пусть проект был не из самых серьезных, по пути возникало немало проблем, но все они были успешно преодолены в процессе доработки.
Начнем с самого начала – февраль, несколько первых проектных лекций, посвященных деталям реализации, настройке сервера, установке необходимого программного обеспечения и «разбору полетов» с основными технологиями, используемых в проекте. Мой прогресс на этом уровне реализации можно было бы назвать если не отрицательным, то никаким – в виду отсутствия у меня (на тот момент) портативного ноутбука, я не имела возможности работать в одном темпе с одногруппниками, хотя всеми силами пыталась запомнить весь лекционный материал. Однако и здесь не все прошло так гладко.
  Описанная сейчас мною проблема, возникшая на данном этапе, может показаться никак не связанной с самим проектом, однако, если разобраться, она имеет самое что ни на есть прямое отношение к реализации. Дело в том, что виртуальная машина, которую требовалось запустить, организовав на ней сервер, так и называлась – Ubuntu Server (насколько я сейчас понимаю, это означает операционную систему на самой виртуальной машине). Однако минимальные познания в устройствах серверов, виртуальных машин и прочих непроизносимых слов толкнули меня на мысль, что серверная убунта должна стоять и на моей локальной машине. Как оказалось – очень зря.
  Запустив машины, локальную и  виртуальную, на них удивительно легко было установить все необходимые фреймворки и средства (были написаны основные скрипты для запуска приложения __init__.py, run.py, config.py и db_create.py и настроены конфигурации nginx’a, mysql’я) – кроме одного. PyCharm.Среда разработки, по всем законам жанра, требует мощной графической оболочки – да хоть просто графическую оболочку! – коей серверная версия операционной системы не обладает. Остается два выхода – переустанавливать всю операционку вместе со всеми свеженастроенными программами – или же довольствоваться консольными редакторами. Первая идея отсеклась на корню в виду отсутствия времени, моих познаний и связей с понимающими в этом людьми, как следствие - здравствуй, vim и nano. 
  Как вы поняли, написание проекта слегка усложнилось вышеизложенными обстоятельствами в виду длительных переходов между папками, ограниченными возможностями правки  в консольных редакторах и ручным залитием кода на github. В связи с этим долгий март ушел на разборки с принципами работы консоли и самого веб-приложения, а так же написание более-менее осмысленного каркаса. Здесь возникла первая модель базы данных, состоящая из двух таблиц Users и Posts, первый простенький шаблон на Bootstrap’е и первые рабочие строчки в models.py, views.py. Однако март-апрель так же были периодами напряженной учебы по остальным предметам с неустанными сдачами контрольных и домашних работ, поэтому работа над проектом на время приостановилась – и началась с новыми силами уже в мае.
  Майские каникулы – не самое лучшее время, чтобы программировать, однако для того, чтобы придумать и реализовать интересные шаблоны, вполне сгодятся. Простыми формами на цветастеньком фоне уже никого не удивишь, нужно было придумать что-то новое, но не такое сложное в реализации, чтобы безболезненно успеть к сроку. На этом этапе была придумана практически вся front-end концепция микроблога – представить его в виде ленты в прямом смысле. Каждый «твит» представлял бы собой некое подобие вырезки из газет, эдакой «вырванной» цитаты. Изюминкой этой детали стала текстура бумаги, на которой написана цитата: в папке static на сервере на данный момент лежит 5 видов изображений. При создании твита одно из его полей в базе данных заполняется рандомным числом от одного до пяти, и впоследствии именно в зависимости от этого числа шаблон определяет, какая из текстур должна быть применена. Следующая страница - лента подписок: свиток с этими цитатами, идущий из печатной машинки (причем машинка строго привязана к «подвалу» страницы, таким образом, какой бы длины лента не оказалась, машинка вместе с полем для публикации твитов всегда будет у ее «подножия»). Страница регистрации-авторизации  же представляет собой стопку бумаги, торчащей из той же (хотя, по сути, другой) печатной машинки; она переключается с листа на лист (т.е., с формы на форму) простеньким JS-скриптом. И лишь страница пользователя наименее привязана к общей тематике: здесь – стандартная, почти твиттерская, шапка, поле для «вырезок»  и блоки с необходимыми кнопками. Изначально и эта страница задумывалась поинтереснее – то была «первая полоса» газеты, где, соответственно, шапка – это логотип с броским названием, а кнопки – вроде содержания. За майские праздники все вышеизложенное в более-менее приемлемом виде реализовано средствами html, css и Bootstrap.
За время верстки я узнала множество новых нюансов. Во-первых, мне ужасно понравилось использовать jinja2 для разметки необходимых параметров на странице – как удобно порой загнать что-то в цикл или использовать if’ы, чтобы сменить оформление пользователю! Ее автор определенно был гением, ибо оно работает просто, но очень эффективно. Во-вторых, хочется отметить еще одно такое блестящее изобретение человечества, как плавающие контейнеры Bootstrap’а, да и сам Bootstrap в целом. Пусть порой нужно четко осознавать, какой класс приписывать той или иной кнопке, в итоге страницы приобретают законченный образ, и, что приятно, не теряют своей красоты при масштабировании окна. Однако с этими двумя средствами проблем почти не возникало – естественно, основная часть все равно падала на html. Так, оформление  твита-цитаты изначально задумывалось еще более сложным: это не просто пять картинок бумаги, но два набора изображений. Первый отвечает за цвет бумаги, второй – за своеобразную рамку, те самые оторванные края «вырезок». Таким образом, разнообразие вариантов возрастало в квадрате. Было даже найдено средство для реализации сего адского решения: в html5 существует поддержка двух фоновых изображений для блока, и под низ можно было загрузить текстуру, а сверху – обрезать ее края другой картинкой. Тем не менее, возникла проблема с несовпадением цвета «поверхности», на которой лежат твиты – она была полупрозрачная – и рамкой, потому от этой идеи я отказалась. 

  К этому же времени была усовершенствована модель базы данных: теперь это уже более сложная конструкция со сводными таблицами, отвечающими за фолловинг, теги, лайки, комментарии и прочие прелести жизни. Хотя базировались эти нововведения все еще на исходных Users и Posts, пусть и с дополнительными параметрами (к Пользователям добавилась несколько граф, связанных с дизайном (шапка, фон, название дневника и описание)). Однако если на картинке база данных уже включала в себя несколько новых сводных таблиц, до реализации некоторых их них дело так и не дошло.
Близился конец мая, и вот, наконец-то, после, кажется, миллиона прочитанных статей про микроблоги, flask, sqlalchemy и прочие радости жизни, появились первые зачатки работающей авторизации-регистрации – к промежуточному отчету поддержка базы данных так и не была реализована, но  уже к июню все необходимые функции были написаны (чуть далее я расскажу о них подробнее в контексте структуры приложения). Вообще, что касается самого кода, вся реализация проекта сводится к умелому оперированию тремя файлами сервера и шаблонами со статикой. Эти файлы – models.py, forms.py и views.py – отвечают соответственно за модель базы данных и прилежащих к ней функций, формы, используемые в проекте, и, собственно, представления всех функций и страниц приложения. Работа полетела очень быстро – понимания основ работы хватило для успешной отладки приложения (естественно, проблемы возникали, например, написанная мною авторизация не имела смысла без коротенькой функции load_user), и к первым числам июня приложение уже имело возможности беспрепятственной регистрации-авторизации, публикации постов и фолловинга с лентой друзей. Сейчас, уже ближе к сдаче, в проекте реализованы так же функции представления списка подписчиков и подписок пользователя, а так же возможность изменять параметры в настройках.

###И наконец, давайте рассмотрим, из чего состоит микроблог:
•	Models.py: 

users  - id, nickname, email, password (в md5), last_been, posts (связь с написанными юзером постами), about (описание в шапке), title (заголовок дневника), background (ссылка на фон), style (ссылка на шапку), followed (сводная таблица подписок)
Значимые функции в классе: is_following(self, user), followed_posts (self), follows you(self), follow(self, user), unfollow(self, user)

posts – id, user_id, text, post_date, design (та самая рандомная величина, отвечающая за оформление поста).

•	Forms.py:  LoginForm, SignUpForm, Tweet, SettingsForm; 

•	Views.py:  
Функции: index (страница ленты), login, load_user (без нее не работает авторизация), settings, user/<login> (принимает на вход логин пользователя и перенаправляет на нужную страничку), [logout, follow/<user>, unfollow<user>] (не подразумевают шаблоны), followers, followings.

•	Шаблоны: base (страница пользователя), feed, login, followers (встроенный в base; подписки пользователя / на него),  index (встроенный в base; посты пользователя), settings (так же встроенный в base).
+ сама база данных, несколько необходимых конфигов, и, собственно, run.py.

Вот, вкратце, все, из чего состоит структура моего проекта. Он достаточно небольшой и несложный  (несмотря на мою реализацию, он достаточно прост в понимании и не требует заоблачных умений), но в то же время показался мне безумно интересным. 

##Инструкция по эксплуатации:
Для того, чтобы микроблог запустился у вас на сервере, нужно:
1.	Скопировать репозиторий на сервер;
2.	Установить uwsgi;
3.	Настроить nginx;
4.	Запустить:
 - uwsgi —socket 127.0.0.1:5000 --wsgi-file run.py --master --processes 4 --threads 2
непосредственно из папки репозитория на сервере.

Для того, чтобы оперировать на самом сайте, специальных инструкций не требуется.



Благодарю за прочитанный до конца отчет! Спокойной ночи.
