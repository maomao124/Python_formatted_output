"""
 * Project name(项目名称)：Python格式化输出
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/23 
 * Time(创建时间)： 21:01
 * Version(版本): 1.0
 * Description(描述)： str.format(args)
此方法中，str 用于指定字符串的显示样式；args 用于指定要进行格式转换的项，如果有多项，之间有逗号进行分割。
其完整的语法格式为：
{ [index][ : [ [fill] align] [sign] [#] [width] [.precision] [type] ] }
注意，格式中用 [] 括起来的参数都是可选参数，即可以使用，也可以不使用。各个参数的含义如下：
index：指定：后边设置的格式要作用到 args 中第几个数据，数据的索引值从 0 开始。如果省略此选项，则会根据 args 中数据的先后顺序自动分配。
fill：指定空白处填充的字符。注意，当填充字符为逗号(,)且作用于整数或浮点数时，该整数（或浮点数）会以逗号分隔的形式输出，例如（1000000会输出 1,000,000）。

align	含义
<	数据左对齐。
>	数据右对齐。
=	数据右对齐，同时将符号放置在填充内容的最左侧，该选项只对数字类型有效。
^	数据居中，此选项需和 width 参数一起使用。

sign：指定有无符号数

sign参数	含义
+	正数前加正号，负数前加负号。
-	正数前不加正号，负数前加负号。
空格	正数前加空格，负数前加负号。
#	对于二进制数、八进制数和十六进制数，使用此参数，各进制数前会分别显示 0b、0o、0x前缀；反之则不显示前缀。

width：指定输出数据时所占的宽度。
.precision：指定保留的小数位数。
type：指定输出数据的具体类型

type类型值	含义
s	对字符串类型格式化。
d	十进制整数。
c	将十进制整数自动转换成对应的 Unicode 字符。
e 或者 E 	转换成科学计数法后，再格式化输出。
g 或 G	自动在 e 和 f（或 E 和 F）中切换。
b	将十进制数自动转换成二进制表示，再格式化输出。
o	将十进制数自动转换成八进制表示，再格式化输出。
x 或者 X	将十进制数自动转换成十六进制表示，再格式化输出。
f 或者 F	转换为浮点数（默认小数点后保留 6 位），再格式化输出。
%	显示百分比（默认显示小数点后 6 位）。

 """
import datetime

