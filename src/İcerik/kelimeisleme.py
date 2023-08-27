import string
# -*- coding: utf-8 -*-

turkce_harfler =['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'ğ', 'h', 'ı', 'i', 'j', 'k', 'l', 'm','n', 'o', 'ö', 'p', 'r', 's', 'ş', 't', 'u', 'ü', 'v',
                   'y', 'z', 'A', 'B', 'C', 'Ç', 'D', 'E', 'F', 'G', 'Ğ', 'H', 'I', 'İ', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'R', 'S', 'Ş', 'T', 'U',
                     'Ü', 'V', 'Y', 'Z']

ingilizce_harfler = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
                      'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

pinyin= {'的', '一', '是', '不', '了', '在', '人', '有', '我', '他', '这', '个', '中', '为', '大', '们', '来', '上', '以', '国', '和', '到', '地','之', '说', '时',
          '要', '出', '也', '就', '可', '会', '而', '于', '子', '生', '对', '年', '能', '得', '你', '下', '自', '道', '那', '后','行', '着', '发', '过', '所', '用', 
          '作', '事', '家', '里', '成', '方', '其', '然', '种', '去', '如', '多', '经', '法', '学', '同', '天', '都', '分', '当', '定', '者', '进', '么', '十', '主', 
          '日', '动', '部', '现', '面', '起', '小', '理', '还', '军', '与', '看', '本', '好', '无', '前', '些', '没', '心', '因', '从', '三', '只', '实', '样', '开', 
          '此', '公', '使', '将', '但', '意', '力', '民', '二', '长', '想', '它', '机', '知', '又', '第', '明', '把', '已', '工', '正', '见', '性', '她', '外', '业',
            '关', '高', '相', '两', '情', '全', '文', '问', '等', '由', '并', '月', '应', '间', '重', '物', '政', '点', '体', '战'} 

pinyin_den_latine =  {'的': 'de', '一': 'yī', '是': 'shì', '不': 'bù', '了': 'le', '在': 'zài', '人': 'rén', '有': 'yǒu', '我': 'wǒ', '他': 'tā', '这': 'zhè', '个': 'gè',
                     '中': 'zhōng','为': 'wèi', '大': 'dà', '们': 'men', '来': 'lái', '上': 'shàng', '以': 'yǐ', '国': 'guó', '和': 'hé', '到': 'dào', '地': 'dì', 
                     '之': 'zhī', '说': 'shuō','时': 'shí', '要': 'yào', '出': 'chū', '也': 'yě', '就': 'jiù', '可': 'kě', '会': 'huì', '而': 'ér', '于': 'yú', '子': 'zǐ',
                       '生': 'shēng', '对': 'duì','年': 'nián', '能': 'néng', '得': 'dé', '你': 'nǐ', '下': 'xià', '自': 'zì', '道': 'dào', '那': 'nà', '后': 'hòu', 
                       '行': 'xíng', '着': 'zhe', '发': 'fā','过': 'guò', '所': 'suǒ', '用': 'yòng', '作': 'zuò', '事': 'shì', '家': 'jiā', '里': 'lǐ', '成': 'chéng', 
                       '方': 'fāng', '其': 'qí', '然': 'rán', '种': 'zhǒng', '去': 'qù', '如': 'rú', '多': 'duō', '经': 'jīng', '法': 'fǎ', '学': 'xué', '同': 'tóng', 
                       '天': 'tiān', '都': 'dōu', '分': 'fēn', '当': 'dāng', '定': 'dìng','者': 'zhě', '进': 'jìn', '么': 'me', '十': 'shí', '主': 'zhǔ', '日': 'rì', '动': 'dòng',
                         '部': 'bù', '现': 'xiàn', '面': 'miàn', '起': 'qǐ', '小': 'xiǎo', '理': 'lǐ', '还': 'hái', '军': 'jūn', '与': 'yǔ', '看': 'kàn', '本': 'běn', 
                         '好': 'hǎo', '无': 'wú', '前': 'qián', '些': 'xiē', '没': 'méi', '心': 'xīn','因': 'yīn', '从': 'cóng', '三': 'sān', '只': 'zhǐ', '实': 'shí', 
                         '样': 'yàng', '开': 'kāi', '此': 'cǐ', '公': 'gōng', '使': 'shǐ', '将': 'jiāng', '但': 'dàn','意': 'yì', '力': 'lì', '民': 'mín', '二': 'èr',
                           '长': 'cháng', '想': 'xiǎng', '它': 'tā', '机': 'jī', '知': 'zhī', '又': 'yòu', '第': 'dì', '明': 'míng','把': 'bǎ', '已': 'yǐ', '工': 'gōng', 
                           '正': 'zhèng', '见': 'jiàn', '性': 'xìng', '她': 'tā', '外': 'wài', '业': 'yè', '关': 'guān', '高': 'gāo', '相': 'xiāng','两': 'liǎng', 
                           '情': 'qíng', '全': 'quán', '文': 'wén', '问': 'wèn', '等': 'děng', '由': 'yóu', '并': 'bìng', '月': 'yuè', '应': 'yīng', '间': 'jiān', '重': 'zhòng',
                           '物': 'wù', '政': 'zhèng', '点': 'diǎn', '体': 'tǐ', '战': 'zhàn'}



