import re

# result = dir(re)

# re module kullanarak arama

str = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

#result = re.findall("Python", str)

#result = len(result)
# regular expression nasıl yazılır

#result = re.split(" ",str)

# result = re.sub(" ","-",str)

"""
result = re.search("Python",str) #var mı ve konumu
result = result.span() #konumu başlangıç bitiş
result = result.start() #hangi karakterden başlıyor
result = result.end() #hangi karakterde bitiyor
result = result.group() #neyi arıyor (Python)
result = result.string() #nerede arıyorsa o metni getirir
"""

#result = re.findall("[abc]",str) #str'nin içinde a,b,c karakterlerinin hepsini tek tek arar
#result = re.findall("[a-e]",str) # str'nin içinde a,b,c,d,e karkterlerini arar
#result = re.findall("[1-5]") #str'nin içinde 1,2,3,4,5 arar

# "[0-395]" => 0,1,2,3,9,5
# "[^abc]" => a,b,c dışındaki karakterler
# "[^0-9]" => rakam olmayan karakterler

""" . => Her hangi bir tek karakteri belirtir.
    ..  =>  a       :   No match
        =>  ab      :   1 match
        =>  abc     :   1 match
        =>  abcd    :   2 matches 
"""
# result = re.findall("...",str) # 3 karakterli olarak str'yi ayırıp yazdırır.
# result = re.findall("Py...n",str)

"""
^ => belirtlen karakterle başlıyor mu? En baştan
^a =>   a   :   1 match
        abc :   1 match
        cda :   No match   
"""
result = re.findall("^P",str)

"""
$ - Belirtilen karakterle bitiyor mu?
a$  =>  a       :   1 match
        lamba   :   1 match
        Python  : No match

"""
result = re.findall("at$",str)

"""
* - Bir karakterin sıfır ya da daha fazla sayıda olmasını kontrol eder.
    ma*n    =>mn    : 1 match
            =>man   : 1 match
            =>maan  : 1 match
            =>main  : No match (a'nın akdasına n gelmiyor)
"""

result = re.findall("sa*t",str)

"""
    + - Bir karakterin bir ya da daha fazla sayıda olmasını kontrol eder.

        ma+n    =>  mn  : No match
                    man :   1 match
                    maaan   :   1 match
                    main    :   No match (a'nın arkasına n gelmiyor)                
"""

result = re.findall("sa+t",str)

"""
    ? - Bir karakterin sıfır ya da bir kere olmasını kontrol eder.

    ma?n    =>  mn   : No match
                man  : 1 match
                maaan   : 1 match
                main    : no match
"""

result = re.findall("sa?t",str)


"""
{} - Karakter sayısını kontrol eder.

    al{2}   =>  a'nın arkasına l karakteri 2 kere tekrarlamalı
    al{2,3} =>  a'nın arkasına l karakteri en az 2 en fazla 3 kere tekrarlamalı.
    [0-9]{2,4}  => En az 2 en çok 4 basamaklı sayılar
"""

#result = re.findall("a{2}",str) #yanyana 2 tane a varsa ['aa'] şeklinde çıktı verir.

#result = re.findall("[0-9]{2}",str) #str'nin içindeki 2 basamaklı sayıları getirir.

"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir.

        a|b => a ya da b

            cde => No match
            ade => 1 match
            acdbea => 2 matches
"""

"""
    () - Gruplama yapmak için kullanılır.
        (a|b|c)xy   => a,b,c karakterlerinin arkasına xz gelmelidir.
        axy => ok
        cxy => ok
        dyz => No match
"""

"""
    \ - özel karakterleri aramamızı sağlar.

        \$a => $ Karakterinin arkasına a karakterini arar. 
                yani regular expension engine tarafından yorumlanmaz.

        \A  -   Belirtilen karakter stringin başında mı?
            \Athe => the string ifadenin başında mı?
        
        \Z  -   Belirtilen karakter stringin sonunda mı?
            the\Z   => the string ifadenin sonunda mı?

        \b  -   Belirtilen karakter stringin başında ya da sonunda mı?
            the\b   => the string ifadenin sonunda mı?
            b\the   => the string ifadenin başında mı?

        \B  -   Belirtilen karakter stringin başında ya da sonunda değil mı?
            the\B   => the string ifadenin sonunda değil mi?
            B\the   => the string ifadenin başında değil mi?

        \d  -   [0-9] ile aynı anlama gelir yani rakam arar.
            \d => 12abc34
        
        \D  -   [^0-9] ile aynı anlama gelir yani rakam olmayanları arar.
            \D => 12abc34  

        \s  -   Boşluk karakterlerini arar.
        \S  -   Boşluk olmayan karakterleri arar.
        \w  -   Alfabetik karakterler, rakamlar ve altçizgi karakterleri.
        \W  -   w'nun tam tersini arar.

"""

result = re.findall("\APython",str)


print(result)