if __name__ == '__main__':
    # 以货币形式显示
    print("货币形式：{:,d}".format(1000000))
    # 科学计数法表示
    print("科学计数法：{:E}".format(1200.12))
    # 以十六进制表示
    print("100的十六进制：{:#x}".format(100))
    # 输出百分比形式
    print("0.01的百分比表示：{:.0%}".format(0.01))

    print('{0} {1}'.format('Python', 3.7))  # Python 3.7
    print('{} {}'.format('Python', 3.7))  # Python 3.7
    print('{1} {0} {1}'.format('Python', 3.7))  # 3.7 Python 3.7

    print('{name}年龄是{age}岁。'.format(age=18, name="张三"))

    print('{:>8}'.format('1'))  # 总宽度为8，右对齐，默认空格填充
    print('{:0>8}'.format('1'))  # 总宽度为8，右对齐，使用0填充
    print('{:a<8}'.format('1'))  # 总宽度为8，左对齐，使用a填充

    s = "PYTHON"
    print(format(s, '10'))  # 没有标志符，如果是字符串则默认左对齐，不足宽度部分默认用空格填充
    print(format(13.14, '10'))  # 没有标志符，如果是数字则默认右对齐，不足宽度部分默认用空格填充
    print(format(s, '0>10'))  # 右对齐，不足指定宽度部分用0填充
    print(format(s, '>04'))  # 右对齐，因字符实际宽度大于指定宽度4，不用填充
    print(format(s, '*>10'))  # 右对齐，不足部分用"*"填充
    print(format(s, '>010'))  # 右对齐，不足部分用0填充
    print(format(s, '>10'))  # 右对齐，默认用空格填充
    print(format(s, '<10'))  # 左对齐，默认用空格填充
    print(format(s, '<010'))  # 左对齐，不足部分用0填充
    print(format(s, '@^10'))  # 中间对齐，不足部分用'@'填充，宽度为10个空格
    print(format(13.14, '0<10'))  # 左对齐，不足部分用0填充
    print(format(13.14, '@^10'))  # 中间对齐，不足部分用@填充
    print(format(13.14, '0>10'))  # 右对齐，不足部分用0填充
    print(format(-13.14, '0=10'))  # 右对齐，符号后面不足部分用0填充

    print(format(12.2, 'f'))  # 转换成浮点数，默认为小数保留6位，输出：12.200000
    print(format(12, 'd'))  # 转换成十进制，输出：12
    print(format(13))  # 不带参数默认为十进制，输出：13
    print(format(13, 'n'))  # 转换成十进制数，输出：13
    print(format(13, 'b'))  # 转换成二进制，输出：1101
    print(format(65, 'c'))  # 转换Unicode成字符，输出：A
    print(format(97, 'c'))  # 转换Unicode成字符，输出：a
    print(format(8750, 'c'))  # 转换Unicode成字符，输出：∮
    print(format(12, 'o'))  # 转换成八进制，输出：14
    print(format(12, 'x'))  # 转换成十六进制小写字母表示，输出：c
    print(format(12, 'X'))  # 转换成十六进制大写字母表示，输出：C

    print(format(628, '.1f'))  # 格式化为保留1位小数的浮点数，输出：628.0
    print(format(628, '.2f'))  # 格式化为保留2位小数的浮点数，输出：628.00
    print(format(3.14159, '.1f'))  # 格式化为保留1位小数的浮点数，输出：3.1
    print(format(3.14159, '.2f'))  # 格式化为保留2位小数的浮点数，输出：3.14
    print(format(3.14159, '.5f'))  # 格式化为保留5位小数的浮点数，输出：3.14159
    print(format(-3.14159, '.3f'))  # 格式化为保留3位小数的浮点数，输出：-3.142
    print(format(3.1415926535898, 'f'))  # 默认精度保留6位小数，输出：3.141593
    # 默认精度保留6位小数，不足部分用空格填充，输出：3.141590
    print(format(3.14159, 'f'))
    print(format(3.14159, '+.3f'))  # 格式化为保留3位小数带符号的浮点数
    print(format(3.14159, '>8.2f'))  # 右对齐，保留2位小数
    print(format(3.14159, '<10.2f'))  # 左对齐，宽度为10，保留2位小数，不足部分用空格填充
    print(format(3.14159, '<.3f'))  # 左对齐，保留3位小数
    print(format(3.14159, '@>10.3f'))  # 右对齐，用“@”填充不足位置
    print(format(-3.14159, '=10.2f'))  # 格式化为保留2位小数的10位数，默认用空格填充
    print(format(-3.14159, '0=10.2f'))  # 格式化为保留2位小数的10位数，空格用0填充
    print(format(3.14159, '0^10.2f'))  # 保留2位小数的10位数，居中显示，空格用0填充

    print(format(0.161896, '%'))  # 将小数格式化成百分数，输出：16.189600%
    print(format(0.161896, '.2%'))  # 格式化为保留2位小数的百分数，输出：16.19%
    print(format(0.0238912, '.6%'))  # 格式化为保留6位小数的百分数，输出：2.389120%
    print(format(2 / 16, '.2%'))  # 格式化为保留2位小数的百分数，输出：12.50%
    print(format(3.1415926, '.1%'))  # 格式化为保留1位小数的百分数，输出：314.2%
    print(format(0.161896, '.0%'))  # 格式化为保留整数的百分数，输出：16%
    print(format(0.0238912, '8.6%'))  # 格式化为保留6位小数的八位百分数，输出：2.389120%
    print(format(0.0238912, '>8.3%'))  # 格式化为保留3位小数的八位百分数，输出：2.389%

    print(format(77))  # 格式参数为空，默认为十进制
    print(format(77, 'd'))  # 原来是十进制数，转换后为原值
    print(format(-77, 'd'))  # 原来是十进制数，转换后为原值
    print(format(77, '8d'))  # 转换为8位十进制数，空余部分用空格填充
    print(format(-77, '8d'))  # 转换为8位十进制数，负数在负号前填充空余部分空格
    print(format(77, '+8d'))  # 转换为8位带符号十进制数，在符号前填充空余部分空格
    print(format(-77, '08d'))  # 转换为8位十进制数，负数在负号前填充空余部分空格
    print(format(77, '+08d'))  # 转换为8位带符号十进制数，在符号前填充空余部分空格
    print(format(-77, '#8d'))  # 转换为8位十进制数，加进制标志
    print(format(-77, '=8d'))  # 转换为8位十进制数，空余部分填充空格
    print(format(+77, '=8d'))  # 转换为8位十进制数，空余部分填充空格
    print(format(+77, '*=8d'))  # 转换为8位十进制数，空余部分填充*
    print(format(+77, '*=+8d'))  # 转换为8位带符号十进制数，符号与数据之间填充*
    print(format(-77, '#=8d'))  # 转换为8位十进制数，在符号与空余部分填充#
    print(format(+77, '*<8d'))  # 转换为8位十进制数，左对齐，空余部分填充*
    print(format(-77, '#>8d'))  # 转换为8位十进制数，右对齐，空余部分填充#
    print(format(0X5A, 'd'))  # 十六进制数5A转换成十进制数，0X代表十六进制数
    print(format(0B011101, '+8d'))  # 二进制数011101转换成十进制数，0B代表二进制数
    print(format(0O34, 'd'))  # 八进制数34转换成十进制数，0O代表八进制数
    print(format(0O123456, '08d'))  # 十六制数123456转换成十进制数，不足用0填充
    print(format(+0X1234, '*>8d'))  # 十六进制数1234转换成十进制数，右对齐，不足用*

    print(format(0X5A, 'x'))  # 去除十六进制数的前缀，输出：5a
    print(format(0B011101, 'b'))  # 去除二进制数的前缀，输出：11101
    print(format(0O34, 'o'))  # 去除八进制数的前缀，输出：34

    now = datetime.datetime.now()
    print(format(now, '%Y-%m-%d %H:%M:%S %A'))  # 当前时间格式化为年-月-日+完整英文星期
    print(format(now, '%Y-%m-%d %H:%M:%S %a'))  # 当前时间格式化为年-月-日+简写英文星期
    # 中文年-月-日显示
    print(format(now, '%Y'), '年', format(now, '%m'), '月', format(now, '%d'), '日')
    # 中文时间显示
    print(format(now, '%H'), '年', format(now, '%M'), '分', format(now, '%S'), '秒')
    print(format(now, '%Y-%m-%d %H:%M:%S %a'))  # 当前时间格式化为年-月-日+简写英文星期
    print(format(now, '%Y-%m-%d'))  # 当前时间格式化为标准年-月-日
    print(format(now, '%y-%m-%d'))  # 当前时间格式化为短日期年-月-日
    print(format(now, '%Y<%m>%d'))  # 当前时间格式化为长日期年-月-日，间隔符为“<”和“>”
    print(format(now, '%c'))  # 本地对应的年-月-日星期表示

    print(format(now, '%B'))  # 本地完整的月份表示，输出：May
    print('现在是今年第', format(now, '%j'), '天')  # 今天是一年中第几天，输出：现在是今年第 017 天
    print('本周是今年第', format(now, '%U'), '周')  # 本周是一年中第几周，输出：本周是今年第 02 周
    print(format(now, '%y%m%d'))  # 无间隔符短日期格式年月日，输出：210117
    print(format(now, '%Y-%m'))  # 长日期格式年-月，输出：2021-01
    print(format(now, '%m-%d'))  # 月-日显示，输出：01-17
    print(format(now, '%m'))  # 月份单独显示，输出：01
    print(format(now, '%d'))  # 日期单独显示，输出：17

    print(format(now, '%H%M%S'))  # 无间隔符，输出：133536
    print(format(now, '%H:%M:%S'))  # 标准时-分-秒，输出：13:35:36
    print(format(now, '%I:%M:%S %I'))  # 12小时制时-分-秒，输出：01:35:36 01
    print(format(now, '%H:%M'))  # 时+分，输出：13:35
    print(format(now, '%M%S'))  # 分+秒，输出：3536
    print(format(now, '%H'))  # 只显示小时，输出：13
    print(format(now, '%H:%M:%S %p'))  # 日期显示按AM，PM显示，输出：13:35:36 PM
    print(format(now, '%a'))  # 英文星期简写，输出：Sun
    print(format(now, '%A'))  # 英文星期完整显示，输出：Sunday
    week = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
    print(week[int(format(now, '%w'))])  # 中文星期，输出：星期日

    dt = datetime.datetime(2020, 5, 9)
    dm = datetime.datetime(2020, 5, 9, 12, 50, 20)
    # 将输入的日期按年-月-日和时间格式化，因时间没有输入，按0时处理
    print(format(dt, '%Y-%m-%d %H:%M:%S'))
    print(format(dt, '%Y-%m-%d'))  # 将输入的日期按年-月-日格式化
    print(format(dm, '%Y-%m-%d %H:%M:%S'))  # 将输入的日期按年-月-日和时间格式化
    print(format(dm, '%Y-%m-%d'))  # 将输入的日期按年-月-日格式化

    wx = datetime.datetime.now()
    print(str(wx), format(1, '0>3'))  # 年-月-日 +3位编号
    print(format(now, '%Y-%m-%d'), format(1, '0>3'))  # 年-月-日 +3位编号
    print(format(now, '%Y%m%d'), 'NO' + format(1, '0>3'))  # 年-月-日 +NO+3位编号
    print(format(now, '%d'), 'NO' + format(1, '0>3'))  # 日期 +NO+3位编号
    print(format(now, '%H%M'), 'NO' + format(1, '0>3'))  # 时钟+分 +NO+3位编号