pinyinden_turkce = {'的': 'nin', '一': 'bir', '是': 'olmak', '不': 'değil', '了': 'tamamlandı', '在': 'içinde', '人': 'kişi', '有': 'sahip olmak', '我': 'ben', 
                    '他': 'o (erkek)', '这': 'bu', '个': 'birey', '中': 'orta', '为': 'için', '大': 'büyük', '们': 'çoğul', '来': 'gelmek', '上': 'üst', '以': 'olarak', 
                    '国': 'ülke', '和': 've', '到': 'varmak', '地': 'yer', '之': 'nin', '说': 'söylemek', '时': 'zaman', '要': 'istemek', '出': 'dışarı', '也': 'ayrıca', 
                    '就': 'sadece', '可': 'olabilir', '会': 'yetenekli olmak', '而': 'ancak', '于': 'içinde', '子': 'çocuk', '生': 'hayat', '对': 'doğru', '年': 'yıl', 
                    '能': 'yapabilmek', '得': 'almak', '你': 'sen', '下': 'aşağı', '自': 'kendisi', '道': 'yol', '那': 'o (işaret zamiri)', '后': 'sonra', '行': 'gitmek',
                    '着': 'halinde', '发': 'göndermek', '过': 'geçmek', '所': 'aslında', '用': 'kullanmak', '作': 'yapmak', '事': 'konu', '家': 'ev', '里': 'içinde', 
                    '成': 'olmak', '方': 'kare', '其': 'onun', '然': 'böylece', '种': 'tür', '去': 'gitmek', '如': 'gibi', '多': 'birçok', '经': 'geçmek', '法': 'hukuk', 
                    '学': 'öğrenmek', '同': 'aynı', '天': 'gökyüzü/gün', '都': 'hepsi', '分': 'bölmek', '当': 'olarak kabul etmek', '定': 'ayarlamak', '者': 'olan',
                    '进': 'girmek', '么': 'ek', '十': 'on', '主': 'ana', '日': 'gün', '动': 'hareket etmek', '部': 'bölüm', '现': 'şimdi', '面': 'yüz', '起': 'kalkmak',
                    '小': 'küçük', '理': 'yönetmek', '还': 'hala', '军': 'ordu', '与': 've', '看': 'görmek', '本': 'köken', '好': 'iyi', '无': 'olmadan', 
                    '前': 'önünde', '些': 'bazı', '没': 'olmamış', '心': 'kalp', '因': 'nedeniyle', '从': 'dan', '三': 'üç', '只': 'sadece', '实': 'gerçek',
                    '样': 'görünüş', '开': 'açmak', '此': 'bu', '公': 'kamu', '使': 'kullanmak', '将': 'olacak', '但': 'ancak', '意': 'fikir', '力': 'enerji', 
                    '民': 'insanlar', '二': 'iki', '长': 'uzun', '想': 'düşünmek', '它': 'o (dişi)', '机': 'makine', '知': 'bilmek', '又': 'tekrar', 
                    '第': 'numara', '明': 'parlak', '把': 'tutmak', '已': 'zaten', '工': 'iş', '正': 'doğru', '见': 'görüşmek', '性': 'cinsiyet', '她': 'o (dişi)',
                    '外': 'dışında', '业': 'sanayi', '关': 'kapatmak', '高': 'yüksek', '相': 'birbirini', '两': 'iki', '情': 'duygu', '全': 'tüm', '文': 'dil', 
                    '问': 'sormak', '等': 'beklemek', '由': 'yüzünden', '并': 'ayrıca', '月': 'ay', '应': 'olmalı', '间': 'arasında', '重': 'ciddi', '物': 'şey',
                    '政': 'siyaset', '点': 'nokta', '体': 'vücut', '战': 'savaş'}




def kelime_sayisi(cumle):
    # Verilen cümleyi boşluklardan bölerek kelimelere ayırın
    kelimeler = cumle.split()

    # Noktalama işaretlerini içeren bir string oluşturun
    noktalama_isaretleri = string.punctuation

    # Kelime sayısını tutacak bir değişken oluşturun
    sayac = 0

    # Her kelimeyi kontrol edin ve eğer sadece noktalama işareti içermiyorsa sayacı artırın
    for kelime in kelimeler:
        if kelime.strip(noktalama_isaretleri) != "":
            sayac += 1

    return sayac

