## 此文件包含有可自定义您游戏的设置。
##
## 以“##”开头的语句是注释，您不应该对其取消注释。以“#”开头的语句是注释掉的代码，
## 在适用的时候您可能需要对其取消注释。


## 基础 ##########################################################################

## 用户可读的游戏名称。此命令用来设置默认窗口标题，并且会在界面和错误报告中出
## 现。
##
## 带有 _() 的字符串表示其可被翻译。

define config.name = _("CAA")


## 决定上面给出的标题是否显示在标题界面屏幕。设置为 False 来隐藏标题。

define gui.show_name = True


## 游戏版本号。

define config.version = "1.0"


## 放置在游戏内“关于”屏幕上的文本。将文本放在三个引号之间，并在段落之间留出空
## 行。

define gui.about = _p("""
""")


## 在构建的发布版中，可执行文件和目录所使用的短名称。此处仅限使用 ASCII 字符，并
## 且不能包含空格、冒号或分号。

define build.name = "CAA"


## 音效和音乐 #######################################################################

## 这三个变量控制哪些内置的混音器会默认显示给用户。将其中一个设置为 False 将隐藏
## 对应的混音器。

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## 为了让用户在音效或语音轨道上播放测试音频，请取消对下面一行的注释并设置播放的
## 样本声音。

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## 将以下语句取消注释就可以设置标题界面播放的背景音乐文件。此文件将在整个游戏中
## 持续播放，直至音乐停止或其他文件开始播放。

# define config.main_menu_music = "main-menu-theme.ogg"


## 转场 ##########################################################################
##
## 这些变量用来控制某些事件发生时的转场。每一个变量都应设置成一个转场，或者是
## None 来表示无转场。

## 进入或退出游戏菜单。

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## 各个游戏菜单之间的转场。

define config.intra_transition = dissolve


## 载入游戏后使用的转场。

define config.after_load_transition = None


## 在游戏结束之后进入主菜单时使用的转场。

define config.end_game_transition = None


## 用于控制在游戏开始标签不存在时转场的变量。作为替代，在显示初始化场景后使用
## with 语句。


## 窗口管理 ########################################################################
##
## 此命令控制对话框窗口何时显示。若为 show，对话框将总是显示。若为 hide，对话框
## 仅在对话出现时显示。若为 auto，对话框会在 scene 语句前隐藏，并在有新对话时重
## 新显示。
##
## 在游戏开始后，可以用 window show、window hide 和 window auto 语句来改变其状
## 态。

define config.window = "auto"


## 用于显示和隐藏对话框窗口的转场

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## 默认设置 ########################################################################

## 控制默认的文字显示速度。默认的 0 为瞬间，而其他数字则是每秒显示出的字符数。

default preferences.text_cps = 15


## 默认的自动前进延迟。数字越大，等待时间越长，有效范围为 0 - 30。

default preferences.afm_time = 15

default history_voice_paths = []

## CG 库系统 #######################################################################

