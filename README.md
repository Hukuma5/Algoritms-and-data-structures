# Алгоритмы и структуры данных

## №1 Сумма чисел

Реализуйте программу, которая считает сумму всех введенных чисел. Ввод может содержать любые символы.

## №2 Стек

Реализуйте стек, используя только массив.

**Формат входных данных**

На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются. Первая строка всегда содержит "set_size N", где N - максимальный размер стека, целое число. Каждая последующая строка содержит ровно одну команду: push X, pop или print, где X - произвольная строка без пробелов.

**Формат результата**

Команда print выводит содержимое стека (снизу вверх) одной строкой, значения разделяются пробелами. Если стек пуст, то выводится "empty". В случае переполнения стека выводится "overflow". Команда pop выводит элемент или "underflow", если стек пуст. Память под стек должна быть выделена не более одного раза, при вызове команды "set_size". В любой непонятной ситуации результатом работы любой команды будет "error". Результат работы программы выводится в стандартный поток вывода.

## №3 Очередь

Это как задача про стек, только про очередь. Реализуйте очередь, используя только массив. Ввод и вывод данных осуществляется через файлы. Имена входного и выходного файлов задаются через аргументы командной строки (первый и второй соответственно).

**Формат входных данных**

Во входном файле задаётся последовательность команд. Пустые строки игнорируются. Первая строка всегда содержит "set_size N", где N - максимальный размер очереди, целое число. Каждая последующая строка содержит ровно одну команду: push X, pop или print, где X - произвольная строка без пробелов.

**Формат результата**

Команда print выводит содержимое очередь (от головы к хвосту) одной строкой, значения разделяются пробелами. Если очередь пуста, то выводится "empty". В случае переполнения очереди выводится "overflow". Команда pop выводит элемент или "underflow", если очередь пуста. Память под очередь должна быть выделена не более одного раза, при вызове команды "set_size". В любой непонятной ситуации результатом работы любой команды будет "error".

## №4 Обход графа

Реализуйте обход графа в ширину и глубину. Вершины упорядочены в лексикографическом порядке.

**Формат входных данных**

Первая строка стандартного потока ввода данных имеет формат "[graph_type] [start_vertex] [search_type]", где "[graph_type]" - тип графа, ориентированный ('d') или неориентированный ('u'); "[start_vertex]" - идентификатор вершины, с которой начинать обход графа; "[search_type]" - тип обхода, в ширину ('b') или в глубину ('d'). Каждая последующая строка содержит ребро, которая представляет собой идентификаторы начальной и конечной вершины, разделенные пробелом.

**Формат результата**

Результат работы программы выводится в стандартный поток вывода. Идентификаторы посещенных вершин выводятся по одному в строке в порядке обхода.

## №5 Косое дерево

Реализуйте косое дерево(splay tree).
Реализация самой структуры данных должна быть инкапсулирована, т.е. не зависеть от формата входных/выходных данных и непосредственно ввода/вывода.

**Формат входных данных**

На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются.
Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max, extract или print, где K - целое число(64 бита вам хватит), ключ, V - произвольная строка без пробелов(значение).

**Формат результата**

Команда add добавляет значение V в дерево по ключу K, set - изменяет данные по ключу, команда delete удаляет данные.
Команда search выводит либо "1 V", либо "0", где V - значение для найденного ключа.
Команды min и max выводят "K V", где K -  минимальный или максимальный ключ дерева соответственно, V - значение по этому ключу.
Команда extract извлекает корень кучи и выводит "K V", где K, V - ключ и значение извлеченного элемента.
Команда print выводит всё дерево целиком. Она не изменяет дерево.
Дерево выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень дерева в формате "[K V]" или "__", если дерево пустое.
Каждая последующая строка содержит один уровень дерева. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.
В любой непонятной ситуации результатом работы любой команды будет "error".
Результат работы программы выводится в стандартный поток вывода.

## №6 Непростая куча

Реализуйте двоичную min-кучу. Модифицируйте её таким образом, чтобы внутреннее её строение было таким же, но при этом доступ по ключу к любому элементу осуществлялся за константное время.
Реализация самой структуры данных должна быть инкапсулирована, т.е. не зависеть от формата входных/выходных данных и непосредственно ввода/вывода.

**Формат входных данных**

На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируются.
Каждая строка содержит ровно одну команду: add K V, set K V, delete K, search K, min, max, extract или print, где K - целое число(64 бита вам хватит), ключ, V - произвольная строка без пробелов(значение).

**Формат результата**

Команда add добавляет значение V в кучу по ключу K, set - изменяет данные по ключу, команда delete удаляет данные.
Команда search выводит либо "1 I V", либо "0", где I - индекс, V - значение для найденного ключа.
Команды min и max выводят "K I V", где K -  минимальный или максимальный ключ кучи соответственно, I - индекс, V - значение по этому ключу.
Команда extract извлекает корень кучи и выводит "K V", где K, V - ключ и значение извлеченного элемента.
Команда print выводит всю кучу целиком.
Куча выводится строго по уровням, слева направо, 1 строка - 1 уровень. Первая строка содержит только корень кучи в формате "[K V]" или "__", если куча пустая.
Каждая последующая строка содержит один уровень кучи. Вершины выводятся в формате "[K V P]", где P - ключ родительской вершины. Если вершина отсутствует, ставится "_". Вершины разделены пробелом.
В любой непонятной ситуации результатом работы любой команды будет "error".
Результат работы программы выводится в стандартный поток вывода.

