import config, pprint, platform, myTranslation
from translations import translations
# [Optional] Google-translate
try:
    from googletrans import Translator
    googletransInstall = True
except:
    googletransInstall = False

class Languages:

    codes = {
        "Afrikaans": "af",
        "Albanian": "sq",
        "Amharic": "am",
        "Arabic": "ar",
        "Armenian": "hy",
        "Azerbaijani": "az",
        "Basque": "eu",
        "Belarusian": "be",
        "Bengali": "bn",
        "Bosnian": "bs",
        "Bulgarian": "bg",
        "Catalan": "ca",
        "Cebuano": "ceb",
        "Chinese (Simplied)": "zh-CN",
        "Chinese (Traditional)": "zh-TW",
        "Corsican": "co",
        "Croatian": "hr",
        "Czech": "cs",
        "Danish": "da",
        "Dutch": "nl",
        "English": "en",
        "Esperanto": "eo",
        "Estonian": "et",
        "Finnish": "fi",
        "French": "fr",
        "Frisian": "fy",
        "Galician": "gl",
        "Georgian": "ka",
        "German": "de",
        "Greek": "el",
        "Gujarati": "gu",
        "Haitian Creole": "ht",
        "Hausa": "ha",
        "Hawaiian": "haw",
        "Hebrew he or": "iw",
        "Hindi": "hi",
        "Hmong": "hmn",
        "Hungarian": "hu",
        "Icelandic": "is",
        "Igbo": "ig",
        "Indonesian": "id",
        "Irish": "ga",
        "Italian": "it",
        "Japanese": "ja",
        "Javanese": "jv",
        "Kannada": "kn",
        "Kazakh": "kk",
        "Khmer": "km",
        "Korean": "ko",
        "Kurdish": "ku",
        "Kyrgyz": "ky",
        "Lao": "lo",
        "Latin": "la",
        "Latvian": "lv",
        "Lithuanian": "lt",
        "Luxembourgish": "lb",
        "Macedonian": "mk",
        "Malagasy": "mg",
        "Malay": "ms",
        "Malayalam": "ml",
        "Maltese": "mt",
        "Maori": "mi",
        "Marathi": "mr",
        "Mongolian": "mn",
        "Myanmar (Burmese)": "my",
        "Nepali": "ne",
        "Norwegian": "no",
        "Nyanja (Chichewa)": "ny",
        "Pashto": "ps",
        "Persian": "fa",
        "Polish": "pl",
        "Portuguese (Portugal, Brazil)": "pt",
        "Punjabi": "pa",
        "Romanian": "ro",
        "Russian": "ru",
        "Samoan": "sm",
        "Scots Gaelic": "gd",
        "Serbian": "sr",
        "Sesotho": "st",
        "Shona": "sn",
        "Sindhi": "sd",
        "Sinhala (Sinhalese)": "si",
        "Slovak": "sk",
        "Slovenian": "sl",
        "Somali": "so",
        "Spanish": "es",
        "Sundanese": "su",
        "Swahili": "sw",
        "Swedish": "sv",
        "Tagalog (Filipino)": "tl",
        "Tajik": "tg",
        "Tamil": "ta",
        "Telugu": "te",
        "Thai": "th",
        "Turkish": "tr",
        "Ukrainian": "uk",
        "Urdu": "ur",
        "Uzbek": "uz",
        "Vietnamese": "vi",
        "Welsh": "cy",
        "Xhosa": "xh",
        "Yiddish": "yi",
        "Yoruba": "yo",
        "Zulu": "zu",
    }

    translation = {
        "menu1_app": "UniqueBible",
        "menu1_screenSize": "Window Size",
        "menu1_generalPreferences": "General Preferences",
        "menu1_fullScreen": "Full Screen",
        "menu1_topHalf": "Top Half",
        "menu1_bottomHalf": "Bottom Half",
        "menu1_leftHalf": "Left Half",
        "menu1_rightHalf": "Right Half",
        "menu1_smallSize": "Small Size",
        "menu1_resize": "Resize",
        "menu1_remoteControl": "Open / Close Control Panel",
        "menu1_setDefaultFont": "Default Font and Size",
        "menu1_setChineseFont": "Chinese Font",
        "menu1_setAbbreviations": "Select Bible Abbreviations",
        "menu1_setMyFavouriteBible": "Select my Favourite Bible",
        "menu1_setMyLanguage": "Select my Language",
        "menu1_programInterface": "Program Interface",
        "menu1_translateInterface": "Translate into my Language",
        "menu1_toogleInterface": "English / My Translation",
        "menu1_wikiPages": "Wiki Pages",
        "menu1_update": "Update",
        "menu1_clipboard": "Clipboard Content",
        "menu1_readClipboard": "Read",
        "menu1_runClipboard": "Run",
        "menu1_selectTheme": "Select Theme",
        "menu1_default_theme": "Default Theme",
        "menu1_dark_theme": "Dark Theme",
        "menu1_selectMenuLayout": "Select Menu Layout",
        "menu1_menuLayout": "Menu Layout",
        "menu1_classic_menu_layout": "Classic Menu Layout",
        "menu1_aleph_menu_layout": "Aleph Menu Layout",
        "menu1_selectDefaultLexicon": "Select Default Lexicon",
        "menu1_StrongsGreek": "Strong's Greek",
        "menu1_StrongsHebrew": "Strong's Hebrew",
        "menu1_setDefaultStrongsGreekLexicon": "Select Default Greek Lexicon",
        "menu1_setDefaultStrongsHebrewLexicon": "Select Default Hebrew Lexicon",
        "menu1_exit": "Exit",
        "menu2_toobars": "Toolbars",
        "menu2_view": "Layout",
        "menu2_all": "All / None",
        "menu2_topOnly": "All / Top Toolbar Only",
        "menu2_top": "Top Toolbar [Show / Hide]",
        "menu2_second": "Second Toolbar [Show / Hide]",
        "menu2_left": "Left Sidebar [Show / Hide]",
        "menu2_right": "Right Sidebar [Show / Hide]",
        "menu2_icons": "Icons [Full-size / Standard]",
        "menu2_landscape": "Orientation [Landscape / Portrait]",
        "menu2_study": "Study Window [Resize / Hide]",
        "menu2_bottom": "Bottom Window [Show / Hide]",
        "menu2_hover": "Instant Lookup",
        "menu2_fonts": "Fonts",
        "menu2_fontSize": "Font Size",
        "menu2_larger": "Larger",
        "menu2_smaller": "Smaller",
        "menu2_format": "Formatted / Simple Style",
        "menu2_subHeadings": "Insert Subheadings into Simple Style Chapter",
        "menu_toggleFeatures": "Toggle Features",
        "menu_toggleEnforceCompareParallel": "Enforce Compare / Parallel",
        "menu_syncStudyWindowBible": "Sync Study Window Bible",
        "menu_syncBibleCommentary": "Sync Bible Commentary",
        "menu2_toggleHighlightMarkers": "Highlight Markers",
        "menu3_history": "History",
        "menu2_mainWindowHistory": "Bible Window History",
        "menu2_studyWindowHistory": "Study Window History",
        "menu3_main": "All Records",
        "menu3_mainBack": "Previous Record",
        "menu3_mainForward": "Next Record",
        "menu3_study": "All Records",
        "menu3_studyBack": "Previous Record",
        "menu3_studyForward": "Next Record",
        "menu4_further": "Gems",
        "menu4_book": "Book Features",
        "menu4_chapter": "Chapter Features",
        "menu4_verse": "Verse Features",
        "menu4_word": "Word Features",
        "menu4_compareFeatures": "Version Comparison",
        "menu4_next": "Next Chapter",
        "menu4_previous": "Previous Chapter",
        "menu4_indexes": "Smart Indexes",
        "menu4_commentary": "Bible Commentary",
        "menu4_lastCommentary": "The Last Opened Commentary",
        "menu4_enableEnforceCompareParallel": "Comparison / Parallel Enforced",
        "menu4_disableEnforceCompareParallel": "One-off Comparison / Parallel",
        "menu4_traslations": "Translations",
        "menu4_discourse": "Discourse Analysis",
        "menu4_words": "Individual Words",
        "menu4_tdw": "TDW Combo",
        "menu4_crossRef": "Cross References",
        "menu4_tske": "TSK (Enhanced edition)",
        "menu4_compareAll": "Compare All Bible Versions",
        "menu4_moreComparison": "Comparison / Parallel Reading / Difference",
        "menu5_search": "Search",
        "menu5_lookup": "Search",
        "menu5_bible": "Bibles",
        "menu5_main": "Bible Window's Last Opened Bible",
        "menu5_study": "Study Window's Last Opened Bible",
        "menu5_dictionary": "The Last Opened Bible Dictionary",
        "menu5_encyclopedia": "The Last Opened Bible Encyclopedia",
        "menu5_book": "The Last Opened Reference Book",
        "menu5_selectBook": "Reference Book",
        "menu5_favouriteBook": "My Favourite Reference Books",
        "menu5_allBook": "All Reference Books",
        "menu5_characters": "Bible Characters",
        "menu5_names": "Bible People Names",
        "menu5_locations": "Bible Locations",
        "menu5_topics": "Bible Topics",
        "menu5_lastTopics": "The Last Opened Bible Topics",
        "menu5_allTopics": "All Bible Topics",
        "menu5_lexicon": "Hebrew / Greek Lexicon",
        "menu5_3rdDict": "Third Party Dictionaries",
        "menu6_notes": "Bible Notes",
        "menu6_mainChapter": "Bible Window's Bible Chapter Notes",
        "menu6_studyChapter": "Study Window's Bible Chapter Notes",
        "menu6_searchChapters": "Search Bible Chapter Notes",
        "menu6_mainVerse": "Bible Window's Bible Verse Notes",
        "menu6_studyVerse": "Study Window's Bible Verse Notes",
        "menu6_searchVerses": "Search Bible Verse Notes",
        "menu7_topics": "Note Files",
        "menu7_create": "Create a New File",
        "menu7_open": "Open an Existing File",
        "menu7_recent": "Recently Opened Files",
        "menu7_read": "Read the Last Opened File",
        "menu7_edit": "Edit the Last Opened File",
        "menu8_resources": "Resources",
        "menu8_bibles": "Install Formatted Bible",
        "menu8_commentaries": "Install Bible Commentary",
        "menu8_datasets": "Install Marvel.bible Datasets",
        "menu_marvelBibles": "Marvel Bibles",
        "menu8_plusLexicons": "Install BibleBentoPlus Lexicon",
        "menu8_plusDictionaries": "Install BibleBentoPlus Dictionary",
        "menu8_3rdParty": "Import 3rd Party Module",
        "menu8_3rdPartyInFolder": "Import Multiple 3rd Party Modules",
        "menu8_settings": "Select Import Options",
        "menu8_tagFile": "Add Bible Reference Links to a File",
        "menu8_tagFiles": "Add Bible Reference Links to Multiple Files",
        "menu8_tagFolder": "Add Bible Reference Links to a Folder's Files",
        "menu8_fixDatabase": "Fix Database",
        "menu9_information": "Information",
        "menu9_credits": "Sources",
        "menu9_contact": "Contact us",
        "menu10_books": "Books",
        "menu10_dialog": "Open a Reference Book",
        "menu10_addFavourite": "Add a Favourite Reference Book",
        "menu10_displayContent": "Display Content: Study / New Window",
        "menu10_bookOnNew": "Further book content will be opened on a new window.",
        "menu10_bookOnStudy": "Further book content will be opened on Study Window.",

        "menu_abbreviations": "Abbreviations",
        "menu_about": "About",
        "menu_annotate": "Annotate",
        "menu_apps": "Apps",
        "menu_bible": "Bible",
        "menu_bible_format": "Bible Format",
        "menu_bible_chapter_notes": "Bible Chapter Notes",
        "menu_bible_notes": "Bible Notes",
        "menu_bible_verse_notes": "Bible Verse Notes",
        "menu_build_macro": "Build Macro",
        "menu_chapter": "Chapter",
        "menu_chineseFont": "Chinese Font",
        "menu_command": "Command",
        "menu_config_flags": "Set Config Flags",
        "menu_data": "Data",
        "menu_defaults": "Defaults",
        "menu_display": "Display",
        "menu_donate": "Donate",
        "menu_edit_note": "Edit Note",
        "menu_external_notes": "External Notes",
        "menu_favouriteBible": "Favourite Bible",
        "menu_first_chapter": "First Chapter",
        "menu_font": "Font and Size",
        "menu_font": "Font",
        "menu_highlight": "Highlight",
        "menu_highlight": "Highlights",
        "menu_history": "History",
        "menu_language": "Language",
        "menu_last_chapter": "Last Chapter",
        "menu_lexicon": "Lexicon",
        "menu_library": "Library",
        "menu_light_theme": "Light Theme",
        "menu_macros": "Macros",
        "menu_main_page_down": "Main Page Scroll Down",
        "menu_main_page_up": "Main Page Page Up",
        "menu_main_scroll_to_top": "Main Scroll To Top",
        "menu_navigation": "Navigation",
        "menu_new_note": "New Note",
        "menu_next_book": "Next Book",
        "menu_next_chapter": "Next Chapter",
        "menu_next_verse": "Next Verse",
        "menu_notes": "Notes",
        "menu_open_note": "Open Note",
        "menu_previous_book": "Previous Book",
        "menu_previous_chapter": "Previous Chapter",
        "menu_quit": "Quit",
        "menu_read_note": "Read Note",
        "menu_reload": "Reload",
        "menu_run": "Run",
        "menu_scroll": "Scroll",
        "menu_bibleMenu": "Menu",
        "menu_search": "Search",
        "menu_simple_formatted": "Simple/Formatted",
        "menu_select_default_font": "Default Font and Size",
        "menu_startup_macro": "Startup Macro",
        "menu_study_page_down": "Study Page Scroll Down",
        "menu_study_page_up": "Study Page Page Up",
        "menu_study_scroll_to_top": "Study Scroll To Top",
        "menu_subheadings": "Subheadings",
        "menu_tabs": "Tabs",
        "menu_theme": "Theme",
        "menu_toolbar": "Toolbar",
        "menu_verse": "Verse",
        "menu_verse_all_versions": "Verse All Versions",
        "menu_wiki": "Wiki",
        "menu_window": "Window",
        "tab_print": "Print",
        "context1_copy": "Copy",
        "context1_copy_html": "Copy HTML",
        "context1_copyReferences": "Copy All Bible References",
        "context1_speak": "Speak",
        "context1_english": "Translate into English",
        "context1_tChinese": "翻譯成繁體中文",
        "context1_sChinese": "翻译成简体中文",
        "context1_my": "My Language",
        "context1_translate": "Translate into",
        "context1_pinyin": "翻译成汉语拼音",
        "context1_search": "Search",
        "context1_current": "Search Opened Bible Book",
        "context1_favourite": "Search my Favourite Bible",
        "context1_original": "Search Hebrew / Greek Bible",
        "context1_originalLexicon": "Search Hebrew / Greek Lexicon",
        "context1_favouriteBooks": "Search my Favourite Reference Books",
        "context1_allBooks": "Search All Reference Books",
        "context1_encyclopedia": "Bible Encyclopedia",
        "context1_dict": "Bible Dictionary",
        "context1_extract": "Extract All Bible References",
        "context1_command": "Run as Command",
        "bar1_title": "Top Toolbar",
        "bar2_title": "Second Toolbar",
        "bar3_title": "Left Sidebar",
        "bar4_title": "Right Sidebar",
        "bar2_enableBible": "Open Bible References on Study Window",
        "bar2_disableBible": "Open Bible References on Bible Window",
        "bar1_menu": "Bible Window",
        "bar1_reference": "Bible Window's Bible Reference",
        "bar1_chapterNotes": "Bible Window's Bible Chapter Notes",
        "bar1_verseNotes": "Bible Window's Bible Verse Notes",
        "bar1_searchBible": "Search Bible Window's Last Opened Bible",
        "bar1_searchBibles": "Search Bible Window's Bible",
        "bar1_command": "Type your command here",
        "bar1_toolbars": "Show / Hide Other Toolbars",
        "bar2_menu": "Study Window",
        "bar2_reference": "Study Window's Bible Reference",
        "bar2_chapterNotes": "Study Window's Bible Chapter Notes",
        "bar2_verseNotes": "Study Window's Bible Verse Notes",
        "bar2_searchBible": "Search Study Window's Last Opened Bible",
        "bar2_searchBibles": "Search Study Window's Bible",
        "bar2_searchBooks": "Search Reference Book",
        "bar3_pdf": "Export to PDF",
        "note_title": "Note Editor Menu Bar",
        "note_save": "Save",
        "note_saveAs": "Save as",
        "note_print": "Print",
        "note_toolbar": "Show / Hide Toolbar",
        "note_mode": "Rich Format / Plain Mode",
        "noteTool_title": "Toolbar",
        "noteTool_bold": "Bold Font",
        "noteTool_italic": "Italic Font",
        "noteTool_underline": "Underline Style",
        "noteTool_trans0": "Transform Selected Text",
        "noteTool_trans1": "For example, create a bullet list:",
        "noteTool_trans2": "For example, create a numbered list:",
        "noteTool_trans3": "For example, create a table:",
        "noteTool_no1": "one",
        "noteTool_no2": "two",
        "noteTool_no3": "three",
        "noteTool_no4": "four",
        "noteTool_no5": "five",
        "noteTool_no6": "six",
        "noteTool_left": "Align Left",
        "noteTool_centre": "Align Centre",
        "noteTool_right": "Align Right",
        "noteTool_justify": "Justify Text",
        "noteTool_delete": "Delete Formatting",
        "noteTool_hyperlink": "Add a Hyperlink",
        "noteTool_externalImage": "Link to an External Image File",
        "noteTool_image": "Embed an Image",
        "noteTool_exportImage": "Export Embedded Images",
        "tabBible": "Bible",
        "tabStudy": "Tool",
        "message_done": "Done.",
        "message_fail": "Failed to complete the last operation!",
        "message_invalid": "Entered command is invalid!",
        "message_missing": "Missing component:",
        "message_installFirst": "Install it first and try again.",
        "message_restart": "Restart this application to apply the new changes.",
        "message_run": "Before you can run this feature, you need to:",
        "message_selectWord": "Select a word or some words.",
        "message_setLanguage": "Select your language.",
        "message_translateFirst": "Translate program interface into your language.",
        "message_improveTrans": "To improve the quality of interface translation, you may close this application first and manually edit this file:",
        "message_newInterfaceItems": "Added new translated items of program interface.",
        "message_migration": "Some of your files are old.  We are helping you to upgrade those files.",
        "message_noReference": "Found no bible reference.",
        "message_noSupport": "It looks like that this feature does not work on your device.",
        "message_newerFile": "This file has a newer version:",
        "message_installFrom": "Install from menu:",
        "message_downloadAllFiles": "It takes time to complete this operation.",
        "message_noSupportedFile": "No valid file.",
        "message_tagged": "Tagged file is prefixed with:",
        "message_willBeNoticed": "You will receive another message when the operation is done.",
        "message_themeTakeEffectAfterRestart": "Theme will take effect after the next restart",
        "html_searchBible2": "Search Bible:",
        "html_searchBibles2": "Search Multiple Bibles:",
        "html_features": "Special Features:",
        "html_and": "and:",
        "html_showCompare": "Show Comparison",
        "html_showParallel": "Show Parallel Reading",
        "html_showDifference": "Show Difference",
        "html_current": "Current Selection:",
        "html_bibles": "Bible Version:",
        "html_book": "Bible Book:",
        "html_chapter": "Bible Chapter:",
        "html_verse": "Bible Verse:",
        "html_open": "open",
        "html_openHere": "open HERE",
        "html_openMain": "open on Bible Window",
        "html_openStudy": "open on Study Window",
        "html_introduction": "Introduction",
        "html_overview": "Overview",
        "html_summary": "Summary",
        "html_chapterIndex": "Bible Characters & Locations",
        "html_timelines": "Timelines",
        "message_remarks": "Remarks:",
        "message_cancel": "Cancel",
        "message_install": "Download and Install",
        "message_installing": "Installing...",
        "message_downloadHelper": "Download Helper",
        "message_searchMorphology": "Search Morphology",
        "import_linebreak": "Additional linebreak for each bible verse",
        "import_strongNo": "Allow search for Strong's numbers",
        "import_morphCode": "Allow search for morphology codes",
        "import_rtl": "Old Testament Text Direction: Right-to-left",
        "import_interlinear": "Interlinear Bible",
        "message_addFavouriteVersion": "Add as a parallel version for reading multiple bible verse references:",
        "search_notFound": "[no result]",
        "menu11_multimedia": "Multimedia",
        "menu11_images": "Images",
        "menu11_music": "Music",
        "menu11_video": "Video",
        "menu11_setupDownload": "Instructions to Setup YouTube Downloader",
        "menu11_youtube": "Download YouTube Audio / Video",
        "youtube_back": "Back",
        "youtube_forward": "Forward",
        "youtube_mp3": "Download Audio in mp3 Format",
        "youtube_mp4": "Download Video in mp4 Format",
        "youtube_address": "Enter a YouTube address:",
        "youtube_copy": "Copy Opened Link",
        "menu9_donate": "Donate to us",
        "menu8_moreBooks": "Download More Reference Books",
        "menu_more": "More ...",
        "menu1_moreConfig": "Select More ...",
        "message_readWiki": "You may check this Wiki page for description of the following items:",
        "menu1_tabNo": "Select Number of Tabs",
        "menu5_last3rdDict": "The Last Opened Third Party Dictionary",
        "menu8_marvelData": "Database Files",
        "menu8_download3rdParty": "Download 3rd Party Modules",
        "menu10_bookFromImages": "Create a Reference Book from Image Files",
        "menu10_bookFromHtml": "Create a Reference Book from HTML Files",
        "menu10_bookFromNotes": "Create a Reference Book from Note Files",
        "noteTool_header1": "Header 1",
        "noteTool_header2": "Header 2",
        "noteTool_header3": "Header 3",
        "noteTool_textFont": "Text Font",
        "noteTool_textColor": "Text Color",
        "noteTool_textBackgroundColor": "Text Background Color",
        "menu10_clearBookHighlights": "Remove Search Result Highlights",
        "menu1_reload": "Reload the Last Opened Records",
        "select_a_folder": "Select a Folder",
        "bar2_commentarySyncEnabled": "Commentary in Sync with Main Window",
        "bar2_commentarySyncDisabled": "Commentary out of Sync with Main Window",
        "bar2_studyWindowBibleSyncEnabled": "Study Window's Bible in Sync with Main Window",
        "bar2_studyWindowBibleSyncDisabled": "Study Window's Bible out of Sync with Main Window",
        "empty": "[empty]",
        "remote_control": "Control Panel",
        "bible": "Bible",
        "translations": "Translations",
        "commentaries": "Commentaries",
        "lexicons": "Lexicons",
        "dictionaries": "Dictionaries",
        "enter": "Enter",
        "enter_command_here": "Enter command here ...",
        "filename": "Filename",

        "message_select_macro": "Select Macro",
        "message_macro_save_highlights": "Enter filename to save all highlights as a macro file",
        "message_macro_save_command": "Enter filename to save current command as a macro file"
    }

    def translateInterface(self, language):
        code = self.codes[language]
        if code in translations:
            config.translationLanguage = language
            if hasattr(myTranslation, "translation"):
                open("myTranslation.py", "w", encoding="utf-8").close()
            return True
        else:
            print("translating interface into '{0}' ...".format(language))
            translator = Translator()
            tempDict = {}
            for key, value in self.translation.items():
                try:
                    tempDict[key] = translator.translate(value, dest=code).text
                except:
                    tempDict[key] = value
            #config.translationLanguage = language
            self.writeMyTranslation(tempDict, language)
            print("Done")
            return True
        return False

    def writeMyTranslation(self, translationDict, language):
        with open("myTranslation.py", "w", encoding="utf-8") as fileObj:
            content = "translationLanguage = {0}\ntranslation = {1}\n".format(pprint.pformat(language), pprint.pformat(translationDict))
            fileObj.write(content)

    def createTranslationTemplates(self):
        if googletransInstall:
            for code in self.codes.values():
                print("creating '{0}' template ...".format(code))
                translator = Translator()
                tempDict = {}
                for key, value in self.translation.items():
                    tempDict[key] = value
# Note: Attempted to use Google Translate to translate interface into all languages, but access is blocked in the middle of the operation.  It looks like Google blocks access by ip, when there are too many queries within a short time.
# Don't use the following 4 lines, or ip will be blocked for Google Translate
#                    try:
#                        tempDict[key] = translator.translate(value, dest=code).text
#                    except:
#                        tempDict[key] = value
                with open("translations.py", "a", encoding="utf-8") as fileObj:
                    code = code.replace("-", "")
                    fileObj.write("uB{0} = {1}\n\n".format(code, pprint.pformat(tempDict)))


if __name__ == '__main__':
    Languages().createTranslationTemplates()