## 定义所有可收集的CG
define gallery_cgs = [
    {"id": "cg_wangfang", "name": "方王吵架", "path": "images/CG/方王吵架.png"},
    {"id": "cg_wangfang2", "name": "方王吵架_2", "path": "images/CG/方王吵架_2.png"},
    {"id": "cg_wangfang3", "name": "方王吵架_3", "path": "images/CG/方王吵架_3.png"},
    {"id": "鹂儿回头", "name": "鹂儿回头", "path": "images/CG/鹂儿回头.png"},
    {"id": "鹂儿回头_2", "name": "鹂儿回头_2", "path": "images/CG/鹂儿回头_2.png"},
    {"id": "林糖葫芦", "name": "林糖葫芦", "path": "images/CG/林糖葫芦.png"},
    {"id": "林糖葫芦_2", "name": "林糖葫芦_2", "path": "images/CG/林糖葫芦_2.png"},
    {"id": "三人狂奔", "name": "三人狂奔", "path": "images/CG/三人狂奔.png"},
    {"id": "雁桥头", "name": "雁桥头", "path": "images/CG/雁桥头.png"},
    {"id": "雁桥头2", "name": "雁桥头2", "path": "images/CG/雁桥头2.png"},
    {"id": "雁桥头3", "name": "雁桥头3", "path": "images/CG/雁桥头3.png"},
    {"id": "雁桥头4", "name": "雁桥头4", "path": "images/CG/雁桥头4.png"},
    {"id": "拉雁", "name": "拉雁", "path": "images/CG/拉雁.png"},
    {"id": "拉雁3", "name": "拉雁3", "path": "images/CG/拉雁3.png"},
    {"id": "与雁相拥", "name": "与雁相拥", "path": "images/CG/与雁相拥.png"},
    {"id": "与雁相拥2", "name": "与雁相拥2", "path": "images/CG/与雁相拥2.png"},
    {"id": "性感雁", "name": "性感雁", "path": "images/CG/性感雁.png"},
    {"id": "雁就寝", "name": "雁就寝", "path": "images/CG/雁就寝.png"},
    {"id": "雁侧卧", "name": "雁侧卧", "path": "images/CG/雁侧卧.png"},
    {"id": "雁侧卧2", "name": "雁侧卧2", "path": "images/CG/雁侧卧2.png"},
    {"id": "雁侧卧3", "name": "雁侧卧3", "path": "images/CG/雁侧卧3.png"},
    {"id": "雁侧卧4", "name": "雁侧卧4", "path": "images/CG/雁侧卧4.png"},
    {"id": "雁侧卧5", "name": "雁侧卧5", "path": "images/CG/雁侧卧5.png"},
    {"id": "雁宥共寝", "name": "雁宥共寝", "path": "images/CG/雁宥共寝.png"},
    {"id": "雁宥共枕", "name": "雁宥共枕", "path": "images/CG/雁宥共枕.png"},
    {"id": "雁宥共枕2", "name": "雁宥共枕2", "path": "images/CG/雁宥共枕2.png"},
    {"id": "雁宥共枕3", "name": "雁宥共枕3", "path": "images/CG/雁宥共枕3.png"},
    {"id": "雁宥共枕4", "name": "雁宥共枕4", "path": "images/CG/雁宥共枕4.png"},
    {"id": "cg_breakfirst", "name": "共进早餐1", "path": "images/CG/共进早餐1.png"},
    {"id": "cg_breakfirst2", "name": "共进早餐2", "path": "images/CG/共进早餐2.png"},
    {"id": "共进早餐3", "name": "共进早餐3", "path": "images/CG/共进早餐3.png"},
    {"id": "共进早餐4", "name": "共进早餐4", "path": "images/CG/共进早餐4.png"},
    {"id": "shopping", "name": "shopping", "path": "images/CG/shopping.png"},
    {"id": "shopping1", "name": "shopping1", "path": "images/CG/shopping1.png"},
    {"id": "shopping3", "name": "shopping3", "path": "images/CG/shopping3.png"},
    {"id": "shopping4", "name": "shopping4", "path": "images/CG/shopping4.png"},
    {"id": "shopping5", "name": "shopping5", "path": "images/CG/shopping5.png"},
    {"id": "雁宥逛街1", "name": "雁宥逛街1", "path": "images/CG/雁宥逛街1.png"},
    {"id": "雁宥逛街2", "name": "雁宥逛街2", "path": "images/CG/雁宥逛街2.png"},
    {"id": "偶遇翩翩", "name": "偶遇翩翩", "path": "images/CG/偶遇翩翩.png"},
    {"id": "偶遇翩翩1", "name": "偶遇翩翩1", "path": "images/CG/偶遇翩翩1.png"},
    {"id": "偶遇翩翩2", "name": "偶遇翩翩2", "path": "images/CG/偶遇翩翩2.png"},
    {"id": "三人行", "name": "三人行", "path": "images/CG/三人行.png"},
    {"id": "三人行1", "name": "三人行1", "path": "images/CG/三人行1.png"},
    {"id": "三人行2", "name": "三人行2", "path": "images/CG/三人行2.png"},
    {"id": "三人行3", "name": "三人行3", "path": "images/CG/三人行3.png"},
    {"id": "三人行4", "name": "三人行4", "path": "images/CG/三人行4.png"},
    {"id": "三人行5", "name": "三人行5", "path": "images/CG/三人行5.png"},
    {"id": "苏特写", "name": "苏特写", "path": "images/CG/苏特写.png"},
    {"id": "林特写", "name": "林特写", "path": "images/CG/林特写.png"},
    {"id": "蝶雁换装", "name": "蝶雁换装", "path": "images/CG/蝶雁换装.png"},
    {"id": "追兵", "name": "追兵", "path": "images/CG/追兵.png"},
    {"id": "逃跑", "name": "逃跑", "path": "images/CG/逃跑.png"},
    {"id": "三人逃跑", "name": "三人逃跑", "path": "images/CG/三人逃跑.png"},
    {"id": "被压制", "name": "被压制", "path": "images/CG/被压制.png"},
    {"id": "出手相救1", "name": "出手相救1", "path": "images/CG/出手相救1.png"},
        {"id": "王生开门", "name": "王生开门", "path": "images/CG/王生开门 (1).png"},
    {"id": "王生开门2", "name": "王生开门2", "path": "images/CG/王生开门 (2).png"},
    {"id": "林幻境", "name": "林幻境", "path": "images/CG/林幻境.png"},
    {"id": "林幻境2", "name": "林幻境2", "path": "images/CG/林幻境2.png"},
    {"id": "林幻境3", "name": "林幻境3", "path": "images/CG/林幻境3.png"},
    {"id": "拿香囊", "name": "拿香囊", "path": "images/CG/拿香囊.png"},
    {"id": "训斥", "name": "训斥", "path": "images/CG/训斥.png"},
    {"id": "训斥2", "name": "训斥2", "path": "images/CG/训斥2.png"},
    {"id": "训斥3", "name": "训斥3", "path": "images/CG/训斥3.png"},
    {"id": "训斥4", "name": "训斥4", "path": "images/CG/训斥4.png"},
    {"id": "训斥5", "name": "训斥5", "path": "images/CG/训斥5.png"},
    {"id": "训斥6", "name": "训斥6", "path": "images/CG/训斥6.png"},
    {"id": "被发现", "name": "被发现", "path": "images/CG/被发现.png"},
    {"id": "帘子", "name": "帘子", "path": "images/CG/帘子.png"},
    {"id": "帘子2", "name": "帘子2", "path": "images/CG/帘子2.png"},
    {"id": "帘子3", "name": "帘子3", "path": "images/CG/帘子3.png"},
    {"id": "帘子4", "name": "帘子4", "path": "images/CG/帘子4.png"},
    {"id": "帘子5", "name": "帘子5", "path": "images/CG/帘子5.png"},
    {"id": "帘子6", "name": "帘子6", "path": "images/CG/帘子6.png"},
    {"id": "帘子7", "name": "帘子7", "path": "images/CG/帘子7.png"},
    {"id": "对峙", "name": "对峙", "path": "images/CG/对峙.png"},
    {"id": "挽留", "name": "挽留", "path": "images/CG/挽留.png"},
    {"id": "第一次相见", "name": "第一次相见", "path": "images/CG/第一次相见.png"},
    {"id": "林二十四桥", "name": "林二十四桥", "path": "images/CG/林二十四桥.png"},
    {"id": "悔儿眺望", "name": "悔儿眺望", "path": "images/CG/悔儿眺望.png"},
    {"id": "悔儿眺望2", "name": "悔儿眺望2", "path": "images/CG/悔儿眺望2.png"},
    {"id": "悔儿眺望3", "name": "悔儿眺望3", "path": "images/CG/悔儿眺望3.png"},
    {"id": "悔儿眺望4", "name": "悔儿眺望4", "path": "images/CG/悔儿眺望4.png"},
    {"id": "悔儿眺望5", "name": "悔儿眺望5", "path": "images/CG/悔儿眺望5.png"},
    {"id": "悔儿眺望6", "name": "悔儿眺望6", "path": "images/CG/悔儿眺望6.png"},
    {"id": "悔儿眺望7", "name": "悔儿眺望7", "path": "images/CG/悔儿眺望7.png"},
    {"id": "悔儿眺望8", "name": "悔儿眺望8", "path": "images/CG/悔儿眺望8.png"},
    {"id": "悔儿眺望9", "name": "悔儿眺望9", "path": "images/CG/悔儿眺望9.png"},
    {"id": "悔儿眺望10", "name": "悔儿眺望10", "path": "images/CG/悔儿眺望10.png"},
    {"id": "悔儿眺望11", "name": "悔儿眺望11", "path": "images/CG/悔儿眺望11.png"},
    {"id": "悔儿眺望12", "name": "悔儿眺望12", "path": "images/CG/悔儿眺望12.png"},
    {"id": "蝶化", "name": "蝶化", "path": "images/CG/蝶化.png"},
    {"id": "化蝶1", "name": "化蝶1", "path": "images/CG/化蝶1.png"},
    {"id": "化蝶2", "name": "化蝶2", "path": "images/CG/化蝶2.png"},
    {"id": "化蝶3", "name": "化蝶3", "path": "images/CG/化蝶3.png"},
    {"id": "化蝶4", "name": "化蝶4", "path": "images/CG/化蝶4.png"},
    {"id": "告别", "name": "告别", "path": "images/CG/告别.png"},
    {"id": "越拉越远", "name": "越拉越远", "path": "images/CG/越拉越远.png"},
    {"id": "越拉越远2", "name": "越拉越远2", "path": "images/CG/越拉越远2.png"},
    {"id": "越拉越远3", "name": "越拉越远3", "path": "images/CG/越拉越远3.png"},
    {"id": "离开扬州", "name": "离开扬州", "path": "images/CG/离开扬州.png"},
    {"id": "悔儿看书", "name": "悔儿看书", "path": "images/CG/悔儿看书.png"},
    {"id": "林半遮面", "name": "林半遮面", "path": "images/CG/林半遮面.png"},
    {"id": "船头雁", "name": "船头雁", "path": "images/CG/船头雁.png"},
    {"id": "船头雁2", "name": "船头雁2", "path": "images/CG/船头雁2.png"},
    {"id": "雁回头", "name": "雁回头", "path": "images/CG/雁回头.png"},
    {"id": "船上鹂儿", "name": "船上鹂儿", "path": "images/CG/船上鹂儿.png"},
    {"id": "船上鹂儿2", "name": "船上鹂儿2", "path": "images/CG/船上鹂儿2.png"},
    {"id": "鹂儿船3", "name": "鹂儿船3", "path": "images/CG/鹂儿船3.png"},
    {"id": "船上鹂儿4", "name": "船上鹂儿4", "path": "images/CG/船上鹂儿4.png"},
    {"id": "高考", "name": "高考", "path": "images/CG/高考.png"},
    {"id": "高考1", "name": "高考1", "path": "images/CG/高考1.png"},
    {"id": "高考3", "name": "高考3", "path": "images/CG/高考3.png"},
    {"id": "高考4", "name": "高考4", "path": "images/CG/高考4.png"},
    {"id": "高考5", "name": "高考5", "path": "images/CG/高考5.png"},
    {"id": "高考8", "name": "高考8", "path": "images/CG/高考8.png"},
    {"id": "高考9", "name": "高考9", "path": "images/CG/高考9.png"},
    {"id": "高考10", "name": "高考10", "path": "images/CG/高考10.png"},
    {"id": "高考11", "name": "高考11", "path": "images/CG/高考11.png"},
    {"id": "高考12", "name": "高考12", "path": "images/CG/高考12.png"},
    {"id": "高考13", "name": "高考13", "path": "images/CG/高考13.png"},




]