## №7 Автокоррекция

Реализуйте программу, которая предлагает варианты замены слова, в котором допущена одна ошибка. Эту задачу можно решить достаточно многими способами - на это ограничений нет, но код должен быть хорошего качества и читаемым. Регистр букв для программы коррекции не имеет значения (слова в словаре хранятся в нижнем регистре). Варианты ошибок - как в алгоритме Дамерау-Левенштейна: вставка лишнего символа, удаление символа, замена символа или транспозиция соседних символов.

**Формат входных данных**

Данные подаются на стандартный поток ввода. Пустые строки игнорируются. Первая строка содержит число N - количество слов в словаре. Последующие N строк содержат слова из словаря, по одному в строке. Остальные строки - слова, которые надо проверять.

**Формат результата**

Каждая строка выхода содержит предложение для исправления слов, в порядке их появления. Если слово не содержит ошибок, то выводится "%слово% - ok". Если слово содержит одну ошибку, то выводится "%слово% -> %слово_в_словаре%". Если вариантов несколько, то они разделяются запятой с пробелом. Если слово содержит более одной ошибки, то выводится "%слово% -?" Результат работы программы выводится в стандартный поток вывода.

## №8 Рюкзак

Решите задачу о рюкзаке методом динамического программирования. Алгоритм должен быть инкапсулирован.

**Формат входных данных**

Данные подаются на стандартный поток ввода. Пустые строки игнорируются. Первая строка содержит натуральное число - максимальную массу предметов, которую выдержит рюкзак. Каждая последующая содержит два неотрицательных числа: массу предмета и его стоимость.

**Формат результата**

Первая строка содержит два числа: суммарную массу предметов и их суммарную стоимость. В последующих строках записаны номера предметов, которые были помещены в рюкзак, в порядке возрастания номера. Результат работы программы выводится в стандартный поток вывода.

## №9 Сумасшедший богач

Один сумасшедший богач на старости лет впал в маразм и стал еще более сумасшедшим. Он решил отдать половину своих богатств тому, кто выиграет в математической игре. Правила игры: изначально каждый игрок начинает с нулевой суммой. Он может либо получить у богача 1 миллион сантиков, либо отдать ему 1 миллион сантиков, либо получить от богача ту же сумму, которая есть у него сейчас. Выигрывает тот, кто за минимальное количество действий наберет сумму, равную половине состояния богача. На беду других игроков, нашелся человек, который что-то слышал про жадные алгоритмы и двоичную систему счисления (возможно это вы).

**Формат входных данных**

В стандартном потоке записано единственное натуральное число - размер половины состояния богача (в миллионах).

**Формат результата**

Каждая строка выхода содержит ровно одну операцию (inc, dec или dbl) из кратчайшей последовательности действий для победы. Если кто-то решил отнимать деньги у умалишенных людей - значит, он очень жадный. Поэтому если решений несколько, выведите то, в котором больше операций удвоения суммы. Результат работы программы выводится в стандартный поток вывода.

## №10 Фильтр Блума

Реализуйте фильтр Блума, позволяющий дать быстрый, но вероятностный ответ, присутствует ли оъект в коллекции.
Реализация самой структуры данных должна быть инкапсулирована, т.е. не зависеть от формата входных/выходных данных и непосредственно ввода/вывода.
Реализация битового массива также должна быть инкапсулирована. Массив битов должен быть эффективно расположен в памяти.
Параметрами структуры данных является n - приблизительное количество элементов(целое), P - вероятность ложноположительного ответа.
Размер структуры m, вычисляется как -n*log<sub>2</sub>P / ln2, а количество хэш-функций как -log<sub>2</sub>P. Оба значения округляются до ближайшего целого.
В качестве семейства функций используйте семейство хэш-функций вида

h<sub>i</sub>(x) = (((i + 1)*x + p<sub>i+1</sub>) mod M) mod m,

где x - ключ, i - номер хэш-функции, p<sub>i</sub> - i - тое по счету простое число, а M - 31-ое число Мерсенна.

**Формат входных данных**

На стандартном потоке ввода задаётся последовательность команд. Пустые строки игнорируется.
Первая строка содержит команду вида set n P.
Каждая последующая строка содержит ровно одну команду: add K, search K или print, где K - неотрицательное число(64 бита вам хватит), ключ.

**Формат результата**

Команда set инициализирует структуру и выводит вычисленные параметры в формате "m k".
Команда add добавляет в структуру ключ K.
Команда search выводит либо "1", если элемент возможно присутствует в структуре, либо "0", если он там отсутствует.
Команда print выводит внутреннее состояние структуры - последовательность из 0 и 1, не разделенную пробелами.
В любой непонятной ситуации результатом работы любой команды будет "error".
Результат работы программы выводится в стандартный поток вывода.
