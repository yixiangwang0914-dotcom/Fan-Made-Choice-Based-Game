# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。


init python:
    renpy.music.register_channel("voice2", mixer="voice", loop=False)
    renpy.music.register_channel("voice3", mixer="voice", loop=False)
    renpy.music.register_channel("voice4", mixer="voice", loop=False)

    def history_voice_callback(event, interact=True, **kwargs):
        if event == "begin":
            path = kwargs.get("voice")
            if path is None:
                try:
                    path = renpy.music.get_playing("voice")
                except Exception:
                    path = None
            history_voice_paths.append(path)
    
    def cg_unlock(cg_id):
        """解锁一个CG"""
        if cg_id not in unlocked_cgs:
            if isinstance(unlocked_cgs, set):
                unlocked_cgs.add(cg_id)
            else:
                unlocked_cgs.append(cg_id)

        if not hasattr(persistent, "unlocked_cgs") or persistent.unlocked_cgs is None:
            persistent.unlocked_cgs = []
        elif isinstance(persistent.unlocked_cgs, set):
            persistent.unlocked_cgs = list(persistent.unlocked_cgs)
        try:
            if cg_id not in persistent.unlocked_cgs:
                persistent.unlocked_cgs.append(cg_id)
        except TypeError:
            persistent.unlocked_cgs = [cg_id]