## 存储已解锁的CG ID
default unlocked_cgs = []
default persistent.unlocked_cgs = []


## 存档目录 ########################################################################
##
## 控制 Ren'Py 放置游戏存档的特定操作系统目录。存档文件将放置在：
##
## Windows：%APPDATA\RenPy\<config.save_directory>
##
## Macintosh：$HOME/Library/RenPy/<config.save_directory>
##
## Linux：$HOME/.renpy/<config.save_directory>
##
## 该语句通常不应变更，若要变更，应为有效字符串而不是表达式。

define config.save_directory = "CAA-1779106637"


## 图标 ##########################################################################
##
## 在任务栏或 Dock 上显示的图标。

define config.window_icon = "gui/window_icon.png"


## 构建配置 ########################################################################
##
## 此部分控制 Ren'Py 如何将您的项目转变为发行版文件。

init python:
    config.keymap['rollback'] = []
    config.keymap['dismiss'] = [ 'mouseup_1' ]

    ## 以下函数接受文件模式。文件模式不区分大小写，并与基础目录的相对路径相匹
    ## 配，包括或不包括 /。如果多个模式匹配，则使用第一个模式。
    ##
    ## 在一个模式中：
    ##
    ## / 是目录分隔符。
    ##
    ## * 匹配所有字符，目录分隔符除外。
    ##
    ## ** 匹配所有字符，包括目录分隔符。
    ##
    ## 例如，“*.txt”匹配基础目录中的 txt 文件，“game/**.ogg”匹配游戏目录或任何子
    ## 目录中的 ogg 文件，“**.psd”匹配项目中任何位置的 psd 文件。

    ## 将文件列为 None 来使其从构建的发行版中排除。

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## 若要封装文件，需将其列为“archive”。

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## 匹配为文档模式的文件会在 Mac 应用程序构建中被复制，因此它们同时出现在 APP
    ## 和 ZIP 文件中。

    build.documentation('*.html')
    build.documentation('*.txt')


## 执行应用内购需要一个 Google Play 许可密钥。许可密钥可以在 Google Play 开发者
## 控制台的“Monetize” > “Monetization Setup” > “Licensing”页面找到。

# define build.google_play_key = "..."


## 与 itch.io 项目相关的用户名和项目名，以 / 分隔。

# define build.itch_project = "renpytom/test-project"
