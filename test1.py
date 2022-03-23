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

if __name__ == '__main__':
    # 以货币形式显示
    print("货币形式：{:,d}".format(1000000))
    # 科学计数法表示
    print("科学计数法：{:E}".format(1200.12))
    # 以十六进制表示
    print("100的十六进制：{:#x}".format(100))
    # 输出百分比形式
    print("0.01的百分比表示：{:.0%}".format(0.01))