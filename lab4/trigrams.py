#!/usr/bin/python
# -*- coding: utf-8 -*-

data = {
'дон гуан дон':0.026305,
'гуан дон гуан':0.026305,
'дона анна дона':0.021044,
'анна дона анна':0.021044,
'дона анна диего':0.021044,
'дон гуан лаура':0.021044,
'гуан дона анна':0.021044,
'дон гуан ступай':0.015783,
'дон гуан дона':0.015783,
'дона анна подите':0.015783,
'молчите дон гуан':0.010522,
'требую дон гуан':0.010522,
'гуан я дон':0.010522,
'барин дон гуан':0.010522,
'стать у двери':0.010522,
'ступай же лепорелло':0.010522,
'лаура дон карлос':0.010522,
'ай дон гуан':0.010522,
'анна о дон':0.010522,
'узнали дона анна':0.010522,
'входит дона анна':0.010522,
'прочь дон гуан':0.010522,
'ай ай ай':0.007332,
'командора дон гуан':0.005261,
'страдальца дона анна':0.005261,
'боится боже проклятое':0.005261,
'лепорелло нам нимало':0.005261,
'исполином какие плечи':0.005261,
'любовью нежной тронуть':0.005261,
'стороже в дверях':0.005261,
'просит завтра прийти':0.005261,
'нарочно дон гуан':0.005261,
'хотел в живых':0.005261,
'мешаю печали вашей':0.005261,
'неизбежна дон гуан':0.005261,
'гуан вставай лаура':0.005261,
'голос дон гуан':0.005261,
'дон карлос встает':0.005261,
'опасный дон гуан':0.005261,
'анне завтра лепорелло':0.005261,
'дон гуан милый':0.005261,
'бесподобно лаура прощайте':0.005261,
'бедны дон альвар':0.005261,
'несчастный дон гуан':0.005261,
'небо тихо недвижим':0.005261,
'тихо вы черные':0.005261,
'велю тебя зарезать':0.005261,
'угодно дон гуан':0.005261,
'наедине с прелестной':0.005261,
'возноситься я прошу':0.005261,
'коварство дона анна':0.005261,
'мучит дон гуан':0.005261,
'поздно бедная инеза':0.005261,
'несешь лепорелло подите':0.005261,
'лет дон карлос':0.005261,
'глядит и сердится':0.005261,
'стать на стороже':0.005261,
'ужин у лауры':0.005261,
'дон гуан красноречив':0.005261,
'шесть они толпиться':0.005261,
'прекрасно в комнате':0.005261,
'украдкою дона анна':0.005261,
'brava чудно бесподобно':0.005261,
'выйти вон дон':0.005261,
'лепорелло инеза черноглазая':0.005261,
'впадут и веки':0.005261,
'гуан ты кланяешься':0.005261,
'свиданья безропотно отдам':0.005261,
'взойдем в мадрит':0.005261,
'любил дона анна':0.005261,
'спой еще лаура':0.005261,
'дурно дон гуан':0.005261,
'жизни бедного гуана':0.005261,
'постой при мертвом':0.005261,
'дон гуан лепорелло':0.005261,
'явился одной минутой':0.005261,
'дон гуан слуга':0.005261,
'дон гуан здравствуй':0.005261,
'любил ее лепорелло':0.005261,
'лаура дон гуана':0.005261,
'лепорелло преславная прекрасная':0.005261,
'негодяй суровый узнал':0.005261,
'святую вашу повторять':0.005261,
'гуан в залог':0.005261,
'дона анна дон':0.005261,
'ай гуан кидается':0.005261,
'друг друга убивать':0.005261,
'лепорелло я счастлив':0.005261,
'скажешь ты лаура':0.005261,
'дерзну порочными устами':0.005261,
'кальвадо дона анна':0.005261,
'ага сам сознаешься':0.005261,
'анна нет отроду':0.005261,
'ног прощенья умоляю':0.005261,
'дон диего уходит':0.005261,
'развязке дело скажите':0.005261,
'сознаться дон гуан':0.005261,
'взгляд такого взгляда':0.005261,
'брат нахальный кавалер':0.005261,
'целует ее лаура':0.005261,
'ожидал дона анна':0.005261,
'когдато мой верный':0.005261,
'счастлив чей хладный':0.005261,
'плаще дон гуан':0.005261,
'думаю счастлив чей':0.005261,
'чудесной не сознаться':0.005261,
'принес к ногам':0.005261,
'гуан что делать':0.005261,
'дон гуан задумчиво':0.005261,
'лучшему нечаянно убив':0.005261,
'гуана вы встретили':0.005261,
'смотри ж бездельник':0.005261,
'дрожишь ты дон':0.005261,
'дона анна падает':0.005261,
'карлос я дон':0.005261,
'несчастный жертва страсти':0.005261,
'лаура очень дон':0.005261,
'волшебством беспрерывным увы':0.005261,
'монах у ваших':0.005261,
'александр сергеевич каменный':0.005261,
'играла как роль':0.005261,
'анна дон диего':0.005261,
'gran commendatore ah':0.005261,
'свиданье мне назначила':0.005261,
'сцена iii памятник':0.005261,
'глуп что осердился':0.005261,
'дон гуан досадно':0.005261,
'люди ль доны':0.005261,
'лаура милый друг':0.005261,
'гуан на поединке':0.005261,
'идет входит монах':0.005261,
'анна подите прочь':0.005261,
'гроб пойдете кудри':0.005261,
'карлос что дон':0.005261,
'зовут дон гуан':0.005261,
'сторожа кричат протяжно':0.005261,
'тучами покрыто холодный':0.005261,
'говорит дон гуан':0.005261,
'насилуто помог лукавый':0.005261,
'убил супруга твоего':0.005261,
'покорный я едваедва':0.005261,
'гости прощай лаура':0.005261,
'моем отсутствии лаура':0.005261,
'сделал что явился':0.005261,
'gentilissima del gran':0.005261,
'земля а небо':0.005261,
'щедушен здесь став':0.005261,
'жизни одной любви':0.005261,
'карлос не сердись':0.005261,
'дона анна оставь':0.005261,
'лепорелло дон гуан':0.005261,
'съединить дон гуан':0.005261,
'правы дон гуан':0.005261,
'прошу я требую':0.005261,
'умру дон гуан':0.005261,
'демон стучат дон':0.005261,
'блестят и щеки':0.005261,
'просит пожаловать ейбогу':0.005261,
'дона анна идет':0.005261,
'помышленьях простите дон':0.005261,
'проказы а всe':0.005261,
'лауры первый гость':0.005261,
'увы судьба судила':0.005261,
'двери входит дон':0.005261,
'анна по долгу':0.005261,
'позднее мой лепорелло':0.005261,
'согрет ее дыханием':0.005261,
'холодный мирный дона':0.005261,
'любовь мелодия взгляни':0.005261,
'тяжело пожатье каменной':0.005261,
'дона анна падая':0.005261,
'злодею кинжал вонзила':0.005261,
'небо точный дым':0.005261,
'кавалер со шпагою':0.005261,
'умоляю дона анна':0.005261,
'смерть за сладкий':0.005261,
'диего уходит дон':0.005261,
'оставила в покое':0.005261,
'лепорелло да дон':0.005261,
'балкона тревожа серенадами':0.005261,
'опомнись твой диего':0.005261,
'помог лукавый дон':0.005261,
'дон гуан недаром':0.005261,
'iv комната доны':0.005261,
'шпагою под мышкой':0.005261,
'мужнину гробницу дон':0.005261,
'карлоса отшельником смиренным':0.005261,
'ночью странную приятность':0.005261,
'гуан гей лаура':0.005261,
'тронут твой угрюмый':0.005261,
'комната доны анны':0.005261,
'первых тамошних красавиц':0.005261,
'обманывать хотел признался':0.005261,
'гуан не мучьте':0.005261,
'прелестной доной анной':0.005261,
'искупить у ног':0.005261,
'грешу вас слушая':0.005261,
'statua gentilissima del':0.005261,
'дон гуан наслаждаюсь':0.005261,
'дон гуан безбожник':0.005261,
'колена преклоняю дона':0.005261,
'дон гуан трус':0.005261,
'ваших ног прощенья':0.005261,
'гуан не правда':0.005261,
'карлос как дон':0.005261,
'сергеевич каменный гость':0.005261,
'оставь меня пусти':0.005261,
'подайте мне гитару':0.005261,
'тайну дона анна':0.005261,
'дон альвар богат':0.005261,
'счастлив завтра вечером':0.005261,
'уме дон гуан':0.005261,
'пахнет яркая луна':0.005261,
'вдовьи слезы бессовестный':0.005261,
'думаю скучает командор':0.005261,
'сердита лаура спой':0.005261,
'анна и такто':0.005261,
'море дон гуан':0.005261,
'должны но лгать':0.005261,
'мысли приди открой':0.005261,
'осужден дона анна':0.005261,
'brava brava чудно':0.005261,
'нейдет из треугольной':0.005261,
'кивая головой статуя':0.005261,
'милый демон стучат':0.005261,
'узами не связаны':0.005261,
'гробу быть верна':0.005261,
'сейчас вы говорили':0.005261,
'родного брата правда':0.005261,
'проникла даже отшельники':0.005261,
'выброшу его дон':0.005261,
'развеселились мы недолго':0.005261,
'седина в косе':0.005261,
'кончено о дона':0.005261,
'прийти попозже вечером':0.005261,
'боюсь моя печальная':0.005261,
'вражду дона анна':0.005261,
'бесплодно спой лаура':0.005261,
'гитана или пьяный':0.005261,
'искать в мадрите':0.005261,
'осердился лаура ага':0.005261,
'анна вечным поминаньем':0.005261,
'сцена iv комната':0.005261,
'любовник дон карлос':0.005261,
'анна прощайте дон':0.005261,
'уходит дон гуан':0.005261,
'альвар богат дон':0.005261,
'июле ночью странную':0.005261,
'лепорелло входит лепорелло':0.005261,
'тих и слаб':0.005261,
'гуан задумчиво бедная':0.005261,
'дон гуаном лепорелло':0.005261,
'умру вели дышать':0.005261,
'вечным поминаньем супруга':0.005261,
'ступай лепорелло преславная':0.005261,
'дон карлос падает':0.005261,
'повеса дон гуан':0.005261,
'узнал я поздно':0.005261,
'головой статуя ай':0.005261,
'гуан слушай лепорелло':0.005261,
'смерклось пока луна':0.005261,
'гуан я просить':0.005261,
'видно тут обдуманность':0.005261,
'любви дон гуан':0.005261,
'бедная инеза лепорелло':0.005261,
'тревожа серенадами ваш':0.005261,
'неправа на совести':0.005261,
'поцелуй дона анна':0.005261,
'дон карлоса лаура':0.005261,
'совершенством не играла':0.005261,
'вольно предавалась вдохновенью':0.005261,
'новой дон гуан':0.005261,
'тело да жив':0.005261,
'карлос скажи лаура':0.005261,
'сердце первый правда':0.005261,
'зов явился дон':0.005261,
'жизнь я осужден':0.005261,
'последней в андалузии':0.005261,
'говорил дон гуан':0.005261,
'счастлив как ребенок':0.005261,
'дон гуана дон':0.005261,
'эскурьялом мы сошлись':0.005261,
'лепорелло я стою':0.005261,
'миг свиданья безропотно':0.005261,
'нейдет вы развлекли':0.005261,
'покрыто холодный дождь':0.005261,
'нимало а гдето':0.005261,
'смел и дух':0.005261,
'идет и ветер':0.005261,
'небо тучами покрыто':0.005261,
'знакомо нам узнал':0.005261,
'ног пусть бедный':0.005261,
'гуан один холодный':0.005261,
'отпирает двери входит':0.005261,
'семья убитого лепорелло':0.005261,
'лаура эх дон':0.005261,
'овдовела дон гуан':0.005261,
'дон гуана мудрено':0.005261,
'передо мной скажите':0.005261,
'монах здесь памятник':0.005261,
'анна что слышу':0.005261,
'дон карлос милый':0.005261,
'дон гуан пред':0.005261,
'статуя ай дон':0.005261,
'должность вы приятнее':0.005261,
'судила мне иное':0.005261,
'холодный дождь идет':0.005261,
'дон карлос виноват':0.005261,
'встретили дона анна':0.005261,
'дон гуан гей':0.005261,
'беспрерывным увы судьба':0.005261,
'грудь моя дона':0.005261,
'прошу в окно':0.005261,
'новизною да слава':0.005261,
'анну взаперти держал':0.005261,
'подите сами дон':0.005261,
'прощенья мирный поцелуй':0.005261,
'дона анна утешь':0.005261,
'шею дон карлос':0.005261,
'лепорелло но дон':0.005261,
'демон сколько бедных':0.005261,
'поди дон гуан':0.005261,
'дон гуан уйдем':0.005261,
'пред мраморным супругом':0.005261,
'анна на мужнину':0.005261,
'памятник командора дон':0.005261,
'супруга командора убитого':0.005261,
'переродился вас полюбя':0.005261,
'гуан о лауру':0.005261,
'гуан и лепорелло':0.005261,
'бьются лаура ай':0.005261,
'тобою дона анна':0.005261,
'гробницу дон гуан':0.005261,
'гуан ты думаешь':0.005261,
'лаура который год':0.005261,
'выбран был дона':0.005261,
'диего я требую':0.005261,
'священной вашей воли':0.005261,
'отец мой отоприте':0.005261,
'карлос ты молода':0.005261,
'дон гуан оставь':0.005261,
'ночи и луны':0.005261,
'роще проклятая признаться':0.005261,
'встречал а голос':0.005261,
'питаете вражду дона':0.005261,
'видала дон гуан':0.005261,
'небесным и окроплен':0.005261,
'тото ж дон':0.005261,
'гуан решетка заперта':0.005261,
'подите прочь дон':0.005261,
'дона анна неправда':0.005261,
'здравствуй лаура дон':0.005261,
'рассержусь диего отвечайте':0.005261,
'теплый воздух ночь':0.005261,
'гуана мудрено признать':0.005261,
'доны анны лепорелло':0.005261,
'извергом о дона':0.005261,
'лаура а виновата':0.005261,
'безмолвно и думаю':0.005261,
'сеньора дона анна':0.005261,
'порочными устами мольбу':0.005261,
'диего только боюсь':0.005261,
'слезами дона анна':0.005261,
'пятку я заметил':0.005261,
'карлос я требую':0.005261,
'анна статуя брось':0.005261,
'лепорелло ай ай':0.005261,
'гранд дон карлос':0.005261,
'commendatore ah padrone':0.005261,
'прощаю но знать':0.005261,
'гуан или желать':0.005261,
'лепорелло дело дон':0.005261,
'тото же сидели':0.005261,
'входит дон гуан':0.005261,
'посетил в смущенном':0.005261,
'пойдете кудри наклонять':0.005261,
'гуан несчастный жертва':0.005261,
'желать кончины дона':0.005261,
'страсти безнадежной дона':0.005261,
'встань встань проснись':0.005261,
'гробе вас мучит':0.005261,
'начать с бровей':0.005261,
'смиренным я скрылся':0.005261,
'поминаньем супруга полно':0.005261,
'дон гуан правда':0.005261,
'анной вы говорили':0.005261,
'гуан не желайте':0.005261,
'друг мой ветреный':0.005261,
'сокровища пустые принес':0.005261,
'ветреный любовник дон':0.005261,
'яркая луна блестит':0.005261,
'заметил лепорелло довольно':0.005261,
'стою за городом':0.005261,
'сердится дон гуан':0.005261,
'лелеять и дарить':0.005261,
'помню три месяца':0.005261,
'вдова все помню':0.005261,
'душе твоей небесной':0.005261,
'таковы дон гуан':0.005261,
'супругом дона анна':0.005261,
'дона анна вечным':0.005261,
'черноглазая о помню':0.005261,
'жена ему воздвигла':0.005261,
'говорят безбожный развратитель':0.005261,
'печали вашей вольно':0.005261,
'вор ждет ночи':0.005261,
'преклоняю дона анна':0.005261,
'балкон как небо':0.005261,
'коленах пред мраморным':0.005261,
'твоим услугам дон':0.005261,
'приезжает каждый день':0.005261,
'анна де сольва':0.005261,
'гуан нет лепорелло':0.005261,
'дон гуан вставай':0.005261,
'дон гуан прощай':0.005261,
'прошу тебя прийти':0.005261,
'гуан правда лепорелло':0.005261,
'вздор несешь лепорелло':0.005261,
'анна какие речи':0.005261,
'убив дон карлоса':0.005261,
'бесподобно первый благодарим':0.005261,
'дон карлос счастливец':0.005261,
'признайся а сколько':0.005261,
'эх дон гуан':0.005261,
'красотою женской отшельники':0.005261,
'доны анны дон':0.005261,
'дон гуан небо':0.005261,
'o statua gentilissima':0.005261,
'супружеской любви дон':0.005261,
'говорить проси статую':0.005261,
'гуан вам незнаком':0.005261,
'карлос твой дон':0.005261,
'усталой много зла':0.005261,
'спой лаура спой':0.005261,
'сердце дон гуан':0.005261,
'статуя кивает головой':0.005261,
'слушая я жду':0.005261,
'случай дона анна':0.005261,
'любил о дон':0.005261,
'гуан лаура кидается':0.005261,
'счастью моему предаться':0.005261,
'дона анна молва':0.005261,
'мужчиной не говорит':0.005261,
'станете меня дона':0.005261,
'уходит лепорелло испанский':0.005261,
'лепорелло а командор':0.005261,
'приехать дона анна':0.005261,
'страшно дон гуан':0.005261,
'отдам я жизнь':0.005261,
'неправда дон гуан':0.005261,
'гуан слуга покорный':0.005261,
'лимоном и лавром':0.005261,
'дон гуана напомнил':0.005261,
'гей лаура лаура':0.005261,
'кинжал вот грудь':0.005261,
'дон гуан диего':0.005261,
'обретаю тогда молений':0.005261,
'анна и любите':0.005261,
'приму но вечером':0.005261,
'диего твой раб':0.005261,
'каменной его десницы':0.005261,
'синими да белизною':0.005261,
'гуан и дона':0.005261,
'убитого не помню':0.005261,
'дон гуан несчастный':0.005261,
'раб священной вашей':0.005261,
'зубы с скрежетом':0.005261,
'думаешь он станет':0.005261,
'темной и сторожа':0.005261,
'молиться и плакать':0.005261,
'долго был покорный':0.005261,
'приди открой балкон':0.005261,
'дон гуан дождемся':0.005261,
'лаура ты бешеный':0.005261,
'терпится изволь бьются':0.005261,
'сделает дон гуан':0.005261,
'дон гуан отопри':0.005261,
'взгляни сам карлос':0.005261,
'гуан я замолчу':0.005261,
'плакать дон гуан':0.005261,
'ай ай гуан':0.005261,
'гуан милый лепорелло':0.005261,
'поры как овдовела':0.005261,
'гуляем дон гуан':0.005261,
'послушай это место':0.005261,
'нечаянно убив дон':0.005261,
'диего я гуан':0.005261,
'анна а такто':0.005261,
'тихо недвижим теплый':0.005261,
'грех и знаться':0.005261,
'развратитель вы сущий':0.005261,
'понравился ты дон':0.005261,
'ссылке далеко лепорелло':0.005261,
'казнь я заслужил':0.005261,
'воздвигла и приезжает':0.005261,
'зарезать моим слугам':0.005261,
'гуан диего де':0.005261,
'гуан я убил':0.005261,
'анна нет мать':0.005261,
'дон гуан покорно':0.005261,
'скажите дон гуан':0.005261,
'гуан а признайся':0.005261,
'прощенья умоляю дона':0.005261,
'ревнив он дону':0.005261,
'вольно изливаться дона':0.005261,
'дона анна статуя':0.005261,
'лаура осьмнадцать лет':0.005261,
'желайте знать ужасную':0.005261,
'сердись она забыла':0.005261,
'место таким речам':0.005261,
'видно мне уйти':0.005261,
'прийти к твоей':0.005261,
'знать желаю дон':0.005261,
'приму дон гуан':0.005261,
'лаура осматривает тело':0.005261,
'наклонять и плакать':0.005261,
'небом правы дон':0.005261,
'дона анна случай':0.005261,
'любить нельзя вдова':0.005261,
'дона анна знак':0.005261,
'цену мгновенной жизни':0.005261,
'лепорелло первый сторож':0.005261,
'предо мной виновны':0.005261,
'гробе подите прочь':0.005261,
'воли все ваши':0.005261,
'лепорелло лепорелло входит':0.005261,
'лепорелло с доной':0.005261,
'страдать в безмолвии':0.005261,
'мольбу святую вашу':0.005261,
'тьмы не обратила':0.005261,
'погубили дон гуан':0.005261,
'дон гуан целуя':0.005261,
'лаура выходят лаура':0.005261,
'иное дона анна':0.005261,
'изливаться дона анна':0.005261,
'раздаваться дона анна':0.005261,
'любви музыка уступает':0.005261,
'жизни дон гуан':0.005261,
'мыслью быть наедине':0.005261,
'светлый сумрак тьмы':0.005261,
'ночи стал провождать':0.005261,
'слушать вас боюсь':0.005261,
'ваших помышленьях простите':0.005261,
'коснуться вы легкою':0.005261,
'приказанья вели умру':0.005261,
'жив гляди проклятый':0.005261,
'милый друг целует':0.005261,
'дон гуан решетка':0.005261,
'дышит каково дон':0.005261,
'дон гуан шутишь':0.005261,
'виноват лаура прости':0.005261,
'став на цыпочки':0.005261,
'могут к небу':0.005261,
'питаю дерзостных надежд':0.005261,
'полно не верю':0.005261,
'карлос падает дон':0.005261,
'ангел дона анна':0.005261,
'дон гуан счастливец':0.005261,
'враг ты отнял':0.005261,
'ah padrone don':0.005261,
'лаура дон гуан':0.005261,
'наслаждаюсь молча глубоко':0.005261,
'истинно прекрасного глаза':0.005261,
'гуан ангел дона':0.005261,
'слово я вольно':0.005261,
'право вечные проказы':0.005261,
'любила лаура делает':0.005261,
'твоей небесной дона':0.005261,
'импровизатором любовной песни':0.005261,
'просить прощенья должен':0.005261,
'конечно ну развеселились':0.005261,
'лаура не давай':0.005261,
'описан вам злодеем':0.005261,
'твоих дона анна':0.005261,
'лукавый дон гуан':0.005261,
'молода еще лет':0.005261,
'часах лепорелло охота':0.005261,
'видеть вас должен':0.005261,
'гуан что сделалось':0.005261,
'речи странные дон':0.005261,
'гуан сеньора дона':0.005261,
'анна нет видно':0.005261,
'монах сейчас сеньора':0.005261,
'двери на часах':0.005261,
'безнадежной дона анна':0.005261,
'лауры пришел искать':0.005261,
'изволь бьются лаура':0.005261,
'рассыплете и мнится':0.005261,
'гуан как сердцем':0.005261,
'лаура делает утвердительно':0.005261,
'услугам дон карлос':0.005261,
'останавливает дон карлоса':0.005261,
'обдуманность коварство дона':0.005261,
'гуан в июле':0.005261,
'карлос милый демон':0.005261,
'счастье дона анна':0.005261,
'сольва как супруга':0.005261,
'уйдем сцена iv':0.005261,
'знак согласия ай':0.005261,
'padrone don giovanni':0.005261,
'анна мне показалось':0.005261,
'выходят лаура останавливает':0.005261,
'косе твоей мелькнет':0.005261,
'глаза одни глаза':0.005261,
'встань проснись опомнись':0.005261,
'ай ай умру':0.005261,
'гуан минуту дона':0.005261,
'дон карлос дон':0.005261,
'рабом моим желали':0.005261,
'смею вы ненавидеть':0.005261,
'покорно просит пожаловать':0.005261,
'молча глубоко мыслью':0.005261,
'узнала дон гуан':0.005261,
'стук о скройся':0.005261,
'статуя мой барин':0.005261,
'требую но видеть':0.005261,
'гуан я счастлив':0.005261,
'испанский гранд дон':0.005261,
'гуан лаура милый':0.005261,
'безбожник и мерзавец':0.005261,
'казнить хоть казнь':0.005261,
'издали с благоговеньем':0.005261,
'слово счастье дона':0.005261,
'жду только приказанья':0.005261,
'дон гуан ежели':0.005261,
'далее тем лучше':0.005261,
'жертвы новой дон':0.005261,
'стучат дон гуан':0.005261,
'дым а женщины':0.005261,
'лаура их сочинил':0.005261,
'гуан здесь дона':0.005261,
'ногой или одеждой':0.005261,
'утешили несчастного страдальца':0.005261,
'командор что скажет':0.005261,
'расстаться нам дон':0.005261,
'чей это голос':0.005261,
'альвар меня любил':0.005261,
'скромностью а пуще':0.005261,
'don giovanni сцена':0.005261,
'гуана дон карлос':0.005261,
'бедного гуана заботитесь':0.005261,
'простите дон гуан':0.005261,
'развратным бессовестным безбожным':0.005261,
'ужели боже отпирает':0.005261,
'единый благосклонный взгляд':0.005261,
'предавалась вдохновенью слова':0.005261,
'приходит это имя':0.005261,
'пройдет когда твои':0.005261,
'сердца мне дона':0.005261,
'увидел дон гуан':0.005261,
'уходит и вбегает':0.005261,
'поет все прелестно':0.005261,
'анна встань встань':0.005261,
'гуан милое созданье':0.005261,
'вставай лаура кончено':0.005261,
'незнаком дона анна':0.005261,
'могли вы оскорбить':0.005261,
'анна неправда дон':0.005261,
'счастливец он сокровища':0.005261,
'покрывалом чуть узенькую':0.005261,
'статуя командора дона':0.005261,
'монах развратным бессовестным':0.005261,
'идет к развязке':0.005261,
'узнать антоньев монастырь':0.005261,
'гуан вас просит':0.005261,
'входит статуя командора':0.005261,
'печальная беседа скучна':0.005261,
'выйти вам неосторожный':0.005261,
'лаура лаура дон':0.005261,
'анна пора поди':0.005261,
'вашего балкона тревожа':0.005261,
'бессовестным безбожным дон':0.005261,
'дону анну взаперти':0.005261,
'клянусь тебе лаура':0.005261,
'убийственную тайну дона':0.005261,
'видно бредишь дон':0.005261,
'едваедва не умер':0.005261,
'тронуть ваше сердце':0.005261,
'счастлив я петь':0.005261,
'близко дале гденибудь':0.005261,
'можете вы слышать':0.005261,
'каково дон гуан':0.005261,
'крестьянки на первых':0.005261,
'слова лаура лаура':0.005261,
'гуан досадно право':0.005261,
'лишь не гоните':0.005261,
'порога чтоб камня':0.005261,
'недаром же покойник':0.005261,
'глаза да взгляд':0.005261,
'надежду любовью нежной':0.005261,
'гуан из ссылки':0.005261,
'хотел лаура эх':0.005261,
'усы плащом закрыв':0.005261,
'гуаном лепорелло ого':0.005261,
'карлос я глуп':0.005261,
'дурно дурно дон':0.005261,
'развлекли меня речами':0.005261,
'дон гуан опасный':0.005261,
'мирный дона анна':0.005261,
'верю дон гуан':0.005261,
'знать ужасную убийственную':0.005261,
'дона анна отец':0.005261,
'прощайте дон диего':0.005261,
'звать зачем дон':0.005261,
'небесной дона анна':0.005261,
'имя равнодушно лаура':0.005261,
'волшебница ты сердце':0.005261,
'досадно право вечные':0.005261,
'серенадами ваш сон':0.005261,
'плакать дона анна':0.005261,
'улицам знакомым усы':0.005261,
'leporello o statua':0.005261,
'окно прыгнуть лепорелло':0.005261,
'сейчас у ваших':0.005261,
'дарить и серенадами':0.005261,
'приняла вас дон':0.005261,
'самовольно в мадрит':0.005261,
'вопроса дон диего':0.005261,
'гость авторы пушкин':0.005261,
'неужто о вдовы':0.005261,
'мадрите не боюсь':0.005261,
'пьяный музыкант иль':0.005261,
'благословили вы дон':0.005261,
'мрамор бледный рассыплете':0.005261,
'власы на мрамор':0.005261,
'верить не смею':0.005261,
'спроси у лепорелло':0.005261,
'гуан не смею':0.005261,
'гробнице мертвого счастливца':0.005261,
'помню кем монах':0.005261,
'гранд как вор':0.005261,
'устами мольбу святую':0.005261,
'лет пять иль':0.005261,
'сущий демон сколько':0.005261,
'делает утвердительно знак':0.005261,
'глуп так помиримся':0.005261,
'слезы бессовестный дон':0.005261,
'каменный гость leporello':0.005261,
'убивать на перекрестках':0.005261,
'тамошних красавиц право':0.005261,
'взоре и помертвелых':0.005261,
'жертва страсти безнадежной':0.005261,
'густой и темной':0.005261,
'сделалось с тобою':0.005261,
'залог прощенья мирный':0.005261,
'воздух ночь лимоном':0.005261,
'женской отшельники прельщаться':0.005261,
'почернеют и седина':0.005261,
'сейчас должна приехать':0.005261,
'лавром пахнет яркая':0.005261,
'мирный поцелуй дона':0.005261,
'ног твоих дона':0.005261,
'знак очень лаура':0.005261,
'предуготовленья импровизатором любовной':0.005261,
'бездна дон гуан':0.005261,
'дона анна прощайте':0.005261,
'падает дон гуан':0.005261,
'лепорелло испанский гранд':0.005261,
'веки сморщась почернеют':0.005261,
'явился дон гуан':0.005261,
'анна я приняла':0.005261,
'статую дон гуан':0.005261,
'восторгом мой сан':0.005261,
'требуете дон гуан':0.005261,
'сейчас лаура дон':0.005261,
'проси ее пожаловать':0.005261,
'король а впрочем':0.005261,
'покое семья убитого':0.005261,
'врешь лепорелло молчите':0.005261,
'молений я дивлюсь':0.005261,
'скройся дон гуан':0.005261,
'мадрит уходит лепорелло':0.005261,
'приготовь я счастлив':0.005261,
'кидается на постелю':0.005261,
'дон карлоса отшельником':0.005261,
'приятность я находил':0.005261,
'статуе я командор':0.005261,
'забыли дон гуан':0.005261,
'анны дон гуан':0.005261,
'боюсь дон гуан':0.005261,
'удар мой искупить':0.005261,
'прыгнуть лепорелло конечно':0.005261,
'мир обнять лепорелло':0.005261,
'господа гости прощай':0.005261,
'глупый лепорелло последней':0.005261,
'скажу без предуготовленья':0.005261,
'дона анна ужасную':0.005261,
'мирный монастырь проникла':0.005261,
'глаза твои блестят':0.005261,
'верн супружеской любви':0.005261,
'назначила лепорелло неужто':0.005261,
'всe не виноват':0.005261,
'дон гуан ангел':0.005261,
'лепорелло завтра приготовь':0.005261,
'богат дон гуан':0.005261,
'недолго нас покойницы':0.005261,
'венте я лауры':0.005261,
'монах мы красотою':0.005261,
'вечером и стать':0.005261,
'анна случай увлек':0.005261,
'монах о дона':0.005261,
'анна знак безумства':0.005261,
'сладкий миг свиданья':0.005261,
'ног ли дон':0.005261,
'доне анне прийти':0.005261,
'гуан дождемся ночи':0.005261,
'мешаю как апрель':0.005261,
'такто вы молчите':0.005261,
'лаура только смотри':0.005261,
'вонзила в сердце':0.005261,
'лепорелло а живы':0.005261,
'лаура ай ай':0.005261,
'лепорелло нет посмотрите':0.005261,
'покойник был ревнив':0.005261,
'сейчас она приедет':0.005261,
'серенадами ночными тешить':0.005261,
'дон гуан слушай':0.005261,
'поглядеть на вдовьи':0.005261,
'сколько бедных женщин':0.005261,
'поры и понял':0.005261,
'дона анна де':0.005261,
'лаура в сию':0.005261,
'души а чьи':0.005261,
'гордый гроб пойдете':0.005261,
'охота вам шутить':0.005261,
'шпаге дон гуан':0.005261,
'согласия ай дон':0.005261,
'молчите я нарочно':0.005261,
'убил его родного':0.005261,
'перестаньте я грешу':0.005261,
'желаю дон гуан':0.005261,
'сцена ii комната':0.005261,
'чьи слова лаура':0.005261,
'громко раздаваться дона':0.005261,
'гробницу эту ангел':0.005261,
'карлос дон гуан':0.005261,
'ужасную вы мучите':0.005261,
'ног твоих жду':0.005261,
'тобою лепорелло кивая':0.005261,
'души его молиться':0.005261,
'положу на перекрестке':0.005261,
'задумчиво бедная инеза':0.005261,
'гуан ну смотри':0.005261,
'дона анна встань':0.005261,
'карлос и любишь':0.005261,
'целуя ей руки':0.005261,
'белизною да скромностью':0.005261,
'шляпой как думаешь':0.005261,
'друзья здесь ужинали':0.005261,
'остыть ему бесплодно':0.005261,
'скрежетом дон карлос':0.005261,
'спой чтонибудь лаура':0.005261,
'дон гуан смерти':0.005261,
'гуан наслаждаюсь молча':0.005261,
'гуан отопри лаура':0.005261,
'гуан ступай лепорелло':0.005261,
'вкусил он райское':0.005261,
'слезы с улыбкою':0.005261,
'дрожащие колена преклоняю':0.005261,
'женщин вы погубили':0.005261,
'лепорелло ну тото':0.005261,
'безмолвии дона анна':0.005261,
'безбожным дон гуаном':0.005261,
'увидимся дона анна':0.005261,
'ай умру дон':0.005261,
'разврата я долго':0.005261,
'хвалы ему поют':0.005261,
'епанчою и положу':0.005261,
'чей хладный мрамор':0.005261,
'анна я слушать':0.005261,
'провождать у вашего':0.005261,
'каждое движенье слово':0.005261,
'несчастного страдальца дона':0.005261,
'гуан здравствуй лаура':0.005261,
'поверьте дон гуан':0.005261,
'диего де кальвадо':0.005261,
'чинились мы друг':0.005261,
'гуан вот нечаянная':0.005261,
'лепорелло кивая головой':0.005261,
'анне прийти попозже':0.005261,
'хотел поговорить монах':0.005261,
'вашей и стать':0.005261,
'поверю чтоб дон':0.005261,
'нравилися мне глазами':0.005261,
'командора дона анна':0.005261,
'вдохновенью слова лились':0.005261,
'бегу являться лепорелло':0.005261,
'жизнь дона анна':0.005261,
'камня моего могли':0.005261,
'подите ж прочь':0.005261,
'лепорелло и слава':0.005261,
'преславная прекрасная статуя':0.005261,
'осьмнадцать лет дон':0.005261,
'полечу по улицам':0.005261,
'сегодня утешили несчастного':0.005261,
'виновны вы дон':0.005261,
'оставь меня слабо':0.005261,
'отопри лаура ужели':0.005261,
'проклятая признаться должность':0.005261,
'жив еще лаура':0.005261,
'статую в гости':0.005261,
'a входит статуя':0.005261,
'ужасную убийственную тайну':0.005261,
'карлос виноват лаура':0.005261,
'анна диего перестаньте':0.005261,
'дон гуан пошлет':0.005261,
'правда ль полюбив':0.005261,
'блестит на синеве':0.005261,
'когданибудь дон гуан':0.005261,
'спою а слушайте':0.005261,
'лаура кончено лаура':0.005261,
'заботитесь так ненависти':0.005261,
'сцена i дон':0.005261,
'монастырь мне памятен':0.005261,
'гуан лепорелло лепорелло':0.005261,
'рабская но сердце':0.005261,
'прелестно бесподобно лаура':0.005261,
'разгорелись не проходит':0.005261,
'знакомым усы плащом':0.005261,
'закрыв а брови':0.005261,
'дух имел суровый':0.005261,
'перестань дон карлос':0.005261,
'дон гуан влюбился':0.005261,
'вашей вольно изливаться':0.005261,
'слышать это имя':0.005261,
'любви ее слезами':0.005261,
'тяготеет так разврата':0.005261,
'дон гуан милое':0.005261,
'сердцем я слаба':0.005261,
'анна падает статуя':0.005261,
'удавалось сегодня каждое':0.005261,
'опасный чем дона':0.005261,
'речам таким безумствам':0.005261,
'дон карлос перестаньте':0.005261,
'двери статуя кивает':0.005261,
'сан мои богатства':0.005261,
'постелю дон карлос':0.005261,
'рождала не память':0.005261,
'вели умру вели':0.005261,
'называть тебя старухой':0.005261,
'гость leporello o':0.005261,
'идет за монахом':0.005261,
'житье да долго':0.005261,
'помиримся дон карлос':0.005261,
'бредишь дон гуан':0.005261,
'лепорелло что какова':0.005261,
'ух не сердита':0.005261,
'недвижим теплый воздух':0.005261,
'ждете монах сейчас':0.005261,
'дойдет что дон':0.005261,
'прощай лаура выходят':0.005261,
'карлос встает зови':0.005261,
'молва о дон':0.005261,
'хотел признался ль':0.005261,
'мать моя велела':0.005261,
'бессовестный дон гуан':0.005261,
'скажите мне несчастный':0.005261,
'сердце ткнул небось':0.005261,
'день мою прелестную':0.005261,
'входит монах монах':0.005261,
'далеко на севере':0.005261,
'гуан покорно просит':0.005261,
'ль доны анны':0.005261,
'достигли мы ворот':0.005261,
'прельщаться не должны':0.005261,
'променяю вот видишь':0.005261,
'дон гуан сеньора':0.005261,
'слаба дон гуан':0.005261,
'del gran commendatore':0.005261,
'монах монах сейчас':0.005261,
'севере в париже':0.005261,
'какова дон гуан':0.005261,
'странные дон гуан':0.005261,
'хладный мрамор согрет':0.005261,
'лаура останавливает дон':0.005261,
'небу смиренно возноситься':0.005261,
'лаура перестань дон':0.005261,
'дон гуан случай':0.005261,
'вдовьим черным покрывалом':0.005261,
'мраморным супругом дона':0.005261,
'горд и смел':0.005261,
'гуан случай дона':0.005261,
'сегодня каждое движенье':0.005261,
'гуан уйдем сцена':0.005261,
'отоприте монах сейчас':0.005261,
'впущуся в разговоры':0.005261,
'кончины дона анна':0.005261,
'взойдет дон гуан':0.005261,
'застал дон гуан':0.005261,
'искуситель вы говорят':0.005261,
'прощайте ж господа':0.005261,
'твои глаза впадут':0.005261,
'лаура и вспомнил':0.005261,
'де кальвадо дона':0.005261,
'неосторожный дон гуан':0.005261,
'позвольте мой барин':0.005261,
'поняла дон гуан':0.005261,
'поединке честно убил':0.005261,
'предупреждать чтоб ваша':0.005261,
'городом в проклятой':0.005261,
'год тебе лаура':0.005261,
'похоронили командора монах':0.005261,
'требую чтоб улыбнулся':0.005261,
'сергеевич жанр драматургия':0.004574,
'раб у ног':0.004574,
'тайны не узнали':0.004172,
'пушкин александр сергеевич':0.003917,
'головой в знак':0.003887,
'друг мой милый':0.003200,
}