define fang = Character("方知宥", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define worker = Character("刻珠匠人", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define who = Character(" ? ", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define wang_sheng = Character("王生", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define Li = Character("鹂儿", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define Lin =  Character("林翩翩", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define lin = Character("林悔儿", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define Jing = Character("景姨", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define su = Character("雁儿姐", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define yan = Character("苏连雁", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define narrator = Character(None, callback=history_voice_callback)
define sui = Character("满穗", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define hua = Character("琼华", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define child = Character("卖报纸的小孩", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define zg = Character("掌柜", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define black = Character("黑衣人", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define gj = Character("管家", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define momo = Character("嬷嬷", what_prefix="[[", what_suffix="]", callback=history_voice_callback)
define momo2 = Character("另一个嬷嬷", what_prefix="[[", what_suffix="]", callback=history_voice_callback)

label view_cg(cg_path, cg_name):
    """CG查看label"""
    call screen cg_view_display(cg_path, cg_name)
    return

# 游戏在此开始。

label start:

    scene black
    call chapter_template_0("images/库/warning.png") from _call_chapter_template_0
    # $ cg_unlock("cg_warning")
    # show chapter_title at chapter_title_pos
    # show chapter_subtitle at chapter_subtitle_pos
    call chapter_template_1("images/桥上幻景2.png") from _call_chapter_template_1

    
    scene 天空雨 with ink2
    play sound "白噪音/小雨.ogg" fadein 1.0 loop
    "崇祯十四年，盛夏。"
    "最近几日，雨一直在下。"
    "天空总是灰蒙蒙的，如丧夫的寡妇那般啜泣不休，泪落不止"
    "纷乱的雨打乱了我的作息，这些日子我常在白昼时入睡，却在深夜时方能醒来，且总会做些光怪陆离的噩梦。"
    "梦中，我常会见到一片海。"
    scene 雁归1 with fade
    "从小到大，我见过许多江河，却从未见过海。"
    "先前，我是从街边贩卖的图册中看过海，从茶馆的说书人那里听过海。"
    "在梦里，海洋像是无比大的秦淮河。"
    "它浩瀚到没有边际，广袤到没有边界，它与天空相接成一线，连西沉的落日都能吞噬。"
    "梦的起始之时，我总会看到雁儿姐。"
    scene 雁归2 with fade 
    "她在画舫之上，抱着琵琶弹奏，长裙与青丝随风飘动，身姿唯美，宛如被风吹动的画卷。"
    scene 雁归3 with fade 
    "画舫行驶在海面之上，水波荡漾，随着泛起的波涛一点点向着远处漂流而去。"
    scene 雁归4 with fade 
    "那画肪越来越远，起初如在面前，后来缩如拳头大小、继而是核桃大小、米粒大小，最后彻底看不见了。"
    "那琵琶声也越来越远，起初如在耳畔，后来如同蝉鸣，再而是如同蚊蝇，最后也是彻底寂静无声。"
    "我慌乱地想要叫住雁儿姐，想要去追赶画舫。"
    "可距离过远，她听不见。"
    "我也无法踏足海中，因此每次都只能眼睁睁地看她远去。"
    "这样的梦一连做了好几次。"
    "每次从这样的梦醒来，我都会猛地从被褥间挣脱而出，从床上坐起，双手颤抖，脸色苍白，冷汗浸透衣衫。"
    "我想摆脱噩梦给我带来的影响，便尝试以写作转移注意力，却更难写出一个字来。"
    "......"
    stop sound fadeout 1.0


#==================梦醒了===============
    scene 方院屋 with eye
    "我再次从那可怕的噩梦中醒来。"
    "......"
    "距离上次见到雁儿姐已经数月了。"
    "这段时间我几乎每隔几天就会去泠音阁。"
    "但每次都被景姨以种种理由拦下。"
    "近日我的心情也因为久久见不到雁儿姐而越发烦闷，甚至开始不吃不喝。"
    "明明上次的见面那么的愉快。"
    "我不禁又开始回想起上次见面时的情景。"

    play music "music/BGM/烟花风月.ogg" fadein 2.0

    scene black
    with fade
    pause 1.0   

    scene 茶舍日
    show 苏连雁 面纱微笑
    with fade
    pause 2.0

    scene 画舫内景昼
    show 苏连雁 面纱害羞
    with fade
    pause 2.0

    scene 东关街巷
    show 苏连雁 面纱说话
    with fade
    pause 2.0

    scene 宥雁相拥 with dissolve
    
    "她的眉眼音容，与我二人往昔相伴之景，在我心头反反复复，挥之不去。"

    stop music fadeout 2.0
    scene black with ink1
    
    "越是想她，心里便越像被什么反复揉碎翻搅，闷得人几乎喘不过气。"
    "罢了。"
    "出去透透气吧。"


#=====================东关街=============
    scene 东关街雨 at bg_leftbottom_to_center_restore with ink2
    play sound "白噪音/小雨.ogg" fadein 1.0 loop
    play sound "白噪音/东关闹市.ogg" fadein 1.0 loop
    "雨下得好大啊。"
    "但东关集的行人流不见半分冷清。" 

    "我漫无目的地在热闹的东关街转着。"
    "路过一家家无比熟悉的店铺。"
    "和林翩翩到访过的香囊店。"
    "曾与雁儿姐、林翩翩一同吃茶的那间茶舍。"
    "还有......"
    voice "配音/chapter1/匠人/匠人补1.wav"
    who "哎！小伙子"
    voice "配音/chapter1/匠人/匠人补2.wav"
    who "前几个月，是不是在这儿见过你。"

    "我猛地一回头。"
    "看见一个正在手拿磨石雕刻镯子的匠人正朝我招手。"
    "他是......"
    "是......"
    "是正是数月前雁儿姐和我托去打造手镯的那人匠人!"
    "忽然想起手镯我们还没有取来。"
    "于是我心下难得轻快了几分，抬步向他走去。"

    show 刻珠匠人
    with dissolve
    voice "配音/chapter1/匠人/audio.wav"
    worker "小伙子，怎么没和上次那个貌美的女子一同来啊？"
    fang "她近来事务繁多，抽不开身，自然也无暇陪我出来闲逛。"
    voice "配音/chapter1/匠人/audio (1).wav"
    worker "是嘛......" 
    voice "配音/chapter1/匠人/audio (2).wav"
    worker "那你是想来取手镯吗？" 
    "我心中很是疑惑。时隔数月，一个日日迎来送往、见惯无数客人的匠人，又怎会还记得我与雁儿姐的模样？"
    "但也不见怪，雁儿姐纵使戴着斗笠、遮了面容，单凭外形，也瞧得出是个世间少有的美人。"
    "于是我便很快打消了心中的疑惑, 点了点头。"
    fang "是的，我来取手镯了。"
    voice "配音/chapter1/匠人/audio (3).wav"
    worker "哦，那你来晚了，就在今日上午，有人帮你取过了。"
    "我听了这话，没搞懂什么意思。"
    fang "取过了？"
    voice "配音/chapter1/匠人/audio (4).wav"
    worker "是啊，上午有个姑娘来取了手镯。"
    "难不成是雁儿姐？"
    "雁儿姐不是得了风寒久久不能出门吗？"
    "她居然独自一人去取了手镯。"
    "她已经痊愈了？"
    "不可能......我前两日才去过泠音阁，景姨还告诉我她尚未痊愈。"
    "难道是景姨一直以来都在瞒我？"
    "雁儿姐早就大病初愈了？"
    "我心中充满了疑惑和不安。"
    fang "请问，今日清晨来取手镯的姑娘长什么样子？是上次来同我一起来这里的那个姑娘吗？"
    voice "配音/chapter1/匠人/audio (5).wav"
    worker "额......那个姑娘啊......"
    voice "配音/chapter1/匠人/audio (6).wav"
    worker "估计不是，上次与你同行的那个姑娘虽戴着斗笠，遮了面容，但气势不凡。"
    voice "配音/chapter1/匠人/audio (7).wav"
    worker "今日清晨前来取物的姑娘长相平平，更像是......"
    fang "更像是......?"
    voice "配音/chapter1/匠人/audio (8).wav"
    worker "更像是个丫鬟。"

    stop sound fadeout 1.0
    play music "BGM/重重墙囚.ogg" fadein 1.0 loop
    "丫鬟？"
    "鹂儿？"
    "我听了这话，心里顿时一沉。"
    "为什么，鹂儿怎么会来取手镯？"
    "一定是雁儿姐委托她来取的。"
    "一定是雁儿姐得了风寒不便出门，所以让鹂儿来取的。"
    voice "配音/chapter1/匠人/audio (9).wav"
    worker "哦对了，前来取物的姑娘神色不太对，感觉有些悲伤。"
    "悲伤，为何物会悲伤，难道是因为雁儿姐吗？"
    "这时，身后突然传来一熟悉的声音。"


#-----------王生来-------------
    stop music fadeout 1.0
    play sound "白噪音/小雨.ogg" fadein 1.0 loop
    play sound "白噪音/东关闹市.ogg" fadein 1.0 loop
    voice "配音/chapter1/王生/王补.wav"
    who "方小弟？"
    hide 刻珠匠人
    with dissolve
    "我猛地回头，看到一个身穿青色长衫的熟人正站在不远处。"
    show 少年王生 喜悦 with dissolve
    voice "配音/chapter1/王生/audio.wav"
    wang_sheng "方小弟,你怎么在这里？真是好久不见啊。"
    "......"
    "......"
    fang "好久不见......"
    "王生见我半天才从嘴里吐出一句话，便有些疑惑地看着我。"
    show 少年王生 震惊
    voice "配音/chapter1/王生/audio (1).wav"
    wang_sheng "方小弟，你怎么了？你看起来......脸色不太好啊。"
    fang "没什么，只是在向这位师傅询问一些事情。"
    voice "配音/chapter1/王生/audio (2).wav"
    wang_sheng "没事便好......"
    show 少年王生 震惊 at left_pos, not_speaking with move
    show 刻珠匠人 at 刻珠匠人_right_pos, speaking
    voice "配音/chapter1/匠人/audio (10).wav"
    worker "小伙子，老夫看你面色凝重，我猜一定与那位美貌的女子有关。"
    voice "配音/chapter1/匠人/audio (11).wav"
    worker "我记得今晨那姑娘来时，双眉紧锁，脸上几无血色，一副心事重重的模样。"
    show 刻珠匠人 at 刻珠匠人_right_pos, not_speaking
    show 少年王生 震惊 at left_pos, speaking
    voice "配音/chapter1/王生/audio (3).wav"
    wang_sheng "什么女子......"
    hide 刻珠匠人
    with dissolve
    

#---------匠人离开--------
    show 少年王生 疑惑 at origin_pos with move
    voice "配音/chapter1/王生/audio (4).wav"
    wang_sheng "难道你还在为那位泠音阁的花魁担心吗？"
    "王生说到这里，脸上露出了一丝凝重的笑容。"
    fang "是,是的......"
    "......"   
    voice "配音/chapter1/王生/audio (5).wav"
    wang_sheng "现在下着大雨，我们找间餐厅进屋说。"
    "我点了点头，跟着王生走进了东关街的一家包子铺。"






#---------包子店内--------
    stop sound fadeout 1.0
    scene 包子店 with ink3
    "我们找了个靠窗的位置坐下。"
    "王生没有绕任何弯子，直接开门见山。"
    play music "BGM/曲终人散.ogg" fadein 1.0 loop
    show 少年王生 通常 with dissolve
    voice "配音/chapter1/王生/audio (6).wav"
    wang_sheng "方小弟，你要的路引我已经帮你弄到了。"
    voice "配音/chapter1/王生/audio (7).wav"
    wang_sheng "花了我不少钱呢。"
    show inner_monologue_dim onlayer master 
    "路引......"
    "我想起了和雁儿姐约定的逃跑计划。"
    "与雁儿姐一同逃出青楼，逃出扬州，去到很远的地方。"
    "可是近些天来雁儿姐没有与我有任何上的联系了。"
    "逃跑计划也因为没有了联系而暂时搁置了。"
    "现在路引已经弄到了，这无疑是一个好消息。"
    "可是......"
    hide inner_monologue_dim
    show 少年王生 疑惑 
    voice "配音/chapter1/王生/audio (8).wav"
    wang_sheng "方小弟，恕我直言，这路引是为了那个花魁准备的吧。"
    "我心里一颤，却也并未太过惊讶。毕竟上回王生提起雁儿姐身染重病的传言时，我便已在他面前失了神色。"
    voice "配音/chapter1/王生/audio (9).wav"
    wang_sheng "最近听说她连客都不接了。"
    voice "配音/chapter1/王生/audio (10).wav"
    wang_sheng "少有人再见过她了。"
    voice "配音/chapter1/王生/audio (11).wav"
    wang_sheng "你备下这些东西，莫不是想带着她离开扬州，远走高飞？"
    fang "......"
    fang "正是。"
    "我有些不自信地回答道。"
    "但考虑到王生是我最亲近的友人，与他坦白也无大碍。"
    show 少年王生 愤怒
    voice "配音/chapter1/王生/audio (12).wav"
    wang_sheng "这几乎不可能实现。"
    "......"
    voice "配音/chapter1/王生/audio (13).wav"
    wang_sheng "先不说她乃扬州城中声名最盛的花魁，多少名士富商都盯着她、想替她赎身。单凭你的身份，若当真带着她私逃，只怕还未出扬州城，便要被人追回来了。"
    fang "......"
    voice "配音/chapter1/王生/audio (14).wav"
    wang_sheng "再者说，若外头那些传言当真不假，她既已病入膏肓，纵真逃出了扬州，只怕也撑不了多久。"
    fang "......"
    voice "配音/chapter1/王生/audio (15).wav"
    wang_sheng "你与她……只怕也剩不了多少相守的时日......"
    play sound "打击音效/AVG_107_B.ogg"
    scene 方王吵架 with fade
    $ cg_unlock("cg_wangfang")
    fang "胡说!!!"
    "我再也压制不住内心的情绪，猛拍桌子站了起来指着王生大骂道。"
    fang "你不配这么说她!!"
    fang "她一定没事的，那都是谣言！"
    fang "便是如此，我也一定要带她离开这里！哪怕拼上这一切，我也要让她过上自己想过的日子。"
    scene 方王吵架_2
    $ cg_unlock("cg_wangfang2")
    voice "配音/chapter1/王生/audio (16).wav"
    wang_sheng "你为什么这么肯定，这么肯定她就会情愿跟你走？！"
    fang "因为.....我们约定好的。"
    voice "配音/chapter1/王生/audio (17).wav"
    wang_sheng "那她又为何这段时间不愿见你?"
    fang "管事的景姨与楼里那些管事的人不肯放我进去。"
    scene 方王吵架_3
    $ cg_unlock("cg_wangfang3")
    voice "配音/chapter1/王生/audio (18).wav"
    wang_sheng "方小弟，你冷静想想。"
    voice "配音/chapter1/王生/audio (19).wav"
    wang_sheng "这些日子，当真只是景姨拦着你么。"
    show inner_monologue_dim onlayer master 
    "听到此话，我顿时冷静下来"
    "若是景姨从中作梗，倒还说得过去"
    "可若不是呢……"
    "若不是景姨。"
    "若是雁儿姐自己不愿见我……"
    "或许, 雁儿姐有自己未解开的苦衷不愿告诉我。"
    hide inner_monologue_dim
    scene 包子店 with fade
    show 少年王生 慌忙 with dissolve
    voice "配音/chapter1/王生/audio (20).wav"
    wang_sheng "哎......"
    voice "配音/chapter1/王生/audio (21).wav"
    wang_sheng "这扬州城里的勾栏瓦舍、花街柳巷，什么样的女子寻不得？你偏偏要去招惹个花魁。"
    "王生无奈地挤出一点笑容，便把手中的路引交给了我。"
    show inner_monologue_dim onlayer master 
    show 路引 with dissolve
    pause 3.0
    hide 路引
    hide inner_monologue_dim
    show 少年王生 微笑 
    voice "配音/chapter1/王生/王生.补补.wav"
    wang_sheng "罢了，人各有志，终归都有自己的缘由。"
    voice "配音/chapter1/王生/audio (22).wav"
    wang_sheng "只是，方小弟......"
    show 少年王生 愤怒
    voice "配音/chapter1/王生/audio (23).wav"
    wang_sheng "……你莫后悔便是。"
    "王生的眼里非常坚定......"
    fang "不会的。"
    "这句话是说给王生听的，也是说给我听的。"





    #=============一个人东关街沉思============
    stop music fadeout 1.0
    scene 东关街阴 with ink4
    pause 2.0
    "雨停了，因为临近傍晚，街上的人也少了起来。"
    "方才我与王生简单寒暄几句后，他便离去。"
    "我整理了一下思绪，并决定不能善罢甘休。"
    "我决定再去一次泠音阁。"
    "如今也顾不得许多，先去寻鹂儿问个究竟再说。"
    







    #===================泠烟阁找li儿=============
    scene 泠烟阁黄昏 with ink2
    play music "BGM/花街柳巷.ogg" fadein 1.5 loop
    "我又到了泠音阁。"
    "距离上次来还不到半月。"
    "可我心头那股异样之感，却愈发强烈起来"
    "越往前走，我心中那股不祥之感便越重，仿佛有什么事，正在一步步逼近。"
    "片刻，我便到了泠音阁的大门口。"
    scene 泠音阁大门黄昏 with fade
    "我站在楼下，望着那灯火辉煌的阁楼。楼中丝竹不断，觥筹交错，文人墨客们谈笑风生，个个都像活得潇洒自在。"
    "可我忽然觉得可笑。"
    "细想来，里面有几人真能超脱世俗？"
    "有人借诗词文章博名，有人借风月场所显雅，有人挥金如土。"
    "他们总爱把自己装点得清高又脱俗，仿佛来这烟花之地饮几杯酒、吟几首诗，便真成了什么风流人物。"
    "可是说到底，不过都是些贪恋名声、欲望与虚荣的人罢了。"
    "忽然我意识到......好像自己和心中所想的这类人也并无多少差别。"
    "我每次去见雁儿姐都和她畅聊诗文歌赋。"
    "和那些人一样。"
    "那时我只觉得，她懂我，我也懂她。"
    "可如今想起来，那些诗词歌赋，又能改变什么呢？"
    "我忽然觉得可笑。"
    "到头来，那些自以为高雅的东西，不过只是我拿来感动自己的玩意罢了。"
    "......"
    "我正为这些念头出神之际......"
    "大门口路过了一个熟悉的身影。"
    "那身形低着头，行迹鬼祟，仿佛心中藏着什么不可见人的事情。"
    "鹂儿？"
    scene 鹂儿回头 with fade
    $ cg_unlock("鹂儿回头")
    pause 1.5
    fang "鹂儿小姐！！"
    "我刚开口唤住她，她那原本躲躲闪闪的身影便猛地一顿，随即回过头来看向我。"
    voice "配音/chapter1/鹂/audio.wav"
    Li "方......方公子？"
    voice "配音/chapter1/鹂/audio (1).wav"
    Li "您......又来找怜烟小姐了吗？"
    voice "配音/chapter1/鹂/audio (2).wav"
    Li "方公子，怜烟最近身体还未恢复，还不能见客。"
    fang "不是的，我有话对你说。"
    scene 泠音阁大门黄昏 with fade
    show 鹂儿通常 with dissolve
    voice "配音/chapter1/鹂/audio (3).wav"
    Li "对我说？"
    fang "嗯。"
    voice "配音/chapter1/鹂/audio (4).wav"
    Li "什么话这么着急啊？"
    fang "......"
    "直接开门见山一定会惊动鹂儿，这样反而会适得其反。"
    "不如先寒暄几句。"
    fang "我就是想知道，怜烟小姐最近……还好吗？"
    voice "配音/chapter1/鹂/audio (5).wav"
    Li "你是指怜烟小姐的病情吗？"
    "我顺着鹂儿的话往下接。"
    fang "嗯。"
    show 鹂儿无奈
    voice "配音/chapter1/鹂/audio (6).wav"
    Li "小姐虽说只是患了风寒，除了日常行动不便并无大碍。"
    voice "配音/chapter1/鹂/audio (7).wav"
    Li "但....."
    voice "配音/chapter1/鹂/audio (8).wav"
    Li "只是近些日子，不太爱说话了。"
    fang "哦，那怜烟小姐最近有没有和你提起一些反常的事情。"
    fang "或者有一些反常的行为。"
    show 鹂儿试探
    voice "配音/chapter1/鹂/audio (9).wav"
    Li "方公子，这些是怜烟小姐的私事，不能对外头说的。"
    "见鹂儿不肯接着话题往下聊，我便直切主题。"
    "但直接问手镯的事情太直接，要变着法子问。"
    fang "对了。"
    fang "我上回与怜烟小姐同坐游舫的时候，买了对手镯，但那时走的太急忘了取。"
    fang "今日我去东关街时，碰见了那位刻镯子的匠人，便想去取。"
    fang "但那匠人说上午有人已替我去取了手镯。"
    fang "就是想询问一下，鹂儿小姐可否知道是谁前去帮我和怜烟小姐去取的。"
    show 鹂儿急切
    "鹂儿慌张的表情已经出卖了她。"
    "看来我没猜错，是雁儿姐指使鹂儿来取的手镯。"
    voice "配音/chapter1/鹂/audio (10).wav"
    Li "方公子可能问错人了吧......"
    voice "配音/chapter1/鹂/audio (11).wav"
    Li "奴婢并...并不知道。"
    "看来鹂儿小姐并不善于撒谎，我便乘胜追击给她下套。"
    fang "是鹂儿小姐取的吧。"
    fang "我都知道了。"
    voice "配音/chapter1/鹂/audio (12).wav"
    Li "不，不是我取的......"
    fang "怜烟小姐都告诉我了。"
    show 鹂儿无奈
    voice "配音/chapter1/鹂/audio (13).wav"
    Li "不可能！"
    voice "配音/chapter1/鹂/audio (14).wav"
    Li "怜烟小姐只与我说过这些。"
    fang "她亲自告诉我的。"
    fang "你自己已经把秘密说出去了。"
    fang "我刚才说的都是编的。"
    Li "......"
    fang "既然秘密已经守不住了，不如告诉我怜烟小姐为何委托鹂儿小姐去取那对手镯。"
    fang "无论怜烟小姐遇上什么事，我都会竭尽所能帮她。"
    show 鹂儿无奈
    voice "配音/chapter1/鹂/audio (15).wav"
    Li "不，你帮不了她。"
    fang "你这话……是什么意思？"
    scene 鹂儿回头_2 with fade
    $ cg_unlock("鹂儿回头_2")
    "鹂儿并没有回答我的问题，而是头也不回的向泠音阁里走去。"
    "我想要进去挽留她。"
    "可鹂儿小姐的神情异常笃定。"
    "我再冲进去怕也拦不住她，况且碰到景姨恐怕也会被以各种理由赶出去。"
    







    #===============无所事事===========
    stop music fadeout 1.0
    scene 泠烟阁黄昏 with fade
    "我又回到泠音阁大门前。"
    "计划算是泡汤了。"
    "虽然知道了是雁儿姐指使鹂儿去拿的手镯。"
    "但这也无法得出任何有用的结论。"
    "唉......"

    scene 天空黄昏 with wipe
    pause 1.5
    play music "BGM/孤风凄雨.ogg" fadein 1.5
    "我漫无目的地在这片繁华的青楼群中走着。"
    "找了一处没人的长椅便躺在上面开始发呆。"
    "若是往日，这时候我应当早已买好些时蔬，回去生火做饭；再不济，也会在外头草草吃上一顿，随后打道回府。"
    "可现在，我哪都不想去。"
    "至少不想离开这片繁华之地。"
    "因为我总觉得，心里像压着一锅将沸未沸的滚水，不住翻腾鼓荡，仿佛下一刻便要彻底炸开。"
    "回想了一下方才鹂儿的话语。"
    "忽然想到鹂儿提到了雁儿姐最近很少说话。"
    "难道是因为风寒？"
    "可如果真是这样为何当我提起手镯之事，鹂儿表现得那么反抗。"
    "而且她说我帮不了雁儿姐。"
    "若是寻常风寒，我大可以替她请来名医诊治。"
    "若只是心里烦闷，我大可以替她寻些她喜欢的东西送过去，陪她解闷。"
    "若是因为被景姨阻拦无法与我出逃......"
    "不对，难道鹂儿已经得知了我和雁儿姐出逃的计划了？"
    "难道雁儿姐告诉她了？"
    "想着想着，我便睡意朦胧。"
    "不知不觉间，我竟昏沉沉睡了过去。"

    scene 雁归4 with ink2
    "我又梦到了那个可怕的梦。"
    "这次，梦的场景依然是海，眼前却没有画舫了。"
    scene 雁归5 with fade
    "空旷的海面上沉寂了许久，突然有一只鸿雁，破水而出，从海水中窜了出来。"
    "它展翅腾飞，飞向了天空，向着大海尽头的红色落日飞去，越飞越高，也越飞越远。"
    "无论我如何呼唤。"
    "它都没有停下来的意思。"
    "那鸿雁就好似雁儿姐一般，渴望着自由，渴望着幸福。"
    "雁儿姐......"
    "雁......"
    stop music fadeout 0.5









    #===================被叫醒（林翩翩）======================
    scene black with dissolve
    voice "配音/chapter1/林/林补.wav"
    who "知宥!"
    "正当我沉浸在梦里无法自拔的时候，听到远处仿佛有人在呼唤我。"
    "我被迫缓缓睁开双眼，眼前是早已暗淡无光的天空"
    scene 天空夜 with eye 
    "谁......"
    "雁儿姐?"
    voice "配音/chapter1/林/audio.wav"
    who "知宥，你怎么在这里睡觉。"
    "声音虽轻柔，却并不显得柔弱，反倒透着一股生气与活泼劲儿。"
    "与雁儿姐完全不同。"
    "我慵懒地坐起身来从长椅上站起。"
    scene 西商街夜 with dissolve
    show 小林 好奇 with dissolve
    play music "BGM/吟诗作对.ogg" fadein 1.0
    voice "配音/chapter1/林/audio (1).wav"
    Lin "知宥，好巧啊，没想到又能在这里碰到你。"
    fang "翩翩？"
    "她那灵动而带着几分娇俏的声音，像是一下子将我从方才的噩梦里生生拽了回来。"
    voice "配音/chapter1/林/audio (2).wav"
    Lin "你在这里做什么？"
    fang "哦，我……我刚才闲来无事，便到这边随意走走。谁知困意忽然上来，不知不觉竟睡着了。"
    voice "配音/chapter1/林/audio (3).wav"
    Lin "闲来无事？"
    voice "配音/chapter1/林/audio (4).wav"
    Lin "知宥，你平常闲来无事的时候总是会来花街吗？"
    fang "倒也没有。"
    voice "配音/chapter1/林/audio (5).wav"
    Lin "没有？"
    show 小林 兴奋
    "她微微眯起眼，忽然笑了。"
    voice "配音/chapter1/林/audio (7).wav"
    Lin "我看你呀，多半又是在外头胡乱招惹姑娘，惹得人家伤心了吧。"
    fang "在你眼里，我就这么不知廉耻吗？"
    voice "配音/chapter1/林/audio (8).wav"
    Lin "嘿嘿开个玩笑啦。"
    fang "......"
    show inner_monologue_dim onlayer master 
    "沉默中，我注视着林翩翩那水灵的大眼睛。多日未见她还是那么开朗乐观。"
    "在那种最下等的风月场里，活着本就是件难事。"
    "不……与其说是活着，倒不如说只是拼命挣扎着求生。"
    "大多数人每日光是顾着填饱肚子、少挨几顿打，便已经耗尽了全部力气，哪里还有余力去照看别人。"
    "明明身处那种地方，林翩翩却仍是一副无忧无虑的模样，仿佛什么烦心事都压不垮她。"
    hide inner_monologue_dim
    "林翩翩先打破了沉默和我的思考。"
    show 小林 开心
    voice "配音/chapter1/林/audio (9).wav"
    Lin "给，看你这大晚上的刚睡醒，肯定饿坏了吧。"
    voice "配音/chapter1/林/audio (10).wav"
    Lin "尝尝。"
    scene 林糖葫芦 with fade
    $ cg_unlock("林糖葫芦")
    fang "这是？"
    voice "配音/chapter1/林/audio (11).wav"
    Lin "糖葫芦！吃过没？"
    fang "吃倒是吃过。"
    voice "配音/chapter1/林/audio (12).wav"
    Lin "刚做好买的，快吃。"
    fang "那就多谢翩翩了。"
    scene 林糖葫芦_2 with dissolve
    $ cg_unlock("林糖葫芦_2")
    "说着，我接过那糖葫芦便没有犹豫的咬了一口。"
    "甜味在嘴里慢慢化开，许久未曾进食的口舌早已干涩发麻，如今骤然尝到些甜头，心里都跟着松快了几分。"
    fang "好吃！"
    "我发自内心的夸赞到。"
    "翩翩也咬了一口回应道。"
    voice "配音/chapter1/林/audio (13).wav"
    Lin "嗯！确实好吃，这家老板的手艺真不错，吃的我都想流泪了。"
    voice "配音/chapter1/林/audio (14).wav"
    Lin "知宥，下次有空了我一定带你去尝尝这老板做的其他好吃的。"
    fang "好，好，你带我去。"
    voice "配音/chapter1/林/audio (15).wav"
    Lin "嘿嘿，一言为定。"
    "看着她那天真无邪的笑容，我又开始想......"
    "林翩翩好似把所有的喜怒哀乐都写在了脸上。"
    "非常好懂。"
    "我其实十分羡慕她。"
    "能从底层游娼那种吃人不吐骨头的地方苟活下来，又一步一步凭着自己的努力爬进花街……林翩翩远比我想象中要坚强和乐观。"
    "若换作是我，恐怕早就死在那种烟花柳巷里了，连替我收尸的人都不会有。"
    "林翩翩再次主动打破了我的沉默。"
    "她暂时放下手中正在品尝的糖葫芦。"
    scene 西商街夜 with dissolve
    show 小林 好奇 with dissolve
    voice "配音/chapter1/林/audio (16).wav"
    Lin "哦对了，你最近不是常去找怜烟小姐吗。"
    "听到雁儿姐的名字，我下意识的一皱眉。"
    fang "嗯。"
    voice "配音/chapter1/林/audio (17).wav"
    Lin "你......和她怎么样了。"
    fang "还可以，我们相处的挺融洽的。"
    "我也只能这样回答。"
    "毕竟不可能把今日发生的事情和我心中所想告诉她。"
    show 小林 羡慕 
    voice "配音/chapter1/林/audio (18).wav"
    Lin "那好吧......"
    "她好像从我的话中听出来我不是很想回答这个问题"
    show 小林 开心
    voice "配音/chapter1/林/audio (19).wav"
    Lin "对了，还有一件事。"
    voice "配音/chapter1/林/30_林翩翩_005.ogg"
    Lin "我想买一件新衣服，因为最近又有好事情发生了。"
    "她微微一笑，嘴角勾出了一个梨涡。"
    fang "哦？"
    voice "配音/chapter1/林/30_林翩翩_006.ogg"
    Lin "我在花街有了些名气，有一家青楼的头牌姐姐看上了我，约好明年让我去她那里做侍女。"
    fang "听着不错啊，记得你先前说过通常要在花街待上三年才能进青楼，不过这样也挺好。"
    voice "配音/chapter1/林/30_林翩翩_007.ogg"
    Lin "是啊，挺好的，侍女虽然卑微，不能挑选客人......但至少每日只需接一客，一般客人也更礼貌，有更多银子，一会顺路的话，我们一起去看看？"
    fang "啊哈，我今日过于疲惫，改天定陪你去。"
    "我实话实说。"
    voice "配音/chapter1/林/audio (20).wav"
    Lin "知宥，过两天你陪我去买新衣服吧。"
    fang "好啊，没问题。"
    "我爽快地答应了她。"
    voice "配音/chapter1/林/audio (21).wav"
    Lin "太好了！嘿嘿！"
    "林翩翩听到我的回答像是被奖赏的孩童般笑着。"
    "时间过得真快。"
    hide 小林 开心 with dissolve
    "我还记得，初遇之时，她还是在柳巷站街的游娼。"
    "没过几年，就从柳巷被调到了花街，明年更是要去一家青楼做侍女了。"
    "有朝一日，她也一定会成为某家青楼的头牌。"
    "关于她的一切仿佛都在变好。"
    "反倒我现在一直在原地踏步。"
    "明明将来定要写出一本名动天下的小说。可几年过去了，到头来却连故事都还卡在开篇。"
    "明明想要带着雁儿姐实现她的梦想，一起逃走。"
    "可现在却连雁儿姐自己究竟怎么想的还搞不清楚。"
    "......"
    "那个一直存在于我心中的雁儿姐，究竟是真正的她，还是只是我自己想象出来的模样？"
    "我心中一直坚信的那些事，或许打一开始就是错的。"
    "那若是这样......"
    "站在我面前的林翩翩，我又怎么笃定我是了解她的。"
    "想到这里，我越发感到郁闷。"
    "若是这样......"
    "眼前每天把笑容挂在脸上的少女，她平日里总是一副笑盈盈的模样，可我忽然觉得，那笑容背后，或许也压着不少不愿让人知道的苦楚。"
    "这苦衷或小或大。"
    "越想我的脑子越混乱。"
    fang "你真的喜欢这样的生活吗？"
    show 小林 惊讶 at char_shake
    "那句话几乎是下意识脱口而出的。"
    "待我反应过来时，连自己都觉得有些荒唐。大概是这些时日思虑过重，又饿得太久，竟让我一时间连脑子都有些不清醒了。"
    "可在我意料之外的是，林翩翩居然也露出惊讶的表情。"
    show 小林 疲惫
    Lin "......"
    fang "......"
    "场面一度变得非常尴尬，我们互相沉默着，不知说什么可好。"
    "难不成......真被我说中了？"




    #=======================鹂儿急切===========================
    hide 小林 疲惫 with dissolve
    stop music
    "忽然，尴尬的气氛被一个急切而极具冲击力的声音打破了。"
    voice "配音/chapter1/鹂/audio (16).wav"
    who "方公子!!不好了......!"
    "这声音震耳欲聋，同时惊起了我和林翩翩的注意，我们望向声音来的方向。"
    voice "配音/chapter1/鹂/audio (17).wav"
    who "方公子!,出事了！"
    voice "配音/chapter1/鹂/audio (18).wav"
    who "怜烟小姐不见了！"
    show 西商街夜 at bg_shake
    pause 0.16
    "......什......什么？"
    "听见这句话，我方才还昏昏沉沉的脑子，顿时像被一盆冰水当头浇下，整个人骤然清醒过来。"
    "那声音是来自鹂儿的，她急匆匆地跑到我跟前，好像发生了什么大事。"
    show 鹂儿急切 with dissolve
    play music "BGM/重重墙囚.ogg"
    fang "你......你方才说什么？"
    voice "配音/chapter1/鹂/audio (19).wav"
    Li "我找不见怜烟小姐了......"
    fang "为什么...怎么会这样。"
    voice "配音/chapter1/鹂/audio (20).wav"
    Li "是这样的。奴婢黄昏时同公子说完话后，心里多少有些不痛快，便回了泠音阁打扫屋子。"
    voice "配音/chapter1/鹂/audio (21).wav"
    Li "公子说得不错。怜烟小姐今晨的确吩咐奴婢去取那只手镯，只是……奴婢并未将它交到小姐手中。"
    fang "那你把手镯放哪里了？？"
    voice "配音/chapter1/鹂/audio (22).wav"
    Li "我按照怜烟小姐的要求放到了东关集市的一家当铺里面，转让给了当铺的老板保管。"
    "我心里有着十万个不解。"
    fang "为什么要这么做？"
    show 鹂儿无奈 
    voice "配音/chapter1/鹂/audio (23).wav"
    Li "具体原因，奴婢也不知道。"
    voice "配音/chapter1/鹂/audio (24).wav"
    Li "只是……怜烟小姐在昨日吩咐奴婢做这些事的时候，神情明显不大对劲。她像是十分悲伤，又像是在刻意逃避什么。"
    voice "配音/chapter1/鹂/audio (25).wav"
    Li "还有就是......怜烟小姐还特地吩咐奴婢若路上遇到您，切记不要搭话，更不要告诉你她委托我办的事情。"
    voice "配音/chapter1/鹂/audio (26).wav"
    Li "奴婢问小姐原因，她只是回了句“我近日不想见他”。"
    "听到这话，我心头一紧，表情也愈发凝重。"
    "雁儿姐......不想见我？"
    "鹂儿没有停下，继续说道。"
    voice "配音/chapter1/鹂/audio (27).wav"
    Li "奴婢以为方公子您在与怜烟小姐近期交谈的时候伤了小姐的心。所以......黄昏时刻的时候才不待见您。"
    voice "配音/chapter1/鹂/audio (28).wav"
    Li "甚至……今晨奴婢去取东西之前，本想先替怜烟小姐打扫闺房。可才走到门外，便听见屋里传来小姐的哭声……"
    voice "配音/chapter1/鹂/audio (29).wav"
    Li "奴婢虽心中担忧，却也没敢贸然进去打扰……直到一个时辰前，奴婢实在放不下心，这才过去查看。可没想到……小姐竟已经不见了。"
    show inner_monologue_dim onlayer master 
    "按照青楼里的规矩，花魁这样的人物在这个时段是绝对不得私自离开闺房的。"
    "可雁儿姐却独自离去..."
    "我忽然想起，鹂儿曾说过，雁儿姐这些日子一直沉默寡言，神情也总是郁郁的。更奇怪的是，她在让鹂儿取回那只手镯后，竟又将其留在了那家名叫“渡芦”的当铺。"
    "这一切怎么看，都不像是寻常之举。"
    "刹那间最坏的想法从我脑中闪过。"
    "莫非，雁儿姐因久病不能痊愈产生了轻生的念头？"
    "绝无可能。雁儿姐那样向往自由、又那般勇敢坚强的人……绝不可能生出这种念头。"
    "还有那句让我心无比绞痛的“我近日不想见他”到底是什么意思。"
    "不对，不对，现在可不是想这些的时候。"
    "当务之急是要先寻回雁儿姐。"
    hide inner_monologue_dim
    fang "鹂儿小姐，除了你之外，可还有别人知道这件事？"
    voice "配音/chapter1/鹂/audio (30).wav"
    Li "没有，奴婢是第一个发现的，还没有告知其他人，因为..."
    voice "配音/chapter1/鹂/audio (31).wav"
    Li "此事若叫旁人知道了，尤其是景姨……奴婢定会因照顾不当被推去担大半责任。到那时候，莫说在阁里待不下去，只怕连官府那边都免不了要问罪。"
    "确实，若让旁人知道此事，鹂儿必然逃不过责罚"
    fang "那，能否带我去怜烟小姐的闺房查看一番。"
    fang "现在也只有在那里可以得知怜烟小姐的真实意图。"
    fang "说不定我可以帮上忙在房间里找到些重要线索，以便更快地找到怜烟小姐。"
    "鹂儿并无它法，只好无奈地答应。"
    voice "配音/chapter1/鹂/audio (32).wav"
    Li "好。"
    voice "配音/chapter1/林/audio (22).wav"
    Lin "那...那个......"
    hide 鹂儿急切
    show 鹂儿无奈 at slide_right_Li, not_speaking
    show 小林 疲惫 at slide_to_left_pos, speaking
    voice "配音/chapter1/林/audio (23).wav"
    Lin "我能跟你们一起去吗。"
    voice "配音/chapter1/林/audio (24).wav"
    Lin "说不定我能帮上什么忙。"
    "我缓过神才意识到林翩翩一直在旁边站着并且听到了我们说的每一个字。"
    "罢了，林翩翩也不算外人。"
    "多一个人帮忙总不是坏事。"
    fang "你当真确定？这件事关系重大，可容不得半点差错。"
    show 小林 惊讶
    voice "配音/chapter1/林/audio (25).wav"
    Lin "放心吧，知宥的事情就是我的事情，我觉得不会给你们添麻烦的！"
    "瞧着她那如此坚定的眼神，我便同意了。"
    fang "好，你跟我们一起。"
    show 三人狂奔 with fade
    $ cg_unlock("三人狂奔")
    play sound "打击音效/Se_BengPao.ogg" 
    pause 2.0
    "我同鹂儿和林翩翩一起沿着花街狂奔着。" 
    "街道两旁依旧灯火璀璨。楼阁里的丝竹声、酒客们的笑谈声、姑娘们招揽客人的娇笑声混在一起，热闹得仿佛整座扬州城都沉浸在一场不会醒来的梦里。"
    "可那些声音落在耳里，却只让我觉得烦躁。"
    "越往前跑，那股莫名的不安便越发强烈，仿佛有什么东西正在一点点压下来，压得我几乎喘不过气。"
    "我开始控制不住地胡思乱想。"
    show inner_monologue_dim onlayer master 
    "雁儿姐如今会在哪？她为什么偏偏要在今日突然离开？她把手镯留在当铺，到底是什么意思？"
    "无数念头像乱麻般缠在一起，搅得我胸口发闷。"
    "我甚至不敢让自己停下来细想。"
    "仿佛只要慢上一点，那最坏的结果便会立刻追上来一般。"
    scene 花街 with fade 
    "我们顺着灯火通明的花街一路奔去。" 
    pause 2.0
    scene 柳巷 with fade 
    "途中，我们还经过了那片远比花街破败阴暗的柳巷。"
    pause 2.0
    scene 泠音阁夜晚 with fade
    "没过多久，便又到了那座囚了雁儿姐半生的阁楼前。那地方于旁人而言是温柔富贵乡，于她而言，却不过是一副怎么也挣不开的枷锁。"
    "若雁儿姐心中所想……当真与我想的一样:她不想一生只能任人摆布，只想作为一个”人“活过。那无论如何，我也一定会带她一起逃离这里。"
    "但恐怕事实不是这样......"
    


    #============================大门计划===================
    scene 泠音阁大门夜晚 with ink3
    "我们一行人急慌慌地冲到了泠音阁大门前。"
    "我找了一处人少的地方先喘了几口气，然后便开始协商之后的计划。"
    show 小林 微笑 at Lin_left with dissolve
    show 鹂儿无奈 at Li_right with dissolve
    fang "现在是不得贸然闯进怜烟小姐的闺房的吧。"
    show 鹂儿无奈 at Li_right, speaking
    show 小林 微笑 at Lin_left, not_speaking
    voice "配音/chapter1/鹂/audio (33).wav"
    Li "是的，现在已经过了怜烟小姐接客的时间，除了奴婢和其他侍奉的仆人，任何人不得进出。"
    fang "也就是说现在知宥鹂儿小姐你可以随意进出。"
    voice "配音/chapter1/鹂/audio (34).wav"
    Li "即便是我也要得到小姐的同意，但这一点现在倒也无所谓。"
    fang "......"
    fang "只有鹂儿小姐一个人进去是不够的。"
    fang "要不我们可以偷偷摸进去。泠音阁终究不是什么官府重地，也不是军营禁所，不至于有人日夜严防死守，只要我们小心一些，想悄悄溜进去……应当并非难事。"
    voice "配音/chapter1/鹂/audio (35).wav"
    Li "道理是可行的，这个时辰，楼里那些看门的多半早已困得发昏，只要小心一些，未必发现得了我们。可麻烦的是……若途中撞上爱四处巡阁的景姨，那便麻烦了。"
    "也是......"
    "听说景姨平日里警觉得很，几乎每隔半个时辰便要亲自巡视一遍整座阁楼。生怕楼里出现些见色起意的下人，污了阁中那些艺妓的清白与名声。"
    show 鹂儿无奈 at Li_right, not_speaking
    fang "现在时间紧迫，没时间想一些更加细致的计划了，不如放手一搏。"
    show 小林 微笑 at Lin_left, speaking
    voice "配音/chapter1/林/audio (26).wav"
    Lin "那......那个。"
    "林翩翩好像要说什么，我和鹂儿同时看向她。"
    voice "配音/chapter1/林/audio (27).wav"
    Lin "若是路上真的遇到了你们口中的景姨，我可以帮你们引开她，虽然未必能拖住多久，但多少也能替你们争取些时间。"
    "我想都没想直接反驳道。"
    fang "不可能，我们怎能让你一个弱女子替我们去冒这种风险。"
    show 小林 惊讶 at Lin_left, speaking
    voice "配音/chapter1/林/audio (28).wav"
    Lin "知宥，我从来都不是你口中所说的“弱女子”，要不要去冒这个险，是我自己的选择，不是你说了算。"
    "听到这话我才发觉方才我说错了话......林翩翩这样在淤泥中还能绽放的花朵，怎么被称为“弱”。"
    show 小林 幽怨 at Lin_left, speaking
    voice "配音/chapter1/林/audio (29).wav"
    Lin "在二十四桥摸爬滚打这么多年，我早已不是那个遇到苦难只会哭鼻子，吆喝着跳河的那个女子了。"
    voice "配音/chapter1/林/audio (30).wav"
    Lin "我这辈子从来没有真正为别人做过事情。"
    voice "配音/chapter1/林/audio (31).wav"
    Lin "知宥，这一次我想为了你做件事情。"
    "我听她这么说，内心也被她说服了。"
    "我又不禁想要问出刚才在花街时没有得到她回答的问题......来验证林翩翩的内心所想是否和我想得一样。"
    "但现在不是时候。"
    fang "也罢。"
    fang "那就按你说的办好了。"
    "我声音非常低沉，好似听不见。"
    voice "配音/chapter1/林/audio (32).wav"
    Lin "嗯。"
    "她的这一声倒显得很有气势......"



    #==========================潜行=====================
    scene black with fade
    "说着，我们便按照计划悄无声息地进入了泠音阁。"
    scene 四艺堂长廊 at bg_leftbottom_to_center_restore with fade
    pause 3.0
    "穿过大门，几步距离便是四艺堂长廊，每次来见雁儿姐的必经之路。"
    "我们一行人小心前进，尽量不发出太大动静引来门卫。"
    "这条长廊说长不长，因为从阁楼前头走到后门，其实也不过片刻功夫；可说短却也不短，只因其中回廊交错、弯弯绕绕，稍不留神便容易迷了方向。"
    "途中穿过了我与雁儿重逢第一次相见在四艺堂用来招待客人的小间。"
    "回忆也逐渐浮上心头。"
    "可现在并不是意淫的时候。"
    "我们需要尽快知道雁儿姐的下落......"
    "就在这时......"
    show 四艺堂长廊 at bg_shake
    "我们最不想要发生的事情发生了。"
    "景姨不知何时出现在了我们斜对面，她正不急不慢地朝着我们这边走来。"
    "我们三人后无退路，前也不通，唯一的一条道路已被景姨挡的结结实实。"
    "况且这狭长的通道没有任何障碍物，两边窗门紧闭也打不开。"
    "难道只能......"
    voice "配音/chapter1/林/audio (33).wav"
    Lin "没事，交给我吧。"
    "一道细微的声音忽然自耳边传来。"
    fang "注意安全，多保重。"
    "说着林翩翩便毫不犹豫地大步向景姨走去。"
    show 四艺堂长廊 at center_restore
    "我和鹂儿蹲在原处，静等林翩翩把景姨引开。"
    "隐约可以听到林翩翩和景姨交谈的声音。"
    voice "配音/chapter1/林/audio (34).wav"
    Lin "景姨你好。"
    voice "配音/chapter1/景姨/audio.wav"
    Jing "嗯？你是哪个丫头？"
    voice "配音/chapter1/林/audio (35).wav"
    Lin "我是今日新来的，方才给今日最后一位客人送酒时迷了路，绕了半天都没绕出去。"
    voice "配音/chapter1/景姨/audio (1).wav"
    Jing "新来的？"
    voice "配音/chapter1/景姨/audio (3).wav"
    Jing "我怎么从未见过你。"
    voice "配音/chapter1/林/audio (36).wav"
    Lin "奴婢白日里一直在后院帮忙，是景姨您忙着招待贵客，没注意到奴婢也正常......"
    "她说这话时语气自然得厉害，连我都险些真以为她是阁中新来的丫头。"
    "我不由得屏住呼吸。"
    "直到这一刻，我也意识到......林翩翩不仅比我想得更勇敢，乐观，还比我想象中更加聪明。"
    "她不仅没有半点慌乱，甚至连语气中的轻重缓急都拿捏得极好。"
    voice "配音/chapter1/景姨/audio (2).wav"
    Jing "那你工作都结束了，还在这里瞎转悠什么？"
    voice "配音/chapter1/林/audio (37).wav"
    Lin "我有点迷路，阁里太大了，我刚来不熟路。"
    voice "配音/chapter1/景姨/audio (4).wav"
    Jing "既然迷路了，为何不去问别人？"
    voice "配音/chapter1/林/audio (38).wav"
    Lin "奴婢......因不认得路，怕手忙脚乱冲撞了楼里的客人。"
    "景姨皱着眉上下打量着林翩翩。"
    "我的心也跟着一点点提了起来。"
    "若此刻被景姨发现端倪，我们三人今晚恐怕谁都走不出去。"
    "可林翩翩却依旧站得笔直。"
    "她甚至还朝景姨轻轻笑了一下，那副模样，竟看不出半点心虚。"
    voice "配音/chapter1/景姨/audio (5).wav"
    Jing "行了。"
    voice "配音/chapter1/景姨/audio (6).wav"
    Jing "既然是新来不久的，我带你去后院找管事嬷嬷。"
    voice "配音/chapter1/景姨/audio (7).wav"
    Jing "以后长点心啊。要不然抽你。"
    voice "配音/chapter1/林/audio (39).wav"
    Lin "是，是，以后一定更加注意，多谢景姨。"
    "说着，林翩翩向另一侧长廊走了过去。"
    "景姨也跟着她慢慢转过了身。"
    "我与鹂儿对视一眼。"
    "机会来了。"



#=======================雁儿姐闺房===========================
    stop music
    scene 花魁房间 with wipe
    "我和鹂儿没有浪费林翩翩争取的时间。"
    "非常迅速地抵达了雁儿姐的闺房。"
    "很幸运，这一路我们并没有遇到任何的危险。"
    "雁儿姐的房间依旧一尘不染。"
    "房间内安静的可怕，除了烛火偶尔发出的轻微爆响外，四周竟静得像断了气一般，听不见半点声音。"
    show 鹂儿无奈 with dissolve 
    voice "配音/chapter1/鹂/audio (36).wav"
    Li "方公子，我们赶紧调查一下怜烟小姐的房间吧。"
    fang "嗯，事不宜迟，要赶快了。"
    voice "配音/chapter1/鹂/audio (37).wav"
    Li "对了，拿东西尽量轻拿轻放，我不想弄坏怜烟小姐的东西......"
    fang "好，没问题。"
    "这也不奇怪，毕竟鹂儿不想因这件事情影响到自己的工作。我们的行动要越隐秘越好。"
    hide 鹂儿无奈 with dissolve
    $ 查过梳妆台 = False
    $ 查过门窗 = False
    $ 查过香踏 = False
    $ 查过案几 = False
    $ 查过书架 = False


    label 调查房间:
        scene 花魁房间 at orgin_restore

        if 查过梳妆台 and 查过门窗 and 查过香踏 and 查过案几 and 查过书架:
            jump 调查结束

        menu:
            "调查梳妆台" if not 查过梳妆台:
                $ 查过梳妆台 = True
                show 花魁房间 at center_restore
                "绕过屏风，我走到雁儿姐平日休息之处。"
                "那张精美的拔步床床铺平整地伫立在那里。"
                "我走到侧边的梳妆台边上。"
                "梳妆台收拾得很整齐。"
                "台前的木制坐墩，铜镜和胭脂水粉等化妆物品摆放非常整齐。"
                "我仔细勘察了一番，发现并没有什么可疑之处。"
                jump 调查房间

            "调查门窗" if not 查过门窗:
                $ 查过门窗 = True
                show 花魁房间 at right_restore
                "我走到那扇可以打开的檀香木门边上。"
                fang "鹂儿小姐，可否帮我打开这扇。"
                voice "配音/chapter1/鹂/audio (38).wav"
                Li "这就来。"
                show 花魁房间夜 at right_stable
                "拉开帘幔，泠音阁夜晚的湖光水色被我一览无余。"
                "明月高悬，星灿作伴，水天一色。"
                "想到雁儿姐曾在这里为我弹过古琴。"
                "那时的美妙的情景即便到现在也难以忘怀..."
                "......"
                "我仔细调查了门窗有无痕迹和污渍。"
                "令人失望的是一番调查下来一无所获......"
                "仔细想想便知道，雁儿姐身体纤细柔弱，怎会通过这门窗逃离阁楼。"
                
                jump 调查房间

            "调查香炉" if not 查过香踏:
                $ 查过香踏 = True
                show 花魁房间 at center_restore
                "香炉中的熏香还残留着的香气。"
                "可房间里也因它而飘一股淡淡冷香。"
                "那是雁儿姐身上常有的味道。"
                "......"
                "这香气......居然还未散尽。"
                fang "鹂儿小姐，你何时为怜烟小姐点的香？"
                voice "配音/chapter1/鹂/audio (39).wav"
                Li "今日清晨雁儿姐托福我取手镯之时。"
                "按照这个香炉的大小, 已过去十五小时香气还未散尽。"
                "这也就代表雁儿姐应该离开这里没有太久。"
                jump 调查房间

            "调查案几" if not 查过案几:
                $ 查过案几 = True
                show 花魁房间 at center_restore
                "我走到雁儿姐平日用来研墨写字的案几。"
                "案几上陈列着茶壶和茶杯，无不摆放规整。"
                "整个案几都被擦拭的无比干净......"
                "好似什么都没发现..."
                "正当我觉得这里没有线索的时候，我无意识地翻到了在案几下方的一个秘密隔层。"
                "里面存放着一本书。"
                show 忆-梁祝 with dissolve
                "书名叫.......《梁祝》"
                "烛火映照下，那泛黄书页显得格外安静。"
                "我怔怔望着那本书，一时间竟有些失神。"
                "梁山伯与祝英台......"
                "雁儿姐平日虽也爱看些话本，可为何这本书会被藏于如此隐秘之位置。"
                "难道这本书有什么含义......"
                "是雁儿姐想要让我知晓的含义......"
                "罢了，先调查其他地方再说。"
                "说着，我便把这本书放进自己的衣袋里。"
                jump 调查房间

            # "调查书架" if not 查过书架:
            #     $ 查过书架 = True
            #     show 花魁房间 at left_restore
            #     "书架上整整齐齐摆着不少诗集与八股时文。"
            #     "那些大抵都是楼里请先生教她们读书时留下的东西。毕竟像雁儿姐这样的花魁，琴棋书画、诗词文章，总归都是要学的。"
            #     "可与那些几乎没怎么翻动过的八股文章相比，另一侧的话本小说却明显旧得多"
            #     "《西游记》、《牡丹亭》，甚至连《金瓶梅》这样的禁书都混在其中。"
            #     "有些书页边角甚至已经被翻得微微卷起。"
            #     "比起那些满口圣贤道理的文章，雁儿姐显然更喜欢这些“离经叛道”的故事。"
            #     "我原本只是随意扫了一眼。"
            #     "可就在转身时，一本夹在角落里的书忽然吸引了我的注意。"
            #     "那是一本《西游记》，却和刚才哪一本不同。"
            #     "书页明显比周围其他书旧上许多，像是被人反复翻阅过。"
            #     "我伸手将其取下"
            #     "可当我翻开时，我却忽然愣住了。"
            #     "整本书都是雁儿姐字迹组成，书中的许多地方，竟都被人用极娟秀的小字仔细做了批注。"
            #     jump 调查房间

    label 结束调查:
        menu:
            "调查书架":
                show 花魁房间 at left_restore
                play music "BGM/明末_心近之刻_可循环.ogg" fadein 2.0 loop
                "书架上整整齐齐摆着不少诗集与八股时文。"
                "那些大抵都是楼里请先生教她们读书时留下的东西。毕竟像雁儿姐这样的花魁，琴棋书画、诗词文章，总归都是要学的。"
                "可与那些几乎没怎么翻动过的八股文章相比，另一侧的话本小说却明显旧得多。"
                "《水浒传》、《牡丹亭》，甚至连《金瓶梅》这样的禁书都混在其中。"
                "有些书页边角甚至已经被翻得微微卷起。"
                "比起那些满口圣贤道理的文章，雁儿姐显然更喜欢这些“离经叛道”的故事。"
                "我原本只是随意扫了一眼。"
                "可就在转身时，一本夹在角落里的书忽然吸引了我的注意。"
                show 记-西游记五十四回 with dissolve
                "那是一本《西游记》，却和刚才那一本不同。"
                "书页明显比周围其他书旧上许多，像是被人反复翻阅过。"
                "这引起了我的注意，我伸手将其取下，突然一张纸条从书中滑落而出。"
                "--若有人翻到此书，还望替我将它交予鹂儿，并托她将此书与那串手串一并寄存在“渡芦”当铺--"
                "这本西游记也要一并存入那个当铺。"
                "我顿时有些纳闷，但同时夹杂着不祥的预感。"
                "雁儿姐这是何用意？"
                "于是我想要将其翻开。"
                "可当我翻开第一页时，我却忽然愣住了。"
                "里面都是由雁儿姐字迹组成，书中的许多地方，竟都被她用极娟秀的小字仔细做了批注。"
                
                "密密麻麻，一页接一页。"
                "它们竖着排列，方方正正。"
                fang "怎么可能......"
                "我连拿着书的手都在发抖。"
                play sound "打击音效/Se_翻纸.ogg"
                su "我快速翻着这本书，不忍去细读完任意一页，而目光却总是不经意瞥见一些批注。"
                scene 苏抄书 with ink2
                voice "pv/补_苏怜烟_01.ogg"
                su "此处手错抄错一行，知宥全当没看见吧。"
                voice "pv/补_苏怜烟_02.ogg"
                su "我抄至此处，忽觉唐僧亦非善类，竟如此逼迫悟空。"
                voice "pv/补_苏怜烟_04.ogg"
                su "冷......今夜格外冷。"
                voice "pv/补_苏怜烟_05.ogg"
                su "此段，倒让我想起了那年在方院，你我隔墙交流之时。"
                voice "pv/补_苏怜烟_06.ogg"
                su "抄至此处，方觉你好久没来了......难道是那景姨从中作梗，说我不想见你。"
                voice "pv/补_苏怜烟_07.ogg"
                su "我想见你。"
                voice "pv/补_苏怜烟_08.ogg"
                su "愈写愈难，怕是抄不完此书了。"
                "她的字迹，越是到后面越是淡，也越是歪斜。"
                "等到了最后那章时，那原本工整娟秀的字体不在了，每一笔每一话都透露出她握笔不易。"
                "我合上书，不愿再看。"
                "似乎一切的真相都悄然浮出水面。"
                scene 苏抄书_2 with ink2
                voice "pv/02_苏怜烟_21.ogg"
                su "倘若有朝一日，你书写成，名动四方，我便赠你一物。"
                "我会想着她当时的容颜。"
                "浅笑着，侧身回眸望向我说看。"
                "那是我与她的约定。"
                "......"
                "她早已为我准备好。"
                "我想起曾对她说过《西游记》是我最喜欢的一本书。"
                "她送我的礼物，竟是她亲手抄写的《西游记》。"
                "我的心一阵一阵地疼。疼得胸口阵阵发颤，疼得五脏六腑都像搅在了一起，疼得人连气都喘不上来。"
                "忽然间我好像耳鸣了。"
                "好像什么都听不见了。"
                "那一瞬间，周围所有声音仿佛都忽然离我远去了。"
                scene black with dissolve
                play sound "打击音效/Se_DaoDi.ogg"
                "可能是因为大脑一些接受过多的信息。"
                "我双脚忽然无力重重的摔在地上。"
                fang "雁儿姐......"
                fang "雁儿姐......"
                fang "怜烟确实...患了重病。"
                "从书中字迹愈发歪斜就能看出雁儿姐病情在一点点恶化。"
                "这份手抄西游记和那串手镯恐怕就是雁儿姐为了我留下的......她留在世上的痕迹。"
                "我收下这本书和那手镯，也就代表......"
                scene 游舫夜 at bg_gray with ink2
                show 苏连雁 通常 with dissolve
                voice "pv/28_方知宥_64.ogg"
                fang "若是雁儿姐不在了，我会成为你活过的痕迹。"
                pause 3.0
                "那时我说过的话也再次涌上心头。"
                "......"
                "如果再结合那本放在桌上的《梁祝》。"
                "不难猜出......雁儿姐是想与我同去黄泉......"
                "这时我脑海里便又浮现出我与雁儿姐最后一次分别之时她说的话。"
                scene 游舫夜 at bg_gray 
                show 苏连雁 悲伤 with dissolve
                voice "pv/28_苏怜烟_57.ogg"
                su "如果......我是说如果......最后我们什么都做不到......我若是想以死明志的话，你会如何？"
                pause 2.0
                "还有那时我们分别时她说的那句......"
                scene 宥雁相拥 at bg_gray with fade
                voice "pv/28_苏怜烟_61.ogg"
                su "我要走啦......"
                voice "pv/28_苏怜烟_62.ogg"
                su "知宥，照顾好自己。"
                pause 2.0
                show inner_monologue_dim onlayer master 
                "雁儿姐曾向我提起“逃走”二字时，我竟半点都未曾察觉。"
                "我一直以为，她还是那个小时候拼命想拉着我逃离束缚、总笑着劝我要为自己活一次的雁儿姐。"
                "看来我今日的想法是对的，我以为的雁儿姐并不是“雁儿姐”。"
                "“逃”也并非“逃”。"
                "逃离束缚是逃，逃离这吃人的世道也是逃……"
                "再次回想傍晚鹂儿告诉我雁儿姐近期不想见我。"
                "恐怕也是因为怕再与我见面，求死之心会有所动摇吧。"
                "......"
                "但心中仍有一未解之谜。"
                "可为何......"
                "雁儿姐......为何......为何你要瞒着我，瞒着鹂儿，瞒着所有人。"
                hide inner_monologue_dim
                voice "配音/chapter1/鹂/audio (40).wav"
                Li "方公子？！！你还好吗？"
                "当我又不受控被回忆吞没的时候，鹂儿将我拉了回来。"
                show 宥雁相拥 at bg_shake
                show 宥雁相拥 at bg_shake
                show 花魁房间 with dissolve
                show 鹂儿无奈 with dissolve 
                voice "配音/chapter1/鹂/audio (41).wav"
                Li "方才你就一直跪在地上发愣。"
                stop music fadeout 1.5
                voice "配音/chapter1/鹂/audio (42).wav"
                Li "是不是发现什么有用的线索了？"
                fang "......"
                fang "发现了......"
                voice "配音/chapter1/鹂/audio (43).wav"
                Li "发现什么了？"
                fang "发现了怜烟小姐执意求死，还想与我殉情。"
                show 鹂儿急切 at char_shake
                voice "配音/chapter1/鹂/audio (44).wav"
                Li "那我们赶紧去找小姐啊。"
                show inner_monologue_dim onlayer master 
                "这一句话，仿佛一道惊雷般猛地将我点醒。"
                "我如今也只是猜到了雁儿姐的心思而已。"
                "万一……万一她还未来得及去做呢？"
                "可另一个念头，却还是不受控制地从脑海深处一点点浮了上来。"
                "距离雁儿姐失踪，已经过去整整两个时辰了。若她当真早已下定决心……那么此刻的她，很可能早就已经……"
                "不，不能这么想。"
                "还没有结束。"
                "但只要还有一丝希望，我就要去抓住。"
                "活要见人，死要见尸。"
                hide inner_monologue_dim

                jump 找小姐

            

            


            

   
    
    


    






    
    








    

    
   
    





    



    









    

    
    

    

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    

    # 此处显示各行对话。

    "您已创建一个新的 Ren'Py 游戏。"

    "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
